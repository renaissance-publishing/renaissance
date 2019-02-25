import click
import colorama
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import inspect
from os.path import dirname, exists, join, realpath
from pathlib import Path
from shutil import copytree, rmtree
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import staticgen.discoverer
import staticgen.builder

colorama.init()

project_root = dirname(dirname(realpath(inspect.getfile(inspect.currentframe()))))


@click.group()
def cli():
    pass


@cli.command(help='Build the static site.')
@click.option('--input-dir', metavar='DIR', default=project_root, help='Input directory. [default: the directory '
                                                                       'containing staticgen.py]')
@click.option('--output-dir', default='./build', metavar='DIR', help='Output directory. [default: ./build]')
@click.option('--book-only', default=False, help='Only output the book in HTML and PDF formats. (Useful for pinned '
                                                 'versions.) [default: False]')
def build(input_dir: str, output_dir: str, book_only: bool):
    if exists(output_dir):
        rmtree(output_dir)

    d = discoverer.Discoverer(Path(input_dir))

    pages = list(d.pages())
    chapters = list(d.chapters())
    rd = d.rules_data()

    b = builder.Builder(Path(output_dir), d.template_dir, pages=pages, chapters=chapters, rules=rd)

    if not book_only:
        copytree(d.static_dir, join(output_dir, 'static'))

        for page in pages:
            b.render_page(page)

    b.generate_toc(chapters)
    for chapter in chapters:
        b.render_chapter(chapter, book_only)


@cli.command(help='Run a testing server that automatically rebuilds the site.')
@click.pass_context
def serve(ctx):
    class RebuildEventHandler(FileSystemEventHandler):
        def on_any_event(self, event):
            ctx.invoke(build)

    class SiteHTTPRequestHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super(SiteHTTPRequestHandler, self).__init__(*args, directory=join(project_root, 'build'), **kwargs)

    ctx.invoke(build)

    observer = Observer()
    observer.schedule(RebuildEventHandler(), join(project_root, 'content'), recursive=True)
    observer.schedule(RebuildEventHandler(), join(project_root, 'layout'), recursive=True)
    observer.start()

    try:
        httpd = ThreadingHTTPServer(('', 8080), SiteHTTPRequestHandler)
        httpd.serve_forever()
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
