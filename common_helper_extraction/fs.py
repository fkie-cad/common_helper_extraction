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
from .jffs import extract_jffs
from .sqfs import extract_sqfs
from .ubifs import extract_ubifs
from .yaffs import extract_yaffs

FS_EXTRACTORS = [extract_sqfs, extract_yaffs, extract_ubifs, extract_jffs]


def extract_fs(input_data: bytes) -> list:
    fs_sections = list()
    for extractor in FS_EXTRACTORS:
        output = extractor(input_data)
        fs_sections.extend(output)
    return fs_sections
