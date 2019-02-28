# common_helper_extraction

[![Build Status](https://travis-ci.org/fkie-cad/common_helper_extraction.svg?branch=master)](https://travis-ci.org/fkie-cad/common_helper_extraction)
[![codecov](https://codecov.io/gh/fkie-cad/common_helper_extraction/branch/master/graph/badge.svg)](https://codecov.io/gh/fkie-cad/common_helper_extraction)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f50240ca6aff4537a00f929aa6a71396)](https://www.codacy.com/app/weidenba/common_helper_extraction?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fkie-cad/common_helper_extraction&amp;utm_campaign=Badge_Grade)

Extraction support functions

## Function Overview

### dump_files

Uses the result list of one of the other functions and dumps the files to `destination_directory`.
File names are `OFFSET[suffix]`.  

`def dump_files(data: list, destination_directory: str, suffix: str='') -> None:`

### cut_at_padding

Cuts a BLOB `input_data` at paddings of `padding_pattern` with a minimal length of `padding_min_length`.

`cut_at_padding(input_data: bytes, padding_min_length: int=4, padding_pattern: bytes=b'\x00') -> list:`

The result is a list of OFFSET, DATA tuples.

```python
[ (OFFSET_1, DATA_1), ... ]
```

### extract_lzma_streams

Extracts LZMA streams out of a BLOB `input_data`.

`extract_lzma_streams(input_data: bytes) -> list`

The result is a list of OFFSET, DATA tuples.

```python
[ (OFFSET_1, DATA_1), ... ]
```

### get_decompressed_lzma_streams

Decompresses LZMA streams that may be the result of `extract_lzma_streams`.

`get_decompressed_lzma_streams(compressed_streams: list) -> list:`

The result is a list of OFFSET, DATA tuples.

```python
[ (OFFSET_1, DATA_1), ... ]
```
