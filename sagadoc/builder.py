# -*- coding: utf-8 -*-

"""Main class for building documents."""

import pathlib
from mako.lookup import TemplateLookup
from ruamel.yaml import YAML


class DocumentBuilder:

    def __init__(self, home='.'):
        self.data_sources = []
        self.home = pathlib.Path(home)
        self.template_lookup = TemplateLookup(directories=[home],
                                              input_encoding='utf-8')

    def add_data_source(self, filename):
        if not isinstance(filename, pathlib.Path):
            filename = pathlib.Path(filename)

        filename = (self.home / filename).resolve(strict=True)
        self.data_sources.append(filename)

    def _make_context(self):
        yaml = YAML()
        context = {}
        for source in self.data_sources:
            with open(source) as infile:
                new_context = yaml.load(infile)
            context.update(new_context)
        return context

    def build(self, template_name, output):
        context = self._make_context()
        template = self.template_lookup.get_template(template_name)
        rendered = template.render_unicode(**context)
        output.write(rendered)
