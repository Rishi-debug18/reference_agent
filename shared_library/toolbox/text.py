"""Text helpers. The worked example every contribution is modelled on."""
import os
import subprocess
import sys


def word_count(text):
    """Count whitespace-separated words.

    >>> word_count("one two three")
    3
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text.split())


def truncate(text, limit, suffix="..."):
    """Shorten text to limit characters, ending with suffix.

    The result is never longer than limit.

    >>> truncate("hello world", 8)
    'hello...'
    >>> truncate("short", 20)
    'short'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if limit < len(suffix):
        raise ValueError("limit must be at least len(suffix)")
    if len(text) <= limit:
        return text
    return text[:limit - len(suffix)] + suffix


def open_review_in_notepad(file_path="review.txt", template=None, launch=True):
    """Create or prepare a review.txt file and open it in Notepad.

    If the file does not exist, a structured review template is written to it.
    Launches Notepad so a reviewer can write and submit their review.

    Parameters
    ----------
    file_path : str, optional
        Target file path (defaults to 'review.txt').
    template : str, optional
        Custom template or review content to write into the file.
    launch : bool, optional
        Whether to launch Notepad (defaults to True).

    Returns
    -------
    str
        The absolute path to the review file.
    """
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if template is not None and not isinstance(template, str):
        raise TypeError("template must be a string")

    default_template = (
        "===================================================\n"
        "REPOSITORY REVIEW: reference_agent\n"
        "===================================================\n"
        "Reviewer Name : \n"
        "Review Date   : \n\n"
        "--- Checklist ---\n"
        "[ ] Project structure and clarity\n"
        "[ ] Code modularity and cleanliness\n"
        "[ ] Documentation and setup guides\n"
        "[ ] Tests pass cleanly\n\n"
        "--- Feedback & Observations ---\n"
        "Strengths:\n"
        "- \n\n"
        "Suggestions for improvement:\n"
        "- \n\n"
        "Overall Rating (1-5): \n"
        "Verdict (Approved / Changes Requested): \n"
        "===================================================\n"
    )

    content = template if template is not None else default_template

    if not os.path.exists(file_path) or template is not None:
        with open(file_path, "w", encoding="utf-8") as fh:
            fh.write(content)

    abs_path = os.path.abspath(file_path)

    if launch:
        if sys.platform.startswith("win"):
            subprocess.Popen(["notepad.exe", abs_path])
        else:
            editor = os.environ.get("EDITOR", "nano")
            subprocess.Popen([editor, abs_path])

    return abs_path


def submit_review(file_path="review.txt", content=None, open_notepad=True):
    """Save review text to file and optionally open it in Notepad.

    Parameters
    ----------
    file_path : str, optional
        Target review file (defaults to 'review.txt').
    content : str, optional
        Review content to save.
    open_notepad : bool, optional
        Whether to open Notepad (defaults to True).

    Returns
    -------
    str
        The absolute path to the review file.
    """
    return open_review_in_notepad(
        file_path=file_path, template=content, launch=open_notepad
    )

