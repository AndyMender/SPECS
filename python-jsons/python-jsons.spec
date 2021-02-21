%global pypi_name jsons

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Python library for (de)serializing objects to/from JSON

License:        MIT
URL:            https://github.com/ramonhagenaars/jsons
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Jsons is a library that allows you to serialize your plain old Python
objects to readable json (dicts or strings) and deserialize them back.
No magic, no special types, no polluting your objects.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:	python3dist(typish)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Jsons is a library that allows you to serialize your plain old Python
objects to readable json (dicts or strings) and deserialize them back.
No magic, no special types, no polluting your objects.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-1
- Initial package for Fedora
