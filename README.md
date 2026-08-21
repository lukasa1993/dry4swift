# dry4swift

`dry4swift` finds duplicated normalized token blocks in Swift source files.

## Install

```bash
pipx install git+https://github.com/lukasa1993/dry4swift.git
```

## Run

```bash
dry4swift --min-tokens 30 --fail
```

Identifiers and numeric literals are normalized. Comments and string contents do not affect matching. Use positional path fragments to limit the scan. Use `--json` for machine-readable output.

Exit status `2` means that duplication was found while `--fail` was active.

## Development

```bash
python -m pip install -e . pytest
pytest -q
```
