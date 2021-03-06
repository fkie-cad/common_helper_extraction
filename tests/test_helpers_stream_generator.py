from helpers.stream_generator import generate_lzma_stream


def test_generate_lzma_stream():
    test_data = b'this is a testcase'
    result = generate_lzma_stream(test_data)
    assert result == b'\x39\x00\x00\x00\x02\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x3A\x1A\x09\x90\xDC\x43\xD7\x91\x68\xB9\x26\xD0\x03\x11\xA6\xA1\x08\xBB\xCC\x11\xEA\xFF\xFC\x4D\x40\x00'
