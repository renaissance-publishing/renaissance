from click import secho

from dataclasses import dataclass
from functools import total_ordering
from funcy.py3 import lmap, omit, partial
import inspect
from typing import List, Optional, Tuple, Union

import frontmatter
# noinspection PyProtectedMember
from mistletoe.block_token import Document

from os import walk
from os.path import join, dirname, realpath
from pathlib import Path

from dulwich.index import build_index_from_tree
from dulwich.objects import Commit
from dulwich.repo import Repo

from staticgen.rulesdata import RulesData

project_root: str = dirname(dirname(realpath(inspect.getfile(inspect.currentframe()))))


@dataclass
class Page(object):
    title: str
    route: str
    content: Union[str, Document]


@dataclass(eq=False, frozen=True)
@total_ordering
class Branch(object):
    name: str
    commit: Commit

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.commit == other.commit

    def __lt__(self, other):
        return self.commit.commit_time < other.commit.commit_time

    @staticmethod
    def from_tuple(repo: Repo, tup: Tuple[bytes, bytes]):
        name = tup[0].decode()
        commit = repo[tup[1]]

        return Branch(name, commit)


class Discoverer(object):
    __current_branch: Optional[Branch] = None
    project_root: Path
    repo_root: Path
    project_repo: Repo

    __pages: Optional[List[Page]] = None
    __chapters: Optional[List[Page]] = None
    __rules: Optional[RulesData] = None

    def __init__(self, p_root: str, o_dir: str):
        secho('project_root is: {}'.format(p_root), fg='yellow')
        self.project_root = Path(p_root)
        self.output_dir = Path(o_dir)

        self.repo = Repo(p_root)
        self.repo_root = self.project_root

    @property
    def content_dir(self) -> Path:
        return self.project_root / 'content'

    @property
    def chapter_dir(self) -> Path:
        return self.content_dir / 'chapters'

    @property
    def page_dir(self) -> Path:
        return self.content_dir / 'pages'

    @property
    def rules_dir(self) -> Path:
        return self.content_dir / 'rules-data'

    @property
    def layout_dir(self) -> Path:
        return self.repo_root / 'layout'

    @property
    def static_dir(self) -> Path:
        return self.layout_dir / 'static'

    @property
    def static_out(self):
        return self.output_dir / 'static'

    @property
    def template_dir(self) -> Path:
        return self.layout_dir / 'templates'

    @property
    def branches(self) -> List[Branch]:
        return sorted(
            lmap(partial(Branch.from_tuple, self.repo),
                 omit(self.repo.refs.as_dict(b'refs/heads'), [b'master']).items()), reverse=True)

    @property
    def current_branch(self) -> Branch:
        if not self.__current_branch:
            head = self.repo.refs.follow(b'HEAD')
            name = head[0][-1][11:].decode()
            commit = self.repo[head[1]]

            return Branch(name, commit)

        return self.__current_branch

    def access_branch(self, branch: Branch, directory: str):
        if branch != self.current_branch:
            index_path = join(directory, 'index')
            object_store = self.repo.object_store

            build_index_from_tree(directory, index_path, object_store, branch.commit.tree)

            self.project_root = Path(directory)
            self.__current_branch = branch

        self.__pages = None
        self.__chapters = None
        self.__rules = None

    def parent_branch(self):
        self.project_root = self.repo_root
        self.__current_branch = None

    @property
    def pages(self) -> List[Page]:
        if not self.__pages:
            self.__pages = []

            for root, dirs, files in walk(str(self.page_dir)):
                for fn in files:
                    print(join(root, fn))
                    page = frontmatter.load(join(root, fn))

                    try:
                        page_title = page['title']
                        page_route = page['route']
                        page_content = page.content

                        self.__pages.append(Page(page_title, page_route, page_content))
                    except KeyError as e:
                        secho(
                            'Missing required key "{}" in the front matter of "{}"'.format(e.args[0], fn),
                            fg='red', bold=True
                        )

        return self.__pages

    def page_path(self, page: Page):
        if page.route == '/':
            return self.output_dir

        return self.output_dir / page.route

    @property
    def chapters(self) -> List[Page]:
        if not self.__chapters:
            self.__chapters = []

            for root, dirs, files in walk(str(self.chapter_dir)):
                for fn in sorted(files):
                    page = frontmatter.load(join(root, fn))

                    try:
                        chapter_title = page['title']
                        chapter_route = fn[3:-3]
                        chapter_content = page.content

                        self.__chapters.append(Page(chapter_title, chapter_route, chapter_content))
                    except KeyError as e:
                        secho(
                            'Missing required key "{}" in the front matter of "{}"'.format(e.args[0], fn),
                            fg='red', bold=True
                        )

        return self.__chapters

    def chapter_path(self, chapter: Page):
        if self.current_branch.name == 'source':
            return self.output_dir / 'book' / chapter.route

        return self.output_dir / 'book' / self.current_branch.name / chapter.route

    @property
    def rules(self) -> RulesData:
        if not self.__rules:
            it = walk(str(self.rules_dir))
            next(it)
            self.__rules = RulesData(it)

        return self.__rules

    @staticmethod
    def keys() -> List[str]:
        return ['pages', 'rules', 'chapters', 'branches', 'current_branch']

    def __getitem__(self, key):
        if key not in self.keys():
            raise KeyError(key)
        return getattr(self, key)
