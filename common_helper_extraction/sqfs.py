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

from .helper_fs import get_fs_sections_with_magic

SQFS_MAGIC_STRINGS = [b'sqsh', b'qshs', b'shsq', b'hsqs']
SQFS_SIZE_BUFFER_OFFSET = 0x28
SQFS_SIZE_BUFFER_TYPE = 'Q'


def extract_sqfs(input_data: bytes) -> list:
    fs_sections = list()
    for fs_magic in SQFS_MAGIC_STRINGS:
        fs_sections.extend(get_fs_sections_with_magic(input_data, fs_magic, SQFS_SIZE_BUFFER_OFFSET, SQFS_SIZE_BUFFER_TYPE))
    return fs_sections
