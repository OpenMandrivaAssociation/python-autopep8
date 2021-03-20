Summary:	Automatic Python code formatter
Name:		python-autopep8
Version:	1.5.6
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		https://github.com/hhatto/autopep8
Source0:	https://files.pythonhosted.org/packages/96/a5/d282540e6e0ea8a3fd58edaf97eff1d787e56787e5bf6c70f670aaedef7a/autopep8-1.5.6.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(setuptools)
BuildArch:	noarch

%description
A tool that automatically formats Python code to conform to the
PEP 8 style guide.

%files
%{_bindir}/autopep8
%{py_puresitedir}/autopep8*
%{py_puresitedir}/__pycache__/*

%prep
%autosetup -p1 -n autopep8-%{version}

%build
%py_build

%install
python setup.py install --root %{buildroot}
