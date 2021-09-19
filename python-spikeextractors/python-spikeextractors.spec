%bcond_with tests
%global pypi_name spikeextractors

Name:           python-%{pypi_name}
Version:        0.9.7
Release:        3%{?dist}
Summary:        Extractor for spike sorting pipelines in different file formats

License:        MIT
URL:            https://github.com/SpikeInterface/spikeextractors
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(datalad)
BuildRequires:  python3dist(exdir)
BuildRequires:  python3dist(h5py)
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(nixio)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pynwb)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(tqdm)

%description
SpikeExtractors attempts to standardize data retrieval
rather than data storage. This eliminates the need for shared file formats
and allows for the creation of new tools built off of our data retrieval
guidelines.

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
Requires:  python3dist(pynwb)
Requires:  python3dist(scipy)
%description -n python3-%{pypi_name}
SpikeExtractors attempts to standardize data retrieval
rather than data storage. This eliminates the need for shared file formats
and allows for the creation of new tools built off of our data retrieval
guidelines.

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
# Ignore some test cases we can't run
%{__python3} -m pytest -v tests \
  --ignore=tests/test_gin_repo.py \
  --deselect="tests/test-extractors.py::TestExtractors::()::test_exdir_extractors" \
  --deselect="tests/test-extractors.py::TestExtractors::()::test_hdsort_extractor" \
  --deselect="tests/test-extractors.py::TestExtractors::()::test_mearec_extractors" \
  --deselect="tests/test-extractors.py::TestExtractors::()::test_shybrid_extractors" 

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Sep 19 2021 Andy Mender <andymenderunix@fedoraproject.org> - 0.9.7-3
- Add exdir to BuildRequires

* Sun Sep 12 2021 Andy Mender <andymenderunix@fedoraproject.org> - 0.9.7-2
- Add missing BuildRequires
- Switch to pytest for running tests

* Sun Aug 29 2021 Andy Mender <andymenderunix@fedoraproject.org> - 0.9.7-1
- Fix egg-info in files section
- Bump to version 0.9.7
- Re-enable tests unconditionally
- Add additional dependencies

* Sun Mar 07 2021 Andy Mender <andymenderunix@fedoraproject.org> - 0.9.3-1
- bump to version 0.9.3
- address review comments

* Sun Feb 21 2021 Andy Mender <andymenderunix@fedoraproject.org> - 0.9.0-1
- Initial submission
