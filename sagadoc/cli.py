# -*- coding: utf-8 -*-

"""Console script for sagadoc."""

import click
from traceback import format_exc
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
@click.pass_context
def build(ctx, output, template, data):
    builder = DocumentBuilder()
    for source in data:
        builder.add_data_source(source)
    try:
        builder.build(template, output)
    except Exception:
        click.echo(click.style('Error occurred while rendering template:',
                               fg='red'))
        click.echo('='*78)
        click.echo(format_exc())
        click.echo(click.style('Aborting',
                               fg='red'))
        click.echo('='*78)
        ctx.exit(1)


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
