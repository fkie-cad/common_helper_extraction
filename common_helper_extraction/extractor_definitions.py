from collections import namedtuple

from common_helper_extraction.encoded_streams import (
    INTEL_HEX_REGEX, SRECORD_REGEX, TEKTRONIX_EXT_REGEX, TEKTRONIX_REGEX, extract_encoded_streams
)
from common_helper_extraction.fs import extract_sqfs
from common_helper_extraction.lzma import HP_LZMA_HEADER, extract_lzma_streams
from common_helper_extraction.padding import get_padding_seperated_sections

Extractor = namedtuple('Extractor', 'name, extract_function, optional_parameters, file_suffix')


PADDING_EXTRACTOR = Extractor('padding seperated sections', get_padding_seperated_sections, [32, b'\xff'], '')
SREC_EXTRACTOR = Extractor('Motorola S-Record', extract_encoded_streams, [SRECORD_REGEX], '.srec')
IHEX_EXTRACTOR = Extractor('Intel Hex', extract_encoded_streams, [INTEL_HEX_REGEX], '.ihex')
TEK_EXTRECTOR = Extractor('Tektronix', extract_encoded_streams, [TEKTRONIX_REGEX], '.tek')
TEKX_EXTRACTOR = Extractor('Tektronix Extended', extract_encoded_streams, [TEKTRONIX_EXT_REGEX], '.tekx')
HP_LZMA_EXTRACTOR = Extractor('LZMA', extract_lzma_streams, [HP_LZMA_HEADER], '.lzma')
SQFS_EXTRACTOR = Extractor('SQFS', extract_sqfs, [], '.sqfs')


EXTRACTOR_LIST = [PADDING_EXTRACTOR, SREC_EXTRACTOR, IHEX_EXTRACTOR, TEK_EXTRECTOR, TEKX_EXTRACTOR, HP_LZMA_EXTRACTOR]
