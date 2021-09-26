%bcond_with tests
%global pypi_name probeinterface

Name:           python-%{pypi_name}
Version:        0.2.5
Release:        1%{?dist}
Summary:        Handles probes for electrophysiology experiments

License:        MIT
URL:            https://github.com/SpikeInterface/%{pypi_name}

Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pytest)

%description
A Python package to handle the layout, geometry, and wiring of silicon
probes for extracellular electrophysiology experiments.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%py_provides python3-%{pypi_name}
 
Requires:  python3dist(matplotlib)
Requires:  python3dist(numpy)
Requires:  python3dist(pandas)

%description -n python3-%{pypi_name}
A Python package to handle the layout, geometry, and wiring of silicon
probes for extracellular electrophysiology experiments.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# Network- and device-dependent won't run during builds
%{__python3} -m pytest -v tests \
  --deselect="tests/test_library.py::test_download_probeinterface_file" \
  --deselect="tests/test_library.py::test_get_from_cache" \
  --deselect="tests/test_library.py::test_get_probe" \
  --deselect="tests/test_wiring.py::test_wire_probe"

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Sep 26 2021 Andy Mender <andymenderunix@fedoraproject.org> - 0.2.5-1
- Initial package building

