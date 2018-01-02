import sagadoc

import io
import pytest


@pytest.fixture
def docbuilder():
    return sagadoc.DocumentBuilder('tests')


@pytest.fixture
def strbuf():
    return io.StringIO()


def test_create_builder(docbuilder):
    assert docbuilder is not None


def test_add_data_source_nonexistent(docbuilder):
    with pytest.raises(FileNotFoundError):
        docbuilder.add_data_source('does-not-exist.yaml')


def test_make_context(docbuilder):
    docbuilder.add_data_source('fixtures/simple-data.yaml')
    context = docbuilder.make_context()
    assert 'foo' in context
    assert context['foo'] == 'bar'


def test_build_no_logic(docbuilder, strbuf):
    docbuilder.build('fixtures/no-logic.tmpl', strbuf)
    assert 'Build successful!' in strbuf.getvalue()


def test_build_no_data(docbuilder, strbuf):
    docbuilder.build('fixtures/simple.tmpl', strbuf)
    assert 'Six times seven is 42' in strbuf.getvalue()


def test_build_with_data(docbuilder, strbuf):
    docbuilder.add_data_source('fixtures/simple-data.yaml')
    docbuilder.build('fixtures/simple-data.tmpl', strbuf)
    assert 'Value of "foo" is: bar' in strbuf.getvalue()


def test_build_with_script(docbuilder, strbuf):
    docbuilder.add_script('fixtures/simple-script.py')
    docbuilder.build('fixtures/simple-script.tmpl', strbuf)
    assert 'Hello from Python' in strbuf.getvalue()
    
