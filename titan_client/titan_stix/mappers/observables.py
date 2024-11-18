import re
from dataclasses import dataclass
from typing import Union, Callable

from stix2 import URL, IPv4Address, DomainName, File, AutonomousSystem, UserAccount, IPv6Address, EmailAddress
from pycti import CustomObservableCryptocurrencyWallet

from titan_client.titan_stix import author_identity
from titan_client.titan_stix.constants import X_OPENCT_CREATED_BY, MARKING


@dataclass(frozen=True)
class MapperConfig:
    mapper: Callable
    src_types: tuple
    value_extractor: Union[Callable, None] = None


class ObservableMapper:

    def __init__(self):
        self.mapper_configs = [
            MapperConfig(self.map_url, ("MaliciousURL", "ActorOtherWebsite", "URL")),
            MapperConfig(self.map_domain, ("MaliciousDomain", "ActorDomain")),
            MapperConfig(self.map_ipv4, ("IPAddress", "IPv4Prefix")),
            MapperConfig(self.map_ipv6, ("IPv6Prefix", )),
            MapperConfig(self.map_email_address, ("EmailAddress", )),
            MapperConfig(self.map_autonomous_system, ("AutonomousSystem",)),
            MapperConfig(self.map_file_hash, ("MD5", "SHA1", "SHA256",)),
            MapperConfig(self.map_filename, ("FileName",)),
            MapperConfig(self.map_crypto_wallet, ("BitcoinAddress", "OtherCryptoCurrencies")),
            MapperConfig(self.map_user_account, (
                "AIM", "Discord", "Facebook", "GitHub", "ICQ", "Instagram", "Jabber", "LinkedIn", "MSN", "MoiMir",
                "Odnoklassniki", "QQ", "Skype", "Telegram", "TOX", "Tox", "Twitter", "VK", "WeChat", "Wickr", "YahooIM",
                "PerfectMoneyID", "QiwiWallet", "WebMoneyID", "WebMoneyPurse", "YandexMoney", "Phone"),
                         lambda x: re.sub(r"^.*/", "", x.strip("/"))),
        ]

    def map_many(self, *observable_sources: dict):
        for observable_source in observable_sources:
            yield self.map(observable_source["type"], observable_source["value"])

    def map(self, type: str, value: str):  # noqa need `type` here as it comes from the API
        for mapper_config in self.mapper_configs:
            if type in mapper_config.src_types:
                if value_extractor := mapper_config.value_extractor:
                    value = value_extractor(value)
                return mapper_config.mapper(value, type=type)


    @staticmethod
    def map_url(value: str, *args, **kwargs) -> URL:
        return URL(
            value=value,
            object_marking_refs=[MARKING],
            custom_properties={X_OPENCT_CREATED_BY: author_identity}
        )

    @staticmethod
    def map_ipv4(value: str, *args, **kwargs) -> IPv4Address:
        return IPv4Address(
            value=value,
            object_marking_refs=[MARKING],
            custom_properties={X_OPENCT_CREATED_BY: author_identity}
        )

    @staticmethod
    def map_ipv6(value: str, *args, **kwargs) -> IPv6Address:
        return IPv6Address(
            value=value,
            object_marking_refs=[MARKING],
            custom_properties={X_OPENCT_CREATED_BY: author_identity}
        )

    @staticmethod
    def map_domain(value: str, *args, **kwargs) -> DomainName:
        return DomainName(
            value=value,
            object_marking_refs=[MARKING],
            custom_properties={X_OPENCT_CREATED_BY: author_identity}
        )

    @staticmethod
    def map_email_address(value: str, *args, **kwargs) -> EmailAddress:
        return EmailAddress(
            value=value,
            object_marking_refs=[MARKING],
            custom_properties={X_OPENCT_CREATED_BY: author_identity}
        )

    @staticmethod
    def map_autonomous_system(value: str, *args, **kwargs) -> AutonomousSystem:
        return AutonomousSystem(
            number=int(re.sub(r"[A-Z]", "", value)),
            object_marking_refs=[MARKING],
            custom_properties={X_OPENCT_CREATED_BY: author_identity}
        )

    @staticmethod
    def map_crypto_wallet(value: str, *args, **kwargs) -> CustomObservableCryptocurrencyWallet:
        return CustomObservableCryptocurrencyWallet(
            value=value,
            object_marking_refs=[MARKING],
            custom_properties={X_OPENCT_CREATED_BY: author_identity}
        )

    @staticmethod
    def map_user_account(value: str, type: str, *args, **kwargs) -> UserAccount:
        return UserAccount(
            account_type = type,
            user_id = value,
            object_marking_refs=[MARKING],
            custom_properties={X_OPENCT_CREATED_BY: author_identity}
    )

    def map_file_hash(self, value: str, type: str) -> File:
        kwargs = {type.lower(): value}
        return self.map_file(**kwargs)

    def map_filename(self, value: str, *args, **kwargs) -> File:
        return self.map_file(name=value)

    @staticmethod
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
            "custom_properties": {X_OPENCT_CREATED_BY: author_identity}
        }
        if hashes:
            file_kwargs["hashes"] = hashes
        if name:
            file_kwargs["name"] = name

        return File(**file_kwargs)
