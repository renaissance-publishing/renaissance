from click import secho

import jinja2
import mistletoe

from dataclasses import dataclass, field
from os import makedirs
from os.path import join, exists
from shutil import copytree, rmtree
from typing import List, Optional

from pprint import pprint

from staticgen.discoverer import Discoverer, Page
from staticgen.renderers import RenaissanceHTMLRenderer


@dataclass(repr=True)
class TocEntry(object):
    title: str
    route: str
    anchor: str = ''
    children: list = field(default_factory=lambda: [])  # Should be List[TocEntry], buuuuuuut


def generate_toc(chapters: List[Page]) -> List[TocEntry]:
    toc: List[TocEntry] = []

    for chapter in chapters:
        level_stack: List[int] = [0]
        toc.append(TocEntry(chapter.title, chapter.route))
        toc_pointer_stack: List[List[TocEntry]] = [toc[-1].children]

        children = mistletoe.Document(chapter.content).children

        for heading in filter(lambda x: isinstance(x, mistletoe.block_token.Heading), children):
            if heading.level <= level_stack[-1]:
                while heading.level <= level_stack[-1]:
                    level_stack.pop()
                    toc_pointer_stack.pop()

            print(heading.children[0].content, level_stack)

            toc_pointer_stack[-1].append(TocEntry(heading.children[0].content, chapter.route, '#' + RenaissanceHTMLRenderer.heading_to_anchor(heading)))

            if heading.level > level_stack[-1]:
                level_stack.append(heading.level)
                toc_pointer_stack.append(toc_pointer_stack[-1][-1].children)

    return toc


class Builder(object):
    def __init__(self, disc: Discoverer):
        self.loader = jinja2.FileSystemLoader(str(disc.template_dir))
        self.env = jinja2.Environment(loader=self.loader, autoescape=jinja2.select_autoescape(['html', 'xml']))
        self.env.trim_blocks = True
        self.env.lstrip_blocks = True
        self.env.strip_trailing_newlines = False
        self.discoverer = disc

        if exists(self.discoverer.output_dir):
            rmtree(self.discoverer.output_dir)

    @property
    def context(self):
        return dict(self.discoverer)

    def render_site(self):
        branch = self.discoverer.current_branch
        sha = branch.commit.sha().hexdigest()
        secho(
            '\nBuilding site from branch "{branch}" (commit {hash}):'.format(branch=branch, hash=sha),
            fg='blue'
        )

        copytree(str(self.discoverer.static_dir), str(self.discoverer.static_out))
        self.render_pages()

    def render_pages(self):
        _ = self.discoverer.rules

        secho('Rendering pages:', fg='yellow')

        for page in self.discoverer.pages:
            self.render_page(page)

    def render_page(self, page: Page):
        page.content = mistletoe.markdown(page.content)
        local_ctx = self.context
        local_ctx['page'] = page

        rendered = self.env.get_template('page.html').render(local_ctx)
        path = self.discoverer.page_path(page)
        makedirs(str(path), exist_ok=True)

        with open(join(path, 'index.html'), 'w') as f:
            f.write(rendered)

        secho('• Rendered page "{}" successfully to route {}'.format(page.title, page.route), fg='green')

    def render_book(self):
        branch = self.discoverer.current_branch
        sha = branch.commit.sha().hexdigest()
        secho(
            '\nBuilding book revision from branch "{branch}" (commit {hash}):'.format(branch=branch, hash=sha),
            fg='blue'
        )

        _ = self.discoverer.rules

        chapters = self.discoverer.chapters

        for chapter in chapters:
            chapter.content = self.env.from_string(chapter.content).render(self.context)

        toc = generate_toc(chapters)

        secho('Rendering chapters:', fg='yellow')

        for chapter in chapters:
            self.render_chapter(chapter, toc)

    def render_chapter(self, chapter: Page, toc: List[TocEntry]):
        chapter.content = mistletoe.markdown(chapter.content, renderer=RenaissanceHTMLRenderer)
        local_ctx = self.context
        local_ctx['chapter'] = chapter
        local_ctx['toc'] = toc

        rendered = self.env.get_template('chapter.html').render(local_ctx)
        path = self.discoverer.chapter_path(chapter)
        makedirs(str(path), exist_ok=True)

        with open(join(path, 'index.html'), 'w') as f:
            f.write(rendered)

        secho('• Rendered chapter "{}" successfully'.format(chapter.title), fg='green')
