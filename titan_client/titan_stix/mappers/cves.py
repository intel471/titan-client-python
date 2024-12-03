import yaml
from stix2 import Bundle, Vulnerability, ExternalReference, Software, Relationship

from .common import BaseMapper, StixMapper
from .. import author_identity, generate_id, StixObjects
from ..constants import MARKING


@StixMapper.register("cves", lambda x: "cveReportsTotalCount" in x)
@StixMapper.register("cve", lambda x: "cve_report" in x.get("data", {}))
class CveMapper(BaseMapper):
    def map(self, source: dict) -> Bundle:
        container = StixObjects()
        items = (
            source.get("cveReports") or []
            if "cveReportsTotalCount" in source
            else [source]
        )
        for item in items:
            uid = item["uid"]
            name = item["data"]["cve_report"]["name"]
            summary = item["data"]["cve_report"]["summary"]
            underground_activity_summary = item["data"]["cve_report"][
                "underground_activity_summary"
            ]
            counter_measures = item["data"]["cve_report"]["counter_measures"]
            extras = yaml.dump(
                {
                    k: v
                    for k, v in item["data"]["cve_report"].items()
                    if k
                    in (
                        "patch_status",
                        "interest_level",
                        "activity_location",
                        "exploit_status",
                    )
                }
            )
            description = f"{summary}\n\n{underground_activity_summary}\n\n{counter_measures}\n\n### Properties\n\n```yaml\n{extras}```"
            cvss3_score = (item["data"]["cve_report"].get("cvss_score") or {}).get("v3")
            external_references = []
            for link_type, key in (
                ("Titan URL", "titan_links"),
                ("PoC", "poc_links"),
                ("Patch", "patch_links"),
            ):
                for link in item["data"]["cve_report"].get(key) or []:
                    external_reference = ExternalReference(
                        source_name=f"[{link_type}] {link['title']}", url=link["url"]
                    )
                    external_references.append(external_reference)

            custom_properties = {"x_intel471_com_uid": uid}
            if cvss3_score:
                custom_properties["x_opencti_base_score"] = cvss3_score
            labels = self.get_girs_labels((item.get("classification") or {}).get("intel_requirements") or [])
            vulnerability = Vulnerability(
                id=generate_id(Vulnerability, name=name.strip().lower()),
                name=name,
                description=description,
                created_by_ref=author_identity,
                external_references=external_references,
                object_marking_refs=[MARKING],
                custom_properties=custom_properties,
                labels=labels
            )
            software = Software(
                name=item["data"]["cve_report"]["product_name"],
                vendor=item["data"]["cve_report"]["vendor_name"])
            rel = Relationship(software, "has", vulnerability, created_by_ref=author_identity)
            container.extend([vulnerability, software, rel, author_identity, MARKING])
        if container:
            bundle = Bundle(*container.get(), allow_custom=True)
            return bundle
