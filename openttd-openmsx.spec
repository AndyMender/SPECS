Name:           openttd-openmsx
Version:        0.3.1
Release:        1%{?dist}
Summary:        Music replacement files for OpenTTD

License:        GPL 2.0 
URL:            http://www.openttd.org/en/
Source0:        http://bundles.openttdcoop.org/openmsx/releases/%{version}/openmsx-%{version}-source.tar.gz

#BuildRequires:  
Requires:       openttd

%description
OpenMSX is an open source replacement for the original Transport Tycoon Deluxe
(TTD) music. All contributions are licensed under the GPL v2.

# To suppress creation of a -debuginfo package:
%global debug_package %{nil}


%prep
%autosetup -n openmsx-%{version}-source


%build
make %{?_smp_mflags}


%install
%make_install
cp -pr %{_sourcedir}/openmsx-%{version}-source/docs/* %{_builddir}/openmsx-%{version}-source/
mkdir -p %{buildroot}/usr/share/openttd/gm/
cp -pr %{_sourcedir}/openmsx-%{version}-source/openmsx-%{version}/*.mid %{buildroot}/usr/share/openttd/gm/
cp -pr %{_sourcedir}/openmsx-%{version}-source/openmsx-%{version}/openmsx.obm %{buildroot}/usr/share/openttd/gm/


%clean
rm -rf %{buildroot}

%files
%license license.ptxt
%doc changelog.ptxt descriptions.ptxt license.ptxt redfarn_music_grant.txt
/usr/share/openttd/gm/openmsx.obm
/usr/share/openttd/gm/*.mid


%changelog
* Sun Sep  4 2016 Andy Mender <andymenderunix@gmail.com>
- 
