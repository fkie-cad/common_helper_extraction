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

from struct import unpack


def get_data_size(input_data: bytes, offset: int, byteorder: str = None) -> int:
    if not byteorder:
        byteorder = get_endianness(input_data[offset:offset + 4], 'I', len(input_data))
    return unpack('{}I'.format(byteorder), input_data[offset:offset + 4])[0]


def get_endianness(size_field_buffer: bytes, size_field_type: str, file_size: int) -> str:
    if unpack('<{}'.format(size_field_type), size_field_buffer)[0] < file_size:
        return '<'
    return '>'
