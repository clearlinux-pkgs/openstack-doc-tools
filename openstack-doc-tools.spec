#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openstack-doc-tools
Version  : 0.30.0
Release  : 18
URL      : http://tarballs.openstack.org/openstack-doc-tools/openstack-doc-tools-0.30.0.tar.gz
Source0  : http://tarballs.openstack.org/openstack-doc-tools/openstack-doc-tools-0.30.0.tar.gz
Summary  : Tools for OpenStack Documentation
Group    : Development/Tools
License  : Apache-2.0
Requires: openstack-doc-tools-bin
Requires: openstack-doc-tools-python
Requires: openstack-doc-tools-data
BuildRequires : Babel-python
BuildRequires : Jinja2-python
BuildRequires : PyYAML-python
BuildRequires : Pygments-python
BuildRequires : Sphinx-python
BuildRequires : astroid-python
BuildRequires : bashate-python
BuildRequires : chardet-python
BuildRequires : demjson-python
BuildRequires : doc8-python
BuildRequires : docutils-python
BuildRequires : flake8-python
BuildRequires : hacking-python
BuildRequires : iso8601-python
BuildRequires : logilab-common-python
BuildRequires : lxml-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : netaddr-python
BuildRequires : oslo.config
BuildRequires : oslo.config-python
BuildRequires : pbr
BuildRequires : pep8-python
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pylint-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : restructuredtext_lint-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore-python
BuildRequires : tox
BuildRequires : virtualenv
Patch1: test.patch

%description
OpenStack Doc Tools
*******************
This repository contains tools used by the OpenStack Documentation
project.

%package bin
Summary: bin components for the openstack-doc-tools package.
Group: Binaries
Requires: openstack-doc-tools-data

%description bin
bin components for the openstack-doc-tools package.


%package data
Summary: data components for the openstack-doc-tools package.
Group: Data

%description data
data components for the openstack-doc-tools package.


%package python
Summary: python components for the openstack-doc-tools package.
Group: Default

%description python
python components for the openstack-doc-tools package.


%prep
%setup -q -n openstack-doc-tools-0.30.0
%patch1 -p1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/doc-tools-check-languages
/usr/bin/doc-tools-update-cli-reference
/usr/bin/openstack-auto-commands
/usr/bin/openstack-autohelp
/usr/bin/openstack-doc-test
/usr/bin/openstack-generate-docbook
/usr/bin/openstack-generate-pot
/usr/bin/openstack-jsoncheck

%files data
%defattr(-,root,root,-)
/usr/share/openstack-doc-tools/cleanup/prettify.py
/usr/share/openstack-doc-tools/cleanup/prettify.pyc
/usr/share/openstack-doc-tools/cleanup/prettify.pyo
/usr/share/openstack-doc-tools/cleanup/remove_trailing_whitespaces.sh
/usr/share/openstack-doc-tools/cleanup/remove_unnecessary_spaces.py
/usr/share/openstack-doc-tools/cleanup/remove_unnecessary_spaces.pyc
/usr/share/openstack-doc-tools/cleanup/remove_unnecessary_spaces.pyo
/usr/share/openstack-doc-tools/cleanup/retf/README.md
/usr/share/openstack-doc-tools/cleanup/retf/disabled_rules.yaml
/usr/share/openstack-doc-tools/cleanup/retf/retf.py
/usr/share/openstack-doc-tools/cleanup/retf/retf.pyc
/usr/share/openstack-doc-tools/cleanup/retf/retf.pyo
/usr/share/openstack-doc-tools/sitemap/README.md
/usr/share/openstack-doc-tools/sitemap/generator/__init__.py
/usr/share/openstack-doc-tools/sitemap/generator/__init__.pyc
/usr/share/openstack-doc-tools/sitemap/generator/__init__.pyo
/usr/share/openstack-doc-tools/sitemap/generator/items.py
/usr/share/openstack-doc-tools/sitemap/generator/items.pyc
/usr/share/openstack-doc-tools/sitemap/generator/items.pyo
/usr/share/openstack-doc-tools/sitemap/generator/pipelines.py
/usr/share/openstack-doc-tools/sitemap/generator/pipelines.pyc
/usr/share/openstack-doc-tools/sitemap/generator/pipelines.pyo
/usr/share/openstack-doc-tools/sitemap/generator/settings.py
/usr/share/openstack-doc-tools/sitemap/generator/settings.pyc
/usr/share/openstack-doc-tools/sitemap/generator/settings.pyo
/usr/share/openstack-doc-tools/sitemap/generator/spiders/__init__.py
/usr/share/openstack-doc-tools/sitemap/generator/spiders/__init__.pyc
/usr/share/openstack-doc-tools/sitemap/generator/spiders/__init__.pyo
/usr/share/openstack-doc-tools/sitemap/generator/spiders/sitemap.py
/usr/share/openstack-doc-tools/sitemap/generator/spiders/sitemap.pyc
/usr/share/openstack-doc-tools/sitemap/generator/spiders/sitemap.pyo
/usr/share/openstack-doc-tools/sitemap/scrapy.cfg
/usr/share/openstack-doc-tools/sitemap/transform-sitemap.xslt

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
