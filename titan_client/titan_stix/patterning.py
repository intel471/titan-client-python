import urllib
from stix2patterns.validator import run_validator


def _wrap(*components):
    return "[" + " OR ".join([f"{i} = {j}" for i, j in components]) + "]"


def create_url_pattern(value: str) -> str:
    pattern = _wrap(("url:value", f"'{value}'"))
    if run_validator(pattern):
        value = urllib.parse.quote(value, safe=":/?&=,")
        pattern = _wrap(("url:value", f"'{value}'"))
    return pattern


def create_ipv4_pattern(value: str) -> str:
    return _wrap(("ipv4-addr:value", f"'{value}'"))


def create_domain_pattern(value: str) -> str:
    return _wrap(("domain-name:value", f"'{value}'"))


def create_file_pattern(md5: str = None, sha1: str = None, sha256: str = None) -> str:
    """
    Using format `file:hashes.md5`, `file:hashes.sha1`, etc.
    instead of   `file:hashes.MD5`, `file:hashes.'SHA-1'`, etc.
    to be compliant with OpenCTI ID generator, which is using the former one.
    """
    hashes = []
    if md5:
        hashes.append(("file:hashes.md5", f"'{md5}'"))
    if sha1:
        hashes.append(("file:hashes.sha1", f"'{sha1}'"))
    if sha256:
        hashes.append(("file:hashes.sha256", f"'{sha256}'"))
    return _wrap(*hashes)
