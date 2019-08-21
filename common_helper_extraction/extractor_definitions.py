from collections import namedtuple
from common_helper_extraction.padding import get_padding_seperated_sections
from common_helper_extraction.encoded_streams import extract_encoded_streams,\
    SRECORD_REGEX, INTEL_HEX_REGEX, TEKTRONIX_REGEX, TEKTRONIX_EXT_REGEX
from common_helper_extraction.lzma import extract_lzma_streams, HP_LZMA_HEADER


Extractor = namedtuple('Extractor', 'name, extract_function, optional_parameters, file_suffix')


padding_extractor = Extractor('padding seperated sections', get_padding_seperated_sections, [32, b'\xff'], '')
srec_extractor = Extractor('Motorola S-Record', extract_encoded_streams, [SRECORD_REGEX], '.srec')
ihex_extractor = Extractor('Intel Hex', extract_encoded_streams, [INTEL_HEX_REGEX], '.ihex')
tek_extractor = Extractor('Tektronix', extract_encoded_streams, [TEKTRONIX_REGEX], '.tek')
tekx_extractor = Extractor('Tektronix Extended', extract_encoded_streams, [TEKTRONIX_EXT_REGEX], '.tekx')
hp_lzma_extractor = Extractor('LZMA', extract_lzma_streams, [HP_LZMA_HEADER], '.lzma')


EXTRACTOR_LIST = [padding_extractor, srec_extractor, ihex_extractor, tek_extractor, tekx_extractor, hp_lzma_extractor]
