"""Tests for src.nbpreview_rtlabs.component.row."""
import pathlib

import nbformat
import pytest

from nbpreview_rtlabs.component import row


def test_render_unknown_output_type() -> None:
    """It does not render an unknown output type."""
    notebook_outputs = [
        nbformat.from_dict({"output_type": "unknown"})  # type: ignore[no-untyped-call]
    ]
    rendered_output_row = row.render_output_row(
        notebook_outputs,
        plain=True,
        unicode=True,
        hyperlinks=True,
        nerd_font=True,
        files=True,
        hide_hyperlink_hints=True,
        theme="ansi_dark",
        pad=(0, 1, 0, 0),
        images=False,
        image_drawing="braille",
        color=True,
        negative_space=True,
        relative_dir=pathlib.Path(),
    )
    with pytest.raises(StopIteration):
        next(rendered_output_row)
