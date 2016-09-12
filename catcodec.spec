Name:           catcodec
Version:        1.0.5
Release:        1
Summary:        encoder/decoder of OpenTTD sound sample catalogues

License:        GPLv2+
URL:            http://www.openttd.org/en/
Source0:        http://binaries.openttd.org/extra/%{name}/%{version}/%{name}-%{version}-source.tar.gz

#BuildRequires:  
#Requires:       

%description
catcodec decodes and encodes sample catalogues for OpenTTD. These sample
catalogues are not much more than some meta-data (description and file name)
and raw PCM data.

# To suppress creation of a -debuginfo package:
%global debug_package %{nil}


%prep
%autosetup


%build
make %{?_smp_mflags}


%install
%make_install

# Moving the binary to /usr/bin/:
mkdir -p %{buildroot}%{_bindir}/
cp -p %{name} %{buildroot}%{_bindir}/

# Copying docs from /usr/local/share/doc to %_buildir:
cp -pr %{buildroot}/usr/local/share/doc/%{name}/* %{_builddir}/%{name}-%{version}/

# Copying manpages from /usr/local/share/man to /usr/share/man:
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p %{buildroot}/usr/local/share/man/man1/%{name}.1.gz %{buildroot}%{_mandir}/man1/

# /usr/local clean-up:
rm -rf %{buildroot}/usr/local/


%files
%license COPYING
%doc changelog.txt readme.txt 
%{_bindir}/catcodec
%{_mandir}/man1/catcodec.1.gz


%changelog
* Sun Sep  4 2016 Andy Mender <andymenderunix@gmail.com>
- Initial build 
