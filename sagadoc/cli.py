# -*- coding: utf-8 -*-

"""Console script for sagadoc."""

import click
from pprint import pformat

from sagadoc import DocumentBuilder


@click.group()
def main(args=None):
    """Console script for sagadoc."""
    pass


@main.command()
@click.option('--output', '-O',
              type=click.File('w'),
              default='-')
@click.option('--data', '-d',
              type=click.Path(exists=True),
              multiple=True)
@click.option('--template', '-t',
              type=click.Path(exists=True))
def build(output, template, data):
    builder = DocumentBuilder()
    for source in data:
        builder.add_data_source(source)
    builder.build(template, output)


@main.command()
@click.option('--output', '-O',
              type=click.File('w'),
              default='-')
@click.option('--data', '-d',
              type=click.Path(exists=True),
              multiple=True)
def dump(output, data):
    builder = DocumentBuilder()
    for source in data:
        builder.add_data_source(source)
    context = builder.make_context()
    output.write(pformat(context))


if __name__ == "__main__":
    main()
