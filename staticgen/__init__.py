import click
from click import secho

from tempfile import TemporaryDirectory

from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from os.path import join
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from staticgen.discoverer import Discoverer, project_root
from staticgen.builder import Builder


@click.group()
def cli():
    pass


# noinspection PyShadowingNames
@cli.command(help='Build the static site.')
@click.option('--input-dir', metavar='DIR', default=project_root, help='Input directory. [default: the directory '
                                                                       'containing staticgen.py]')
@click.option('--output-dir', default='./build', metavar='DIR', help='Output directory. [default: ./build]')
def build(input_dir: str, output_dir: str):

    discoverer = Discoverer(input_dir, output_dir)
    builder = Builder(discoverer)

    with TemporaryDirectory() as tmp:
        source = next(filter(lambda b: b.name == 'source', discoverer.branches))
        discoverer.access_branch(source, tmp)
        builder.render_site()

    for branch in discoverer.branches:
        with TemporaryDirectory() as tmp:
            discoverer.access_branch(branch, tmp)
            builder.render_book()


@cli.command(help='Run a testing server that automatically rebuilds the site.')
@click.option('--input-dir', metavar='DIR', default=project_root, help='Input directory. [default: the directory '
                                                                       'containing staticgen.py]')
@click.option('--output-dir', default='./build', metavar='DIR', help='Output directory. [default: ./build]')
@click.pass_context
def serve(ctx: click.Context, *_, **__):
    class RebuildEventHandler(FileSystemEventHandler):
        def on_any_event(self, event):
            ctx.forward(build)

    class SiteHTTPRequestHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super(SiteHTTPRequestHandler, self).__init__(*args, directory=join(project_root, 'build'), **kwargs)

    ctx.forward(build)

    observer = Observer()
    observer.schedule(RebuildEventHandler(), join(project_root, 'content'), recursive=True)
    observer.schedule(RebuildEventHandler(), join(project_root, 'layout'), recursive=True)
    observer.start()

    try:
        httpd = ThreadingHTTPServer(('', 8080), SiteHTTPRequestHandler)
        secho('Now serving at http://127.0.0.1:8080', fg='blue')
        httpd.serve_forever()
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
