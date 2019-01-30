'''
    common_helper_extraction
    Copyright (C) 2018-2019  Fraunhofer FKIE

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import logging
from lzma import decompress, LZMAError


LZMA_HEADER = b'\x39\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff'


def extract_lzma_streams(input_data: bytes) -> list:
    lzma_streams = list()
    stream_offset = _find_next_stream(input_data, 0)
    while stream_offset < len(input_data):
        old_stream_offset = stream_offset
        stream_offset = _find_next_stream(input_data, old_stream_offset + 1)
        lzma_streams.append((old_stream_offset, input_data[old_stream_offset:stream_offset]))
    return lzma_streams


def get_decompressed_lzma_streams(compressed_streams: list) -> list:
    decompressed_streams = list()
    for stream in compressed_streams:
        decompressed_streams.append((stream[0], _decompress_lzma_stream(stream[1])))
    return decompressed_streams


def _decompress_lzma_stream(compressed_stream: bytes) -> bytes:
    try:
        return decompress(compressed_stream)
    except LZMAError as e:
        logging.error('lzma decompression failed: {}'.format(e))
        return b''


def _find_next_stream(input_data: bytes, offset: int) -> int:
    try:
        return input_data.index(LZMA_HEADER, offset, len(input_data))
    except ValueError:
        logging.debug('no lzma stream found')
        return len(input_data)
