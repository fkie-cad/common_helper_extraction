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
from common_helper_files import write_binary_to_file
from pathlib import Path


def dump_files(data: list, destination_directory: str, suffix: str='') -> None:
    for offset, content in data:
        output_path = Path(destination_directory, '{offset:#x}{suffix}'.format(offset=offset, suffix=suffix))
        write_binary_to_file(content, str(output_path), overwrite=False, file_copy=True)
