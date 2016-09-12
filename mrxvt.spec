Name:           mrxvt
Version:        0.5.4
Release:        1%{?dist}
Summary:        lightweight, tabbed terminal emulator based on rxvt        

License:        GPLv2+
URL:            https://github.com/Jehan/%{name}.git
Source0:        https://github.com/Jehan/%{name}/archive/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  git autoconf automake libtool perl xorg-x11-server-devel
Requires:       libutempter libXrender libXpm libjpeg-turbo libpng

%description
Mrxvt is a multi-tabbed (like gnome-terminal/konsole) terminal emulator for the
X Window System. It targets to be light-weight, so the desktop environment,
like CDE, KDE or GTK is not required in order to run it. It achieves this
without losing the common useful features, like tab, image and
pseudo-transparent background, multi-style scrollbars, XIM and CJK support,
etc.

# To suppress creation of a -debuginfo package:
%global debug_package %{nil}
%global commit0 0feba85811afb7ccf2955f68f2cea7aeb4b7fad6
%global gittag0 release-%{version}
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})


%prep
%autosetup -n %{name}-%{gittag0}
./bootstrap.sh


%build
%configure --enable-everything --disable-debug
make %{?_smp_mflags}


%install
%make_install


%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_defaultdocdir}/%{name}/*
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/pixmaps/*
%{_sysconfdir}/%{name}/*


%changelog
* Tue Sep 13 2016 Andy Mender <andymenderunix@gmail.com>
- Initial build
