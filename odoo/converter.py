#!/usr/bin/python3
# Copyright 2020 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import yaml

HEADER = """-r requirements-find-links.txt

# odoo
-r /odoo/src/requirements.txt
-e /odoo/src
-e /odoo


# patched OCA addons
"""

def add_pr(org, repo, module, pr):
    return (
        f"odoo14-addon-{module} @ git+https://github.com/{org}/"
        f"{repo}@refs/pull/{pr}/head#subdirectory=setup/{module}\n"
    )

with open("requirements.txt.in", "w") as out:
    out.write(HEADER)
    with open("spec.yaml") as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
        for org in data:
            for repo, items in data[org].items():
                org = "oca"
                for key in items:
                    if isinstance(key, int):
                        modules = items[key].split(" ")
                        pr = key
                        for module in modules:
                            out.write(add_pr(org, repo, module, pr))
