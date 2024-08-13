from stix2 import URL, TLP_AMBER, IPv4Address, File, DomainName


def create_url(author: str, value: str) -> URL:
    return URL(
        value=value,
        object_marking_refs=[TLP_AMBER],
        custom_properties={"x_opencti_created_by_ref": author}
    )


def create_ipv4(value: str, author: str) -> IPv4Address:
    return IPv4Address(
        value=value,
        object_marking_refs=[TLP_AMBER],
        custom_properties={"x_opencti_created_by_ref": author}
    )


def create_domain(author: str, value: str) -> DomainName:
    return DomainName(
        value=value,
        object_marking_refs=[TLP_AMBER],
        custom_properties={"x_opencti_created_by_ref": author}
    )


def create_file(author: str, md5: str = None, sha1: str = None, sha256: str = None) -> File:
    hashes = {}
    if md5:
        hashes["md5"] = md5
    if sha1:
        hashes["sha1"] = sha1
    if sha256:
        hashes["sha256"] = sha256
    return File(
        hashes=hashes,
        object_marking_refs=[TLP_AMBER],
        custom_properties={"x_opencti_created_by_ref": author}
    )
