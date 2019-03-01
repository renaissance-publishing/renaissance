from click import secho

import jinja2
import mistletoe

from os import makedirs
from os.path import join, exists
from shutil import copytree, rmtree
from typing import List

from staticgen.discoverer import Discoverer, Page
from staticgen.renderers import RenaissanceHTMLRenderer


def generate_toc(chapters: List[Page]) -> str:
    toc: List[str] = ['<ol>']
    link_t: str = '<a href="../{route}/{anchor}">{title}</a>'

    for chapter in chapters:
        toc.append('<li>')
        toc.append(link_t.format(title=chapter.title, route=chapter.route, anchor=''))
        children = mistletoe.Document(chapter.content).children

        level_stack: List[int] = [0]
        for heading in filter(lambda x: isinstance(x, mistletoe.block_token.Heading), children):
            if heading.level == 4:
                continue

            if heading.level > level_stack[-1]:
                level_stack.append(heading.level)
                toc.append('<ol><li>')
            elif heading.level == level_stack[-1]:
                toc.append('</li><li>')
            else:
                while heading.level < level_stack[-1]:
                    level_stack.pop()
                    toc.append('</li></ol>')
                toc.append('<li>')

            toc.append(link_t.format(title=heading.children[0].content, route=chapter.route,
                                     anchor='#' + RenaissanceHTMLRenderer.heading_to_anchor(heading)))

        for _ in level_stack[1:]:
            toc.append('</li></ol>')

    toc.append('</ol>')

    return ''.join(toc)


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
        toc = generate_toc(chapters)

        secho('Rendering chapters:', fg='yellow')

        for chapter in chapters:
            self.render_chapter(chapter, toc)

    def render_chapter(self, chapter: Page, toc: str):
        chapter.content = self.env.from_string(chapter.content).render(self.context)
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
