from pathlib import Path

from common_helper_files import get_binary_from_file


def get_binary_from_test_file(file_name: str) -> bytes:
    return get_binary_from_file(_get_test_file(file_name))


def _get_test_file(file_name: str) -> Path:
    test_dir = Path(Path(__file__).parent, 'data')
    return Path(test_dir, file_name)
