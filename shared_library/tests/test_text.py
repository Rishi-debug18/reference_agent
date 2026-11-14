"""Tests for toolbox.text - the shape every contribution copies."""
import pytest

from toolbox.text import truncate, word_count


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
