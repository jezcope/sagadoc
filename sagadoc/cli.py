# -*- coding: utf-8 -*-

"""Console script for sagadoc."""

import click
import jinja2
from ruamel.yaml import YAML
# from pprint import pprint as pp

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./templates'),
)


@click.group()
def main(args=None):
    """Console script for sagadoc."""
    pass


@main.command()
def build():
    yaml = YAML()
    with open('cv.yaml') as infile:
        cv_data = yaml.load(infile)
    template = env.get_template('cv-full.tex')
    output = template.render(cv_data)
    click.echo(output)


if __name__ == "__main__":
    main()
