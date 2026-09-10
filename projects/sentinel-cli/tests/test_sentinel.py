"""
Tests for SentinelCLI's FileInspector class. Run with: pytest
These write small, temporary sample files, run FileInspector against
them, and check the printed output — proving the behavior we've been
verifying by hand all along.
"""

import json
import pytest
from sentinel import FileInspector


def test_csv_normal_case(tmp_path, capsys):
    csv_file = tmp_path / "data.csv"
    csv_file.write_text("name,age\nAlice,29\nBob,34\n")

    FileInspector(str(csv_file)).analyze()
    output = capsys.readouterr().out

    assert "File type: CSV" in output
    assert "Rows: 2" in output
    assert "Columns: 2" in output


def test_csv_mismatched_row_is_flagged(tmp_path, capsys):
    csv_file = tmp_path / "bad.csv"
    csv_file.write_text("name,age,country\nAlice,29,Kenya\nBob,34\n")

    FileInspector(str(csv_file)).analyze()
    output = capsys.readouterr().out

    assert "Warning" in output
    assert "different column count" in output


def test_json_list_normal_case(tmp_path, capsys):
    json_file = tmp_path / "data.json"
    json_file.write_text(json.dumps([{"user": "alice"}, {"user": "bob"}]))

    FileInspector(str(json_file)).analyze()
    output = capsys.readouterr().out

    assert "JSON (list)" in output
    assert "Total items: 2" in output


def test_json_malformed_is_caught_not_crashed(tmp_path, capsys):
    json_file = tmp_path / "broken.json"
    json_file.write_text('[{"user": "alice"')  # deliberately broken

    FileInspector(str(json_file)).analyze()
    output = capsys.readouterr().out

    assert "broken and could not be read" in output


def test_text_flags_suspicious_words(tmp_path, capsys):
    log_file = tmp_path / "log.txt"
    log_file.write_text("login ok\nerror: timeout\nfile saved\n")

    FileInspector(str(log_file)).analyze()
    output = capsys.readouterr().out

    assert "Suspicious lines found: 1" in output


def test_empty_file_handled_gracefully(tmp_path, capsys):
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("")

    FileInspector(str(empty_file)).analyze()
    output = capsys.readouterr().out

    assert "empty" in output.lower()


def test_missing_file_handled_gracefully(capsys):
    FileInspector("this_file_does_not_exist.csv").analyze()
    output = capsys.readouterr().out

    assert "File not found" in output


def test_unrecognized_extension_handled_gracefully(tmp_path, capsys):
    weird_file = tmp_path / "no_ext"
    weird_file.write_text("something")

    FileInspector(str(weird_file)).analyze()
    output = capsys.readouterr().out

    assert "Unrecognized" in output