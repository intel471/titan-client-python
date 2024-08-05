def _wrap(*components):
    return "[" + " OR ".join([f"{i} = {j}" for i, j in components]) + "]"


def create_url_pattern(value: str) -> str:
    return _wrap(("url:value", f"'{value}'"))


def create_ipv4_pattern(value: str) -> str:
    return _wrap(("ipv4-addr:value", f"'{value}'"))


def create_domain_pattern(value: str) -> str:
    return _wrap(("domain-name:value", f"'{value}'"))


def create_file_pattern(md5: str = None, sha1: str = None, sha256: str = None) -> str:
    hashes = []
    if md5:
        hashes.append(("file:hashes.md5", f"'{md5}'"))
    if sha1:
        hashes.append(("file:hashes.sha1", f"'{sha1}'"))
    if sha256:
        hashes.append(("file:hashes.sha256", f"'{sha256}'"))
    return _wrap(*hashes)
