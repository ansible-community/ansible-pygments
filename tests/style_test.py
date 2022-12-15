# pylint: disable=redefined-outer-name
"""Tests for Pygments styles."""

try:
    from importlib_metadata import entry_points as _load_entry_points
except ImportError:
    from importlib.metadata import entry_points as _load_entry_points

from io import StringIO

from pygments.formatters import get_formatter_by_name as _get_formatter_by_name
from pygments.lexers import get_lexer_by_name as _get_lexer_by_name
from pygments.style import Style as _PygmentsStyleType
from pygments.styles import get_style_by_name as _get_style_by_name

import pytest


@pytest.fixture(params=('Ansible', 'ansible'))
def style_name(request):
    """Return a distribution entry point style name."""
    return request.param


@pytest.fixture
def style_class_object(style_name):
    """Load a Pygments style by distribution entrypoint name."""
    return _get_style_by_name(style_name)


def test_entry_points(style_class_object, style_name):
    """Check that proper Pygments styles are exposed as entry points.

    This test loads the style by name specified in the distribution package
    entry points using both import machinery and a Pygments helper function.
    It then compares them by identity.
    """
    pygments_styles_eps = {
        entry_point for entry_point in _load_entry_points(
            name=style_name,
            group='pygments.styles',
        )
        if entry_point.value.startswith('ansible_pygments.')
    }

    assert len(pygments_styles_eps) == 1

    pygments_style = pygments_styles_eps.pop().load()
    assert issubclass(pygments_style, _PygmentsStyleType)
    assert pygments_style is style_class_object


def test_style_highlighting(style_class_object):
    """Check that colors specified in the Pygments style are applied.

    This test uses ``BBCodeFormatter`` to emit style text as it produces
    output that is easy to read and compare.
    """
    tokens = list(_get_lexer_by_name('python3').get_tokens('print("thing")'))
    pygments_formatter = _get_formatter_by_name(
        'bbcode',
        style=style_class_object,
    )

    expected_styled_bb_code_txt = (
        '[color=#0086b3]print[/color][b]([/b]'
        '[color=#dd1144]"thing"[/color][b])[/b]\n'
    )

    with StringIO() as io_stream:
        pygments_formatter.format(tokens, io_stream)

        produced_styled_bbcode_txt = io_stream.getvalue()

        assert produced_styled_bbcode_txt == expected_styled_bb_code_txt
