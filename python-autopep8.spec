Summary:	Automatic Python code formatter
Name:		python-autopep8
Version:	1.6.0
Release:	5
Group:		Development/Python
License:	GPLv2+
Url:		https://github.com/hhatto/autopep8
Source0:	https://files.pythonhosted.org/packages/ec/67/564f7d15712a84d4035aa5ad0b97eeafdeccdb7e806d6a822595bf0ffa5f/autopep8-1.6.0.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
A tool that automatically formats Python code to conform to the
PEP 8 style guide.

%files
%{_bindir}/autopep8
%{py_puresitedir}/autopep8*

%prep
%autosetup -p1 -n autopep8-%{version}

%build
%py_build

%install
python setup.py install --root %{buildroot}
