# color-log

Level-aware coloured output for the standard logging module.

## Why

I kept rewriting the same thirty lines in every project, so I pulled them out.

## Install

```bash
pip install color-log
```

## Usage

```python
from color_log import colorLog

result = colorLog("example")
print(result)
```

## Notes

- No runtime dependencies outside the standard library.
- Tested on Python 3.9 and newer.

## License

MIT
