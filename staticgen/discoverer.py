import blessings
from click import echo
from dataclasses import dataclass
import frontmatter
from mistletoe.block_token import Document
from os import walk
from os.path import join
from pathlib import Path
from typing import Iterator, List, Union

from staticgen.rulesdata import RulesData

term = blessings.Terminal()


@dataclass
class Page(object):
    title: str
    route: Path
    content: str
    output_route: Path

    def __init__(self, title: str, route: str, content: str):
        self.title = title
        self.route = Path(route)
        self.content = content
        self.output_route = Path('.' + route)


@dataclass
class Chapter(object):
    title: str
    route: Path
    content: Union[str, Document]
    output_route: Path
    sections: List[str]

    def __init__(self, title: str, route: str, content: str):
        self.title = title
        self.route = Path(route)
        self.content = content
        self.output_route = Path(route)
        self.sections = []


class Discoverer(object):
    def __init__(self, project_root: Path):
        echo(term.yellow('project_root is: {}'.format(project_root)))

        self.content_dir = project_root / 'content'
        self.chapter_dir = self.content_dir / 'chapters'
        self.page_dir = self.content_dir / 'pages'
        self.rules_dir = self.content_dir / 'rules-data'

        self.layout_dir = project_root / 'layout'
        self.static_dir = self.layout_dir / 'static'
        self.template_dir = self.layout_dir / 'templates'

    def pages(self) -> Iterator[Page]:
        for root, dirs, files in walk(str(self.page_dir)):
            for fn in files:
                page = frontmatter.load(join(root, fn))

                try:
                    page_title = page['title']
                    page_route = page['route']
                    page_content = page.content

                    yield Page(page_title, page_route, page_content)
                except KeyError as e:
                    echo(term.bold_red(
                        'Missing required key "{}" in the front matter of "{}"'.format(e.args[0], fn)
                    ))

    def chapters(self) -> Iterator[Chapter]:
        for root, dirs, files in walk(str(self.chapter_dir)):
            for fn in sorted(files):
                page = frontmatter.load(join(root, fn))

                try:
                    chapter_title = page['title']
                    chapter_route = fn[3:-3]
                    chapter_content = page.content

                    yield Chapter(chapter_title, chapter_route, chapter_content)
                except KeyError as e:
                    echo(term.bold_red(
                        'Missing required key "{}" in the front matter of "{}"'.format(e.args[0], fn)
                    ))

    def rules_data(self) -> RulesData:
        it = walk(str(self.rules_dir))
        next(it)

        return RulesData(it)
