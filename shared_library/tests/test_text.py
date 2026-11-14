"""Tests for toolbox.text - the shape every contribution copies."""
import os
import pytest

from toolbox.text import (
    open_review_in_notepad,
    submit_review,
    truncate,
    word_count,
)


def test_word_count_counts_words():
    assert word_count("one two three") == 3


def test_word_count_handles_extra_whitespace():
    assert word_count("  one   two  ") == 2


def test_word_count_rejects_non_strings():
    with pytest.raises(TypeError):
        word_count(42)


def test_truncate_shortens_and_marks():
    assert truncate("hello world", 8) == "hello..."


def test_truncate_leaves_short_text_alone():
    assert truncate("short", 20) == "short"


def test_truncate_never_exceeds_the_limit():
    assert len(truncate("a" * 100, 10)) == 10


def test_open_review_in_notepad_creates_file(tmp_path):
    review_file = str(tmp_path / "review.txt")
    path = open_review_in_notepad(review_file, launch=False)
    assert os.path.exists(path)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "REPOSITORY REVIEW: reference_agent" in content


def test_open_review_in_notepad_custom_template(tmp_path):
    review_file = str(tmp_path / "review.txt")
    custom_text = "Looks good to me!"
    path = open_review_in_notepad(review_file, template=custom_text, launch=False)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == custom_text


def test_open_review_in_notepad_rejects_invalid_types():
    with pytest.raises(TypeError):
        open_review_in_notepad(123, launch=False)
    with pytest.raises(TypeError):
        open_review_in_notepad("review.txt", template=123, launch=False)


def test_submit_review_writes_and_returns_path(tmp_path):
    review_file = str(tmp_path / "my_review.txt")
    path = submit_review(
        file_path=review_file, content="LGTM", open_notepad=False
    )
    assert os.path.exists(path)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == "LGTM"

