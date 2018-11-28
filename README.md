# common_helper_extraction
Extraction support functions

## Function Overview

### cut_at_padding

Cuts a Binary BLOB `input_data` at paddings of `padding_pattern` with a minimal length of `padding_min_length`.

`cut_at_padding(input_data, padding_min_length=4, padding_pattern=b'\x00')`

The result is a list of OFFSET, DATA tuples.

```python
[ (OFFSET_1, DATA_1), ... ]
```
