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
from common_helper_extraction.fs import _get_endianness
from struct import calcsize, unpack


class Yaffs:
    def __init__(self):
        self._input_data = None
        self._number_of_objects = 0
        self._endianess = None
        self._offset = None

    def get_fs_offset(self, input_data: bytes) -> int:
        self._offset = self._get_first_header(input_data)
        if self._offset == -1:
            return -1
        self._input_data = input_data[self._offset:]
        return self._offset

    def extract_fs(self):
        fs_sections = list()
        index = 0
        while index < len(self._input_data):
            chunk = self._input_data[index:]
            if self._get_object_type(chunk) == 1:
                if self._confirm_data(chunk, self._get_object_id(chunk), self._get_data_size(chunk)):
                    print(index)
                    index += 4224
            else:
                index += 2112
        print(index)
        fs_sections.append([self._offset, self._input_data[:index]])
        return fs_sections

    def _confirm_data(self, chunk: bytes, object_id: int, data_size: int) -> bool:
        if chunk[4169] == object_id and \
                unpack('{}{}'.format(self._endianess, 'I'), chunk[4174:4178])[0] == data_size:
            return True
        return False

    def _get_first_header(self, input_data) -> int:
        index = 0
        while not self._is_yaffs_header(input_data[index:]):
            index += 1
            if index > len(input_data) - 2048:
                return -1
        return index

    def _is_yaffs_header(self, input_data=None) -> bool:
        if input_data is None:
            input_data = self._input_data
        if (input_data[8:10] == b'\xff\xff') and \
                (input_data[265:268] == b'\xff\xff\xff') and \
                (input_data[2060:2064] == b'\x00\x00\x00\x00'):
            self._endianess = _get_endianness(input_data[0:4], 'I', len(input_data))
            return True
        return False

    def _get_object_type(self, chunk: bytes) -> int:
        return unpack('{}{}'.format(self._endianess, 'I'), chunk[0:4])[0]

    def _get_object_id(self, chunk: bytes) -> int:
        return chunk[2057]

    def _get_data_size(self, chunk: bytes) -> int:
        return unpack('{}{}'.format(self._endianess, 'I'), chunk[292:296])[0]
