Name:           openttd-opensfx
Version:        0.2.3
Release:        1%{?dist}
Summary:        Sound replacement files for OpenTTD

License:        Creative Commons Sampling Plus 1.0
URL:            http://www.openttd.org/en/
Source0:        http://bundles.openttdcoop.org/opensfx/releases/%{version}/opensfx-%{version}-source.tar.gz

BuildRequires:  catcodec >= 1.0.5
Requires:       openttd       

%description
OpenSFX is an open source replacement for the original Transport Tycoon
Deluxe base sounds used by OpenTTD. The main goal of OpenSFX therefore
is to provide a set of free sounds which make it possible to play
OpenTTD without requiring the (copyrighted) files from the Transport
Tycoon Deluxe cd. This potentially increases the OpenTTD fanbase and
makes it a true free game (with "free" as in both "free beer" and "open
source").

# To suppress creation of a -debuginfo package:
%global debug_package %{nil}


%prep
%autosetup -n opensfx-%{version}-source


%build
make %{?_smp_mflags}


%install
%make_install
cp -pr %{_sourcedir}/opensfx-%{version}-source/docs/* %{_builddir}/opensfx-%{version}-source/
mkdir -p %{buildroot}/usr/share/openttd/data/
cp -pr %{_sourcedir}/opensfx-%{version}-source/opensfx.* %{buildroot}/usr/share/openttd/data/


%files
%license license.txt
%doc changelog.txt digifish_music_grant.txt readme.ptxt descriptions.ptxt
/usr/share/openttd/data/opensfx.*

%changelog
* Sun Sep  4 2016 Andy Mender <andymenderunix@gmail.com>
- 
