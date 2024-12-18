import re

from pycti import CustomObservableCryptocurrencyWallet
from stix2 import URL, IPv4Address, DomainName, File, AutonomousSystem, UserAccount, IPv6Address, EmailAddress
from stix2.exceptions import InvalidValueError

from titan_client.titan_stix import author_identity
from titan_client.titan_stix.constants import MARKING, X_OPENCT_CREATED_BY


def map_url(value: str, *args, **kwargs) -> URL:
    return URL(
        value=value,
        object_marking_refs=[MARKING],
        custom_properties={X_OPENCT_CREATED_BY: author_identity.id}
    )


def map_ipv4(value: str, *args, **kwargs) -> IPv4Address:
    return IPv4Address(
        value=value,
        object_marking_refs=[MARKING],
        custom_properties={X_OPENCT_CREATED_BY: author_identity.id}
    )


def map_ipv6(value: str, *args, **kwargs) -> IPv6Address:
    return IPv6Address(
        value=value,
        object_marking_refs=[MARKING],
        custom_properties={X_OPENCT_CREATED_BY: author_identity.id}
    )


def map_domain(value: str, *args, **kwargs) -> DomainName:
    if value.startswith("http"):
        raise InvalidValueError(DomainName, "value", f"'{value}' is not valid domain name")
    return DomainName(
        value=value,
        object_marking_refs=[MARKING],
        custom_properties={X_OPENCT_CREATED_BY: author_identity.id}
    )


def map_email_address(value: str, *args, **kwargs) -> EmailAddress:
    return EmailAddress(
        value=value,
        object_marking_refs=[MARKING],
        custom_properties={X_OPENCT_CREATED_BY: author_identity.id}
    )


def map_autonomous_system(value: str, *args, **kwargs) -> AutonomousSystem:
    return AutonomousSystem(
        number=int(re.sub(r"[A-Z]", "", value)),
        object_marking_refs=[MARKING],
        custom_properties={X_OPENCT_CREATED_BY: author_identity.id}
    )


def map_crypto_wallet(value: str, *args, **kwargs) -> CustomObservableCryptocurrencyWallet:
    return CustomObservableCryptocurrencyWallet(
        value=value,
        object_marking_refs=[MARKING],
        custom_properties={X_OPENCT_CREATED_BY: author_identity.id}
    )


def map_user_account(value: str, type: str, *args, **kwargs) -> UserAccount:
    return UserAccount(
        account_type=type,
        user_id=value,
        object_marking_refs=[MARKING],
        custom_properties={X_OPENCT_CREATED_BY: author_identity.id}
    )


def map_file(md5: str = None, sha1: str = None, sha256: str = None, name: str = None) -> File:
    hashes = {}
    if md5:
        hashes["MD5"] = md5
    if sha1:
        hashes["SHA-1"] = sha1
    if sha256:
        hashes["SHA-256"] = sha256

    file_kwargs = {
        "object_marking_refs": [MARKING],
        "custom_properties": {X_OPENCT_CREATED_BY: author_identity.id}
    }
    if hashes:
        file_kwargs["hashes"] = hashes
    if name:
        file_kwargs["name"] = name

    return File(**file_kwargs)


def map_file_hash(value: str, type: str) -> File:
    kwargs = {type.lower(): value}
    return map_file(**kwargs)


def map_filename(value: str, *args, **kwargs) -> File:
    return map_file(name=value)
