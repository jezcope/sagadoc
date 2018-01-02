# -*- coding: utf-8 -*-

"""Console script for sagadoc."""

import click
from mako.lookup import TemplateLookup
from ruamel.yaml import YAML
# from pprint import pprint as pp

lookup = TemplateLookup(directories=['./templates'],
                        input_encoding='utf-8')


@click.group()
def main(args=None):
    """Console script for sagadoc."""
    pass


@main.command()
@click.option('--output', '-O',
              type=click.File('w'),
              default='-')
def build(output):
    yaml = YAML()
    with open('cv.yaml') as infile:
        cv_data = yaml.load(infile)
    template = lookup.get_template('/cv-full.tex')
    rendered = template.render_unicode(**cv_data)
    output.write(rendered)


if __name__ == "__main__":
    main()
