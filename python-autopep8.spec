Summary:	Automatic Python code formatter
Name:		python-autopep8
Version:	1.5.4
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		https://github.com/hhatto/autopep8
Source0:	https://files.pythonhosted.org/packages/94/37/19bc53fd63fc1caaa15ddb695e32a5d6f6463b3de6b0922ba2a3cbb798c8/autopep8-1.5.4.tar.gz
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
