# common_helper_extraction

[![Build Status](https://travis-ci.org/fkie-cad/common_helper_extraction.svg?branch=master)](https://travis-ci.org/fkie-cad/common_helper_extraction)
[![codecov](https://codecov.io/gh/fkie-cad/common_helper_extraction/branch/master/graph/badge.svg)](https://codecov.io/gh/fkie-cad/common_helper_extraction)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f50240ca6aff4537a00f929aa6a71396)](https://www.codacy.com/app/weidenba/common_helper_extraction?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fkie-cad/common_helper_extraction&amp;utm_campaign=Badge_Grade)

Extraction support functions

## Function Overview

### cut_at_padding

Cuts a BLOB `input_data` at paddings of `padding_pattern` with a minimal length of `padding_min_length`.

`cut_at_padding(input_data, padding_min_length=4, padding_pattern=b'\x00')`

The result is a list of OFFSET, DATA tuples.

```python
[ (OFFSET_1, DATA_1), ... ]
```

### extract_lzma_streams

Extracts LZMA streams out of a BLOB `input_data`.

`extract_lzma_streams(input_data)`

The result is a list of OFFSET, DATA tuples.

```python
[ (OFFSET_1, DATA_1), ... ]
```
