"""Jupyter notebook output data."""
from typing import Union

from nbpreview_rtlabs.component.content.output.error import Error
from nbpreview_rtlabs.component.content.output.result.result import Result
from nbpreview_rtlabs.component.content.output.stream import Stream

Output = Union[Result, Error, Stream]
