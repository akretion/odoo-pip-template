from configparser import ConfigParser

from setuptools import setup

cfg = ConfigParser()
cfg.read("project.cfg")


setup(
    version=cfg.get("odoo", "series") + "." + cfg.get("odoo", "version"),
    name=f"odoo-addons-{cfg.get('odoo', 'trigram')}",
    description="Custom Odoo Addons",
    setup_requires=["setuptools-odoo"],
    install_requires=[
        'click-odoo-contrib>=1.4.1',
    ],
    odoo_addons=True,
)
