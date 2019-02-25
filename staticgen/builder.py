import blessings
from click import echo
import jinja2
import mistletoe
import os
from typing import List, Tuple

from staticgen.discoverer import Page, Chapter
from staticgen.renderers import RenaissanceHTMLRenderer
from pathlib import Path

term = blessings.Terminal()


class Builder(object):
    def __init__(self, output_dir: Path, template_dir: Path, **global_ctx):
        echo(term.yellow('output_dir is: {}'.format(output_dir)))
        self.output_dir = output_dir.resolve()
        os.makedirs(str(self.output_dir), exist_ok=True)

        self.loader = jinja2.FileSystemLoader(str(template_dir))
        self.env = jinja2.Environment(loader=self.loader, autoescape=jinja2.select_autoescape(['html', 'xml']))
        self.env.trim_blocks = True
        self.env.lstrip_blocks = True
        self.env.strip_trailing_newlines = False
        self.global_ctx = global_ctx

    def render_page(self, page: Page):
        page.content = mistletoe.markdown(page.content)
        local_ctx = self.global_ctx.copy()
        local_ctx['page'] = page

        rendered = self.env.get_template('page.html').render(local_ctx)
        path = self.output_dir / page.output_route
        os.makedirs(str(path), exist_ok=True)

        echo(term.green('• Rendered page "{}" successfully to route {}'.format(page.title, page.route)))

        with open(str(path / 'index.html'), 'w') as f:
            f.write(rendered)

    def generate_toc(self, chapters: List[Chapter]):
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

        self.global_ctx['toc'] = ''.join(toc)

    def render_chapter(self, chapter: Chapter, book_only: bool = False):
        chapter.content = self.env.from_string(chapter.content).render(self.global_ctx)
        chapter.content = mistletoe.markdown(chapter.content, renderer=RenaissanceHTMLRenderer)
        local_ctx = self.global_ctx.copy()
        local_ctx['chapter'] = chapter

        rendered = self.env.get_template('chapter.html').render(local_ctx)
        path = {True: self.output_dir, False: self.output_dir / 'book'}[book_only] / chapter.output_route
        os.makedirs(str(path), exist_ok=True)

        echo(term.green('• Rendered chapter "{}" successfully'.format(chapter.title)))

        with open(str(path / 'index.html'), 'w') as f:
            f.write(rendered)
