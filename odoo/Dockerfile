FROM quay.io/acsone/odoo-bedrock:14.0-py36-latest as dist

RUN set -e \
  && apt update \
  && apt -y install python3-dev python3.6-dev libxml2-dev libxslt1-dev libldap2-dev \
    libsasl2-dev libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev \
    liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev libxcb1-dev libpq-dev \
  && apt -y install --no-install-recommends postgresql-client wget unzip git \
  && apt -y clean \
  && rm -rf /var/lib/apt/lists/*


# use this COPY for a regular docker build, otherwise use
# buildah bud --volume ${PWD}/release:/tmp/release
# or
# podmain build --volume ${PWD}/release:/tmp/release

COPY extra-bin/download-odoo /odoo/bin/download-odoo
COPY extra-bin/freeze /odoo/bin/freeze

FROM dist as dev
ENV PATH=/odoo/extra-bin:$PATH
#RUN pip install --no-deps -r /odoo/app/debug_requirements.txt

FROM dev as prod

RUN download-odoo

COPY requirements.txt /odoo/requirements.txt
COPY project.cfg /odoo/project.cfg
COPY setup.py /odoo/setup.py

COPY start-entrypoint.d /odoo/start-entrypoint.d


COPY odoo /odoo/odoo
COPY script /odoo/script
COPY requirements-find-links.txt /odoo/requirements-find-links.txt

RUN pip install -U pip --upgrade
RUN pip install --no-deps -r /odoo/requirements.txt

