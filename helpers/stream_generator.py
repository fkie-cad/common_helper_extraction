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
from lzma import LZMACompressor, FORMAT_ALONE, FILTER_LZMA1


def generate_lzma_stream(data, dict_size=33554432, lc=3, lp=1, pb=1):
    lzma_filters = [
        {'id': FILTER_LZMA1, 'dict_size': dict_size, 'lc': lc, 'lp': lp, 'pb': pb}
    ]
    compressor = LZMACompressor(format=FORMAT_ALONE, filters=lzma_filters)
    lzma_stream = []
    lzma_stream.append(compressor.compress(data))
    lzma_stream.append(compressor.flush())
    return b''.join(lzma_stream)
