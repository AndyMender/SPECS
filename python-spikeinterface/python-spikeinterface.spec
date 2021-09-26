%bcond_with tests
%global pypi_name spikeinterface

Name:           python-%{pypi_name}
Version:        0.10.0
Release:        1%{?dist}
Summary:        A unified framework for spike sorting

License:        MIT
URL:            https://github.com/SpikeInterface/spikeinterfacExtractor

Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(neo)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pynwb)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(tqdm)

# TODO: submit missing dependencies
# BuildRequires:  python3dist(probeinterface)

# BuildRequires:  python3dist(exdir)
# BuildRequires:  python3dist(h5py)
# BuildRequires:  python3dist(nixio)
# BuildRequires:  python3dist(scipy)

%description
SpikeInterface is a Python framework designed to unify preexisting spike
sorting technologies into a single code base.

In addition to implementing multi-format I/O for various formats,
the framework makes it possible to develop software tools that are agnostic
to the underlying formats by working with the standardized python objects
(recording and sorting extractors). These include processing routines
(filters, sorting algorithms, downstream processing), and visualization
widgets. It also provides mechanisms for lazy manipulation of recordings
and sortings (concatenation, combination, subset extraction).

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%py_provides python3-%{pypi_name}
 
Requires:  python3dist(h5py)
Requires:  python3dist(numpy)
Requires:  python3dist(pynwb)

%description -n python3-%{pypi_name}
SpikeInterface is a Python framework designed to unify preexisting spike
sorting technologies into a single code base.

In addition to implementing multi-format I/O for various formats,
the framework makes it possible to develop software tools that are agnostic
to the underlying formats by working with the standardized python objects
(recording and sorting extractors). These include processing routines
(filters, sorting algorithms, downstream processing), and visualization
widgets. It also provides mechanisms for lazy manipulation of recordings
and sortings (concatenation, combination, subset extraction).
%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# The submodules are not identified correctly in tests
# %{__python3} -m pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Sep 25 2021 Andy Mender <andymenderunix@fedoraproject.org> - 0.10.0-1
- Initial package building

