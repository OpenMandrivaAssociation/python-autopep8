Summary:	Automatic Python code formatter
Name:		python-autopep8
Version:	1.5.5
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		https://github.com/hhatto/autopep8
Source0:	https://files.pythonhosted.org/packages/32/23/3bc0b99f932155c19e8b6b4f01021b735727ee6b0ccda6b8e5f99bef1b6d/autopep8-1.5.5.tar.gz
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
