import pathlib
import logging
from ctypes import cdll, c_char_p, c_uint


log = logging.getLogger(__name__)


file_dir_path = pathlib.Path(__file__).parent
file_path = str(file_dir_path / "icrc32.so")

try:
    lib = cdll.LoadLibrary(str(file_path))
    lib.icrc32.restype = c_uint
except Exception as error:
    import zlib as lib
    lib.icrc32 = lambda x, y, z: lib.crc32(y, x)
    log.warning(error)


def calculate_icrc32(s: bytes | str) -> int:
    if isinstance(s, str):
        s = s.encode(encoding="utf8")
    return lib.icrc32(c_uint(0), c_char_p(s), c_uint(len(s)))
