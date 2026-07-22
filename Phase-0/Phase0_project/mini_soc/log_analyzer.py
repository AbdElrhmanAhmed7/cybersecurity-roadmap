# ---------------- Module 2 --------------------------
from logging import getLevelNamesMapping
from datetime import datetime
from algorthims import *

class LogFormatError(Exception):
    """
    A properly-inheriting custom exception. Elsewhere in Phase 0,
    SecurityError was defined as `class SecurityError(object): pass` --
    that's a bug, since only subclasses of Exception can be raised.
    LogFormatError must inherit from Exception, not object.
    """
    pass


def read_log_lines(filename):
    """Reuse the existing generator as-is (see quick reference)."""
    with open(filename) as f:
        for file in f:
            yield file

def parse_log_line(line) -> tuple:
    """
    Assumes: line is "YYYY-MM-DD HH:MM:SS LEVEL message", possibly with
    a trailing newline (strip it first -- see quick reference).
    Guarantees: returns (timestamp, level, message).
    Raises: LogFormatError if the line doesn't match that shape.
    """
    line = line.strip().split(maxsplit=3)
    dates = line[0].split("-")
    levels = list(getLevelNamesMapping().keys())
    try:
        datetime(int(dates[0]), int(dates[1]), int(dates[2])).date()
        if line[2] in levels:
            return (line[0] + ' ' +line[1], line[2], line[3])
    except Exception as e:
        raise LogFormatError("Incorrected format.")


def filter_by_level(entries, levels=("WARNING", "ERROR")):
    """Returns only entries whose level is in `levels`."""
    result = []
    for entery in entries:
        if any(level in entery for level in levels):
            result.append(entery)
    return result

def sort_logs_by_timestamp(entries):
    """
    entries is a list of (timestamp, level, message) tuples. Tuple
    comparison in Python compares element-by-element, and timestamp is
    already first, so merge_sort(entries) sorts by timestamp correctly
    with NO wrapping needed -- string timestamps in "YYYY-MM-DD HH:MM:SS"
    format sort correctly with plain string comparison.
    """
    # TODO: return merge_sort(entries)
    return merge_sort(entries)


def find_log_at_timestamp(sorted_entries, timestamp):
    """
    Uses binary_search_recursive, which only returns True/False (see quick
    reference) -- this checks existence, it can't return the entry
    itself. If you need the actual entry, filter instead of searching.
    """
    return binary_search_recursive(timestamp, tuple(item[0] for item in sorted_entries))
