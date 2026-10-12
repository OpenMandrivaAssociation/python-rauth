Name:		python-rauth
Version:	0.7.3
Release:	2
Summary:	A Python library for OAuth 1.0/a, 2.0, and Ofly
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/rauth/
Source0:	rauth-0.7.3.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(requests)
BuildArch:	noarch
%description
A Python library for OAuth 1.0/a, 2.0, and Ofly.

%files
%{py_sitedir}/*
