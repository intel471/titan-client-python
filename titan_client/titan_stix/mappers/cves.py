import yaml
from stix2 import Bundle, Vulnerability, ExternalReference, TLP_AMBER

from .common import BaseMapper, StixMapper, generate_id
from .. import author_identity


@StixMapper.register("cves", lambda x: "cveReportsTotalCount" in x)
@StixMapper.register("cve", lambda x: "cve_report" in x.get("data", {}))
class CveMapper(BaseMapper):
    def map(self, source: dict) -> Bundle:
        container = {}
        items = (
            source.get("cveReports") or []
            if "cveReportsTotalCount" in source
            else [source]
        )
        girs_names = self.get_girs_names()
        for item in items:
            uid = item["uid"]
            name = item["data"]["cve_report"]["name"]
            summary = item["data"]["cve_report"]["summary"]
            underground_activity_summary = item["data"]["cve_report"][
                "underground_activity_summary"
            ]
            extras = yaml.dump(
                {
                    k: v
                    for k, v in item["data"]["cve_report"].items()
                    if k
                    in (
                        "vendor_name",
                        "product_name",
                        "patch_status",
                        "interest_level",
                        "activity_location",
                        "exploit_status",
                    )
                }
            )
            girs_paths = item["classification"]["intel_requirements"]
            girs = [{"path": i, "name": girs_names.get(i, i)} for i in girs_paths]
            description = (
                f"{summary}\n\n{underground_activity_summary}\n\n### Properties\n\n```yaml\n{extras}```"
                f"\n\n### Intel requirements\n\n```yaml\n{yaml.dump(girs)}```"
            )
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
            vulnerability = Vulnerability(
                id=generate_id(Vulnerability, name=name.strip().lower()),
                name=name,
                description=description,
                created_by_ref=author_identity,
                external_references=external_references,
                object_marking_refs=[TLP_AMBER],
                custom_properties=custom_properties,
            )
            container[vulnerability.id] = vulnerability
            container[author_identity.id] = author_identity
            container[TLP_AMBER.id] = TLP_AMBER
        if container:
            bundle = Bundle(*container.values(), allow_custom=True)
            return bundle
