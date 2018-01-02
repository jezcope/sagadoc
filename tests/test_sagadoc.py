#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `saga` command line tool."""

import pytest

from click.testing import CliRunner

from sagadoc import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_help(runner):
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_dump(runner):
    dump_result = runner.invoke(cli.dump, ['-d', 'tests/fixtures/simple-data.yaml'])
    assert dump_result.exit_code == 0, dump_result.output
    assert "'foo': 'bar'" in dump_result.output


def test_build(runner):
    build_result = runner.invoke(cli.build, ['-t', 'tests/fixtures/no-logic.tmpl'])
    assert build_result.exit_code == 0, build_result.output
    assert 'Build successful!' in build_result.output


def test_build_with_data(runner):
    build_result = runner.invoke(cli.build, ['-t', 'tests/fixtures/simple-data.tmpl',
                                             '-d', 'tests/fixtures/simple-data.yaml'])
    assert build_result.exit_code == 0, build_result.output
    assert 'Value of "foo" is: bar' in build_result.output
