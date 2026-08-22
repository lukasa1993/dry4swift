from pathlib import Path

from dry4swift.core import find_duplicates


def test_cross_file_duplicate_is_found(tmp_path: Path) -> None:
    first = tmp_path / ("a_" + 'sample.swift')
    second = tmp_path / ("b_" + 'sample.swift')
    first.write_text('struct Choice {\n  func choose(_ a: Bool, _ b: Bool) -> Int {\n    if a && b { return 1 }\n    return 0\n  }\n}\n', encoding="utf-8")
    second.write_text('struct Selection {\n  func decide(_ a: Bool, _ b: Bool) -> Int {\n    if a && b { return 1 }\n    return 0\n  }\n}\n', encoding="utf-8")
    duplicates = find_duplicates(tmp_path, min_tokens=8)
    assert duplicates


def test_non_overlapping_same_file_duplicate_is_found(tmp_path: Path) -> None:
    path = tmp_path / 'sample.swift'
    path.write_text('struct Choice {\n  func choose(_ a: Bool, _ b: Bool) -> Int {\n    if a && b { return 1 }\n    return 0\n  }\n}\n' + "\n" + 'struct Selection {\n  func decide(_ a: Bool, _ b: Bool) -> Int {\n    if a && b { return 1 }\n    return 0\n  }\n}\n', encoding="utf-8")
    duplicates = find_duplicates(tmp_path, min_tokens=8)
    assert any(item.locations[0].file == item.locations[1].file for item in duplicates)
