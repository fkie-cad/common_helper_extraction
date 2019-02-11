import pytest
from tempfile import TemporaryDirectory
from pathlib import Path

from common_helper_extraction import dump_files


@pytest.mark.parametrize('input_list, suffix, expected_files', [
    ([], '', []),
    ([(0, b'test'), (42, b'test2')], '', ['0x0', '0x2a']),
    ([(0, b'test'), (0, b'same_offset')], '_double', ['0x0_double', '0x0_double-1'])
])
def test_dump(input_list, suffix, expected_files):
    tmp_dir = TemporaryDirectory(prefix='test_')
    dump_files(input_list, tmp_dir.name, suffix)
    for item in expected_files:
        assert Path(tmp_dir.name, item).exists()
