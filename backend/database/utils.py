"""
File containing utilities for database operations.
"""

from contextlib import contextmanager
from datetime import date
from typing import Any, Optional, Type, Union

from dateutil import parser

from backend.database.base import Session


def repr_helper(arg: Optional[str]) -> Optional[str]:
    """
    If argument provided is a string, return with double quotes. If it's None, then just return None.
    :return: String or None depending on what type of argument was passed.
    """
    if arg is None:
        return None

    return f'"{arg}"'


@contextmanager
def yield_helper(to_yield: Any) -> Any:
    """
    Context manager to yield object provided.
    :param to_yield: Object to yield.
    :return: Yield object that was passed as an argument.
    """
    yield to_yield


@contextmanager
def session_scope(session_object: Type[Session] = Session) -> Session:
    """
    Provide a transactional scope around a series of operations.
    :param session_object: Session object to instantiate.
    """
    session = session_object()
    try:
        yield session
        session.commit()
    except Exception:  # pylint: disable=broad-except
        session.rollback()
        raise
    finally:
        session.close()


def parse_date(date_object: Union[str, date], null_ok: bool = False) -> date:
    """
    Helper function to parse dates and return as date objects.
    :param null_ok: Boolean whether null date objects are valid or not.
    :param date_object: Date object to parse.
    :return: Parsed date object.
    """
    if isinstance(date_object, date):
        return date_object

    if date_object is None and null_ok:
        return date.today()

    return parser.parse(date_object).date()
