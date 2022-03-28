Summary:	Tool to ease building collections of source packages
Summary(pl.UTF-8):	Narzędzie ułatwiające budowanie zbioru pakietów źródłowych
Name:		jhbuild
Version:	3.38.0
Release:	4
License:	GPL v2+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/jhbuild/3.38/%{name}-%{version}.tar.xz
# Source0-md5:	8621b7757fe0d4e04a66183a380d8f10
URL:		https://wiki.gnome.org/Projects/Jhbuild
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.5
BuildRequires:	rpmbuild(macros) >= 1.507
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	python3 >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JHBuild is a tool designed to ease building collections of source
packages, called "modules".

JHBuild was originally written for building GNOME, but has since been
extended to be usable with other projects.

%description -l pl.UTF-8
JHBuild to narzędzie zaprojektowane w celu ułatwienia budowania zbioru
pakietów źródłowych, zwanych "modułami".

Oryginalnie zostało zaprojektowane w celu ułatwienia budowania GNOME,
ale zostało rozszerzone, aby nadawało się do użycia z innymi
projektami.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' scripts/hg-update.py
%{__sed} -i -e '1s,/usr/bin/env @python@,%{__python3},' scripts/jhbuild.in

%build
%configure \
	ac_cv_build=%{_build} \
	ac_cv_host=%{_host} \
	am_cv_python_pythondir=%{py3_sitescriptdir} \
	--enable-doc-installation \
	--enable-gui \
	--with-python=%{__python3}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.rst
%attr(755,root,root) %{_bindir}/jhbuild
%{py3_sitescriptdir}/jhbuild
%dir %{_datadir}/jhbuild
%{_datadir}/jhbuild/sitecustomize
%{_datadir}/jhbuild/triggers
%attr(755,root,root) %{_datadir}/jhbuild/hg-update.py
%{_datadir}/jhbuild/*.png
%{_desktopdir}/jhbuild.desktop
