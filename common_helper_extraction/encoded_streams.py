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
import re

SRECORD_REGEX = b'S[0-3][0-9A-Fa-f]+[\x0d\x0a]+(S[1-6][0-9A-Fa-f]+[\x0d\x0a]+)+S[7-9][0-9A-Fa-f]+'
INTEL_HEX_REGEX = b'(:[0-9A-Fa-f]{10,}[\x0d\x0a]+)+:00000001FF'
TEKTRONIX_REGEX = b'(/[0-9A-Za-z]+[\x0d\x0a]+)+/00000000'
TEKTRONIX_EXT_REGEX = b'(%[0-9-A-Za-z]+[\x0d\x0a]+)+(%[0-9A-Za-z]{6}.sec[0-9A-Za-z]+[\x0d\x0a]+)*%[0-9A-Za-z]{2}8[0-9A-Za-z]{4,}'
ASCII85_ADOBE_REGEX = b'<~([!-u]*[\x0d\x0a]*)+~>'


def extract_encoded_streams(input_data: bytes, stream_regex: bytes) -> list:
    stream_signature = re.compile(stream_regex)
    stream_list = [
        (match.start(), match.group())
        for match in stream_signature.finditer(input_data)
    ]
    return stream_list
