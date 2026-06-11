%undefine _debugsource_packages

Summary:	Automatic Python code formatter
Name:		python-autopep8
Version:	2.3.2
Release:	1
Group:		Development/Python
License:	MIT
Url:		https://github.com/hhatto/autopep8
Source0:	https://files.pythonhosted.org/packages/source/a/autopep8/autopep8-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildSystem:	python

%description
A tool that automatically formats Python code to conform to the
PEP 8 style guide.

%files
%{_bindir}/autopep8
%{py_puresitedir}/autopep8*
%{python_sitelib}/__pycache__/autopep8.cpython-*.pyc
