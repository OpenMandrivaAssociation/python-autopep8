Summary:	Automatic Python code formatter
Name:		python-autopep8
Version:	1.3.5
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		https://github.com/hhatto/autopep8
Source0:	https://github.com/hhatto/autopep8/archive/v%{version}.tar.gz
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
python setup.py build

%install
python setup.py install --root %{buildroot}
