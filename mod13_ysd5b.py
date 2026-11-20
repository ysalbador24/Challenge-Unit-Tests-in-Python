"""Unit Testing in Python - Yesenia Salbador (ysd5b).

Validate the five stock visualizer inputs using this challenge's rules.
The validators are included so this file can run without Flask, an API key,
or the rest of Project 3. These tests exercise the validators below, rather
than importing the web edition's more permissive validation functions.

Run: python3 mod13_ysd5b.py
"""

import re
import unittest
from datetime import date


def validate_symbol(value):
    """Accept only strings containing 1-7 uppercase letters A-Z."""
    return isinstance(value, str) and re.fullmatch(r"[A-Z]{1,7}", value) is not None


def validate_chart_type(value):
    """Accept one numeric input character: 1 (Bar) or 2 (Line)."""
    return isinstance(value, str) and value in ("1", "2")


def validate_time_series(value):
    """Accept one numeric input character from 1 through 4."""
    return isinstance(value, str) and value in ("1", "2", "3", "4")


def validate_date(value):
    """Accept a real calendar date written exactly as YYYY-MM-DD."""
    if not isinstance(value, str):
        return False
    if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value) is None:
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def validate_start_date(value):
    """Validate the start date's format and calendar validity."""
    return validate_date(value)


def validate_end_date(value):
    """Validate the end date's format and calendar validity."""
    return validate_date(value)


class TestSymbol(unittest.TestCase):
    def test_valid_symbols(self):
        for value in ("A", "GOOGL", "MSFT", "ABCDEFG"):
            with self.subTest(value=value):
                self.assertTrue(validate_symbol(value))

    def test_invalid_length(self):
        for value in ("", "ABCDEFGH"):
            with self.subTest(value=value):
                self.assertFalse(validate_symbol(value))

    def test_lowercase_and_mixed_case(self):
        for value in ("aapl", "Googl", "a"):
            with self.subTest(value=value):
                self.assertFalse(validate_symbol(value))

    def test_nonletters_and_whitespace(self):
        for value in ("AAPL1", "123", "BRK.B", "A-B", "A B", " AAPL", "AAPL ", "AAPL\n", "É"):
            with self.subTest(value=value):
                self.assertFalse(validate_symbol(value))

    def test_nonstring_inputs(self):
        for value in (None, 123, True, ["AAPL"]):
            with self.subTest(value=value):
                self.assertFalse(validate_symbol(value))


class TestChartType(unittest.TestCase):
    def test_valid_choices(self):
        for value in ("1", "2"):
            with self.subTest(value=value):
                self.assertTrue(validate_chart_type(value))

    def test_out_of_range(self):
        for value in ("0", "3", "9", "-1"):
            with self.subTest(value=value):
                self.assertFalse(validate_chart_type(value))

    def test_multiple_characters(self):
        for value in ("12", "01", "1.0", " 1", "2 ", "1\n"):
            with self.subTest(value=value):
                self.assertFalse(validate_chart_type(value))

    def test_empty_and_nonnumeric(self):
        for value in ("", " ", "a", "Bar", "Line", "１"):
            with self.subTest(value=value):
                self.assertFalse(validate_chart_type(value))

    def test_nonstring_inputs(self):
        for value in (None, 1, 2.0, True, ["1"]):
            with self.subTest(value=value):
                self.assertFalse(validate_chart_type(value))


class TestTimeSeries(unittest.TestCase):
    def test_valid_choices(self):
        for value in ("1", "2", "3", "4"):
            with self.subTest(value=value):
                self.assertTrue(validate_time_series(value))

    def test_out_of_range(self):
        for value in ("0", "5", "9", "-1"):
            with self.subTest(value=value):
                self.assertFalse(validate_time_series(value))

    def test_multiple_characters(self):
        for value in ("14", "04", "4.0", " 1", "4 ", "3\n"):
            with self.subTest(value=value):
                self.assertFalse(validate_time_series(value))

    def test_empty_and_nonnumeric(self):
        for value in ("", " ", "a", "Daily", "Weekly", "４"):
            with self.subTest(value=value):
                self.assertFalse(validate_time_series(value))

    def test_nonstring_inputs(self):
        for value in (None, 4, 1.0, True, ["4"]):
            with self.subTest(value=value):
                self.assertFalse(validate_time_series(value))


class TestStartDate(unittest.TestCase):
    def test_valid_dates(self):
        for value in ("2026-01-01", "2026-12-31", "2024-02-29", "2000-02-29"):
            with self.subTest(value=value):
                self.assertTrue(validate_start_date(value))

    def test_invalid_format(self):
        for value in ("", "11/20/2026", "20-11-2026", "2026-1-01", "2026-01-1", "26-01-01", "20260101"):
            with self.subTest(value=value):
                self.assertFalse(validate_start_date(value))

    def test_impossible_dates(self):
        for value in ("2026-02-29", "1900-02-29", "2026-04-31", "2026-13-01", "2026-00-01", "2026-01-00", "0000-01-01"):
            with self.subTest(value=value):
                self.assertFalse(validate_start_date(value))

    def test_extra_characters(self):
        for value in (" 2026-01-01", "2026-01-01 ", "2026-01-01\n", "2026-01-01T12:00:00", "abcd-ef-gh"):
            with self.subTest(value=value):
                self.assertFalse(validate_start_date(value))

    def test_nonstring_inputs(self):
        for value in (None, 20260101, True, date(2026, 1, 1)):
            with self.subTest(value=value):
                self.assertFalse(validate_start_date(value))


class TestEndDate(unittest.TestCase):
    def test_valid_dates(self):
        for value in ("2026-01-01", "2026-12-31", "2024-02-29", "2000-02-29"):
            with self.subTest(value=value):
                self.assertTrue(validate_end_date(value))

    def test_invalid_format(self):
        for value in ("", "11/20/2026", "20-11-2026", "2026-1-01", "2026-01-1", "26-01-01", "20260101"):
            with self.subTest(value=value):
                self.assertFalse(validate_end_date(value))

    def test_impossible_dates(self):
        for value in ("2026-02-29", "1900-02-29", "2026-04-31", "2026-13-01", "2026-00-01", "2026-01-00", "0000-01-01"):
            with self.subTest(value=value):
                self.assertFalse(validate_end_date(value))

    def test_extra_characters(self):
        for value in (" 2026-01-01", "2026-01-01 ", "2026-01-01\n", "2026-01-01T12:00:00", "abcd-ef-gh"):
            with self.subTest(value=value):
                self.assertFalse(validate_end_date(value))

    def test_nonstring_inputs(self):
        for value in (None, 20260101, True, date(2026, 1, 1)):
            with self.subTest(value=value):
                self.assertFalse(validate_end_date(value))


if __name__ == "__main__":
    unittest.main(verbosity=2)
