#
# Conditional build:
%bcond_with	doc	# Sphinx documentation (fails to build)
%bcond_without	tests	# unit tests

%define		module	cachetools
Summary:	Extensible memoizing collections and decorators
Summary(pl.UTF-8):	Rozszerzalne kolekcje i dekoratory z pamięcią
Name:		python3-%{module}
Version:	5.5.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/cachetools/
Source0:	https://files.pythonhosted.org/packages/source/c/cachetools/%{module}-%{version}.tar.gz
# Source0-md5:	bc4019928cf73ca154ff5416280282bb
URL:		https://github.com/tkem/cachetools
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides various memoizing collections and decorators,
including variants of the Python Standard Library's @lru_cache
function decorator.

%description -l pl.UTF-8
Ten moduł udostępnia różne kolekcje i dekoratory z pamięcią, w tym
warianty dekoratora funkcji @lru_cache z biblioteki standardowej
Pythona.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API modułu %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
sphinx-build-3 -b html docs docs/_build/html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
