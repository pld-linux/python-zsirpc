Summary:	Simplified wrapper for ZSI SOAP module
Name:		python-zsirpc
Version:	1.1
Release:	4
License:	Python
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/ose/zsirpc-%{version}.tar.gz
# Source0-md5:	aaecf87a04d3f2f8f96ca430dbbd5ba7
URL:		http://ose.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python-ZSI
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simplified wrapper for ZSI SOAP module.

%prep
%setup -q -n zsirpc-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc zsi*.py functions.py
%{py_sitescriptdir}/*.egg-info
%dir %{py_sitescriptdir}/zsirpc
%{py_sitescriptdir}/zsirpc/*.py[co]
