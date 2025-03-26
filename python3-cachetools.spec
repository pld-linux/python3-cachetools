#
# Conditional build:
%bcond_with	doc		# don't build doc (not provided by package)
%bcond_without	tests	# do not perform "make test"

%define		module	cachetools
Summary:	Various cache implementations based on different cache algorithms
Summary(pl.UTF-8):	Rózne implementacje cache bazujące na róznych algorytmach
Name:		python-%{module}
Version:	5.5.2
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	bc4019928cf73ca154ff5416280282bb
URL:		https://github.com/tkem/cachetools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python3-modules
Requires:	python3-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides various cache implementations based on different cache algorithms, 
as well as decorators for easily memoizing function and method calls.

%description -l pl.UTF-8
Moduł dostarcza rózne implementacje cache'u bazujące na róznych algorytmach, jak również
dektoratory do łatwego zapamiętywania wyników funcji i metod.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build %{?with_tests:test}

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
