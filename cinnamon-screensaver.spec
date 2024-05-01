%define	translations_version	6.0.2
Summary:	Cinnamon screensaver
Summary(pl.UTF-8):	Wygaszacz ekranu dla środowiska Cinnamon
Name:		cinnamon-screensaver
Version:	6.0.3
Release:	2
License:	GPL v2+
Group:		X11/Applications
#Source0Download: https://github.com/linuxmint/cinnamon-screensaver/tags
Source0:	https://github.com/linuxmint/cinnamon-screensaver/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	df9a96f2811ea17818ade0bd322671c7
#Source1Download: https://github.com/linuxmint/cinnamon-translations/tags
Source1:	https://github.com/linuxmint/cinnamon-translations/archive/%{translations_version}/cinnamon-translations-%{translations_version}.tar.gz
# Source1-md5:	36552df46587be4e32ac311b8d7084e4
URL:		https://github.com/linuxmint/cinnamon-screensaver
BuildRequires:	dbus-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pam-devel
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	xdotool-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Screensaver utility.

%description -l pl.UTF-8
Wygaszacz ekranu dla środowiska Cinnamon.

%prep
%setup -q -a1

%build
%meson build \
	--default-library=shared

%ninja_build -C build

%{__make} -C cinnamon-translations-%{translations_version}

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%py3_comp $RPM_BUILD_ROOT%{_datadir}/cinnamon-screensaver
%py3_ocomp $RPM_BUILD_ROOT%{_datadir}/cinnamon-screensaver

cd cinnamon-translations-%{translations_version}
for f in usr/share/locale/*/LC_MESSAGES/%{name}.mo ; do
	install -D "$f" "$RPM_BUILD_ROOT/$f"
done
cd ..

# no headers
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcscreensaver.so
%{__rm} $RPM_BUILD_ROOT%{_datadir}/gir-1.0/CScreensaver-1.0.gir
%{__rm} $RPM_BUILD_ROOT%{_pkgconfigdir}/cscreensaver.pc

# not supported by glibc (as of 2.39)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{frp,mo,nap,rue,sco}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md debian/changelog
%attr(755,root,root) %{_bindir}/cinnamon-screensaver
%attr(755,root,root) %{_bindir}/cinnamon-screensaver-command
%attr(755,root,root) %{_bindir}/cinnamon-unlock-desktop
%attr(755,root,root) %{_libexecdir}/cinnamon-screensaver-pam-helper
%attr(755,root,root) %{_libexecdir}/cs-backup-locker
%attr(755,root,root) %{_libdir}/libcscreensaver.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcscreensaver.so.0
%{_libdir}/girepository-1.0/CScreensaver-1.0.typelib
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/cinnamon-screensaver
%dir %{_datadir}/cinnamon-screensaver
%attr(755,root,root) %{_datadir}/cinnamon-screensaver/cinnamon-screensaver-command.py
%attr(755,root,root) %{_datadir}/cinnamon-screensaver/cinnamon-screensaver-main.py
%attr(755,root,root) %{_datadir}/cinnamon-screensaver/service.py
%{_datadir}/cinnamon-screensaver/__init__.py
%{_datadir}/cinnamon-screensaver/albumArt.py
%{_datadir}/cinnamon-screensaver/audioPanel.py
%{_datadir}/cinnamon-screensaver/baseWindow.py
%{_datadir}/cinnamon-screensaver/cinnamon-screensaver.css
%{_datadir}/cinnamon-screensaver/clock.py
%{_datadir}/cinnamon-screensaver/config.py
%{_datadir}/cinnamon-screensaver/constants.py
%{_datadir}/cinnamon-screensaver/floating.py
%{_datadir}/cinnamon-screensaver/infoPanel.py
%{_datadir}/cinnamon-screensaver/manager.py
%{_datadir}/cinnamon-screensaver/monitorView.py
%{_datadir}/cinnamon-screensaver/osk.py
%{_datadir}/cinnamon-screensaver/passwordEntry.py
%{_datadir}/cinnamon-screensaver/playerControl.py
%{_datadir}/cinnamon-screensaver/singletons.py
%{_datadir}/cinnamon-screensaver/stage.py
%{_datadir}/cinnamon-screensaver/status.py
%{_datadir}/cinnamon-screensaver/unlock.py
%{_datadir}/cinnamon-screensaver/volumeControl.py
%{_datadir}/cinnamon-screensaver/__pycache__
%{_datadir}/cinnamon-screensaver/dbusdepot
%{_datadir}/cinnamon-screensaver/pamhelper
%{_datadir}/cinnamon-screensaver/util
%{_datadir}/cinnamon-screensaver/widgets
%{_datadir}/dbus-1/services/org.cinnamon.ScreenSaver.service
%{_desktopdir}/org.cinnamon.ScreenSaver.desktop
%{_iconsdir}/hicolor/scalable/actions/screensaver-switch-users-symbolic.svg
%{_iconsdir}/hicolor/scalable/actions/screensaver-unlock-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/csr-backup-locker-icon.svg
%{_iconsdir}/hicolor/scalable/status/screensaver-blank.svg
%{_iconsdir}/hicolor/scalable/status/screensaver-notification-symbolic.svg
