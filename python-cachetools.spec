#
# Conditional build:
%bcond_with	doc		# don't build doc (not provided by package)
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	cachetools
Summary:	Various cache implementations based on different cache algorithms
Summary(pl.UTF-8):	Rózne implementacje cache bazujące na róznych algorytmach
# Name must match the python module/package name (as in 'import' statement)
Name:		python-%{module}
Version:	0.7.0
Release:	4
License:	MIT
Group:		Libraries/Python

Source0:	https://pypi.python.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	c67ebb099e7607b689f79b2869585d36
URL:		https://github.com/tkem/cachetools
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-distribute
%endif
%if %{with python3}
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
Requires:		python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides various cache implementations based on different cache algorithms, 
as well as decorators for easily memoizing function and method calls.

%description -l pl.UTF-8
Moduł dostarcza rózne implementacje cache'u bazujące na róznych algorytmach, jak również
dektoratory do łatwego zapamiętywania wyników funcji i metod.

%package -n python3-%{module}
Summary:	Various cache implementations based on different cache algorithms
Summary(pl.UTF-8):	Rózne implementacje cache bazujące na róznych algorytmach
Group:		Libraries/Python
Requires:		python3-modules

%description -n python3-%{module}
This module provides various cache implementations based on different cache algorithms, 
as well as decorators for easily memoizing function and method calls.

%description -n python3-%{module} -l pl.UTF-8
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
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
