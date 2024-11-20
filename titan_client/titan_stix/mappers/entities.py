import re
from dataclasses import dataclass
from typing import Union, Callable

from titan_client.titan_stix.sco import map_url, map_domain, map_ipv4, map_ipv6, map_email_address, \
    map_autonomous_system, map_file_hash, map_filename, map_crypto_wallet, map_user_account
from titan_client.titan_stix.sdo import map_malware, map_threat_actor


@dataclass(frozen=True)
class MapperConfig:
    mapper: Callable
    src_types: tuple
    value_extractor: Union[Callable, None] = None


class EntitiesMapper:
    """
    Map entities attached to the reports under `.entities` key and entities
    present in `/entities` and `/iocs` endpoints.
    """
    def __init__(self):
        self.mapper_configs = [
            MapperConfig(map_url, ("MaliciousURL", "ActorOtherWebsite", "URL")),
            MapperConfig(map_domain, ("MaliciousDomain", "ActorDomain")),
            MapperConfig(map_ipv4, ("IPAddress", "IPv4Prefix")),
            MapperConfig(map_ipv6, ("IPv6Prefix", )),
            MapperConfig(map_email_address, ("EmailAddress", )),
            MapperConfig(map_autonomous_system, ("AutonomousSystem",)),
            MapperConfig(map_file_hash, ("MD5", "SHA1", "SHA256",)),
            MapperConfig(map_filename, ("FileName",)),
            MapperConfig(map_crypto_wallet, ("BitcoinAddress", "OtherCryptoCurrencies")),
            MapperConfig(map_threat_actor, ("Handle",)),
            MapperConfig(map_malware, ("MalwareFamily",)),
            MapperConfig(map_user_account, (
                "AIM", "Discord", "Facebook", "GitHub", "ICQ", "Instagram", "Jabber", "LinkedIn", "MSN", "MoiMir",
                "Odnoklassniki", "QQ", "Skype", "Telegram", "TOX", "Tox", "Twitter", "VK", "WeChat", "Wickr", "YahooIM",
                "PerfectMoneyID", "QiwiWallet", "WebMoneyID", "WebMoneyPurse", "YandexMoney", "Phone"),
                         lambda x: re.sub(r"^.*/", "", x.strip("/"))),
        ]

    def map_many(self, *observable_sources: dict):
        for observable_source in observable_sources:
            yield self.map(observable_source["type"], observable_source["value"])

    def map(self, type: str, value: str, *args, **kwargs):  # noqa need `type` here as it comes from the API
        for mapper_config in self.mapper_configs:
            if type in mapper_config.src_types:
                if value_extractor := mapper_config.value_extractor:
                    value = value_extractor(value)
                return mapper_config.mapper(value, type=type)
