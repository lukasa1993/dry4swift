# dry4swift

`dry4swift` finds normalized duplicate Swift code with a Tree-sitter Swift syntax tree. It reports maximal non-overlapping blocks, including duplicates in one source file.

```bash
pipx install git+https://github.com/lukasa1993/dry4swift.git
dry4swift --min-tokens 30 --fail
```

Exit status: `0` pass, `1` parser or execution error, `2` duplicate groups found with `--fail`.
