from pathlib import Path

from dry4swift.core import find_duplicates, tokenize_file


def test_normalizes_identifiers_and_numbers(tmp_path: Path) -> None:
    path = tmp_path / ("sample" + '.swift')
    path.write_text('func a(_ x: Int) -> Int { if x > 0 { return x + 1 }; return x }\n', encoding="utf-8")
    values = [token.value for token in tokenize_file(path)]
    assert "ID" in values
    assert "NUM" in values


def test_finds_duplicate_blocks(tmp_path: Path) -> None:
    (tmp_path / ("a" + '.swift')).write_text('func a(_ x: Int) -> Int { if x > 0 { return x + 1 }; return x }\n', encoding="utf-8")
    (tmp_path / ("b" + '.swift')).write_text('func b(_ y: Int) -> Int { if y > 0 { return y + 2 }; return y }\n', encoding="utf-8")
    duplicates = find_duplicates(tmp_path, min_tokens=8)
    assert duplicates
    assert len(duplicates[0].locations) >= 2
