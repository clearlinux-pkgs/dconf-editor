#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dconf-editor
Version  : 43.0
Release  : 21
URL      : https://download.gnome.org/sources/dconf-editor/43/dconf-editor-43.0.tar.xz
Source0  : https://download.gnome.org/sources/dconf-editor/43/dconf-editor-43.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: dconf-editor-bin = %{version}-%{release}
Requires: dconf-editor-data = %{version}-%{release}
Requires: dconf-editor-license = %{version}-%{release}
Requires: dconf-editor-locales = %{version}-%{release}
Requires: dconf-editor-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : glib-dev
BuildRequires : pkgconfig(dconf)
BuildRequires : pkgconfig(libhandy-1)
BuildRequires : vala
Patch1: 0001-lookup-for-clearlinux-glib-schemas-cached-in-var.patch

%description
# Dconf-Editor
A GSettings editor for GNOME.
## Useful links
- Homepage: <https://wiki.gnome.org/Apps/DconfEditor>
- Report issues: <https://gitlab.gnome.org/GNOME/dconf-editor/issues/>
- Translate: <https://wiki.gnome.org/TranslationProject>
- Code of Conduct: <https://gitlab.gnome.org/GNOME/dconf-editor/blob/master/code-of-conduct.md>

%package bin
Summary: bin components for the dconf-editor package.
Group: Binaries
Requires: dconf-editor-data = %{version}-%{release}
Requires: dconf-editor-license = %{version}-%{release}

%description bin
bin components for the dconf-editor package.


%package data
Summary: data components for the dconf-editor package.
Group: Data

%description data
data components for the dconf-editor package.


%package license
Summary: license components for the dconf-editor package.
Group: Default

%description license
license components for the dconf-editor package.


%package locales
Summary: locales components for the dconf-editor package.
Group: Default

%description locales
locales components for the dconf-editor package.


%package man
Summary: man components for the dconf-editor package.
Group: Default

%description man
man components for the dconf-editor package.


%prep
%setup -q -n dconf-editor-43.0
cd %{_builddir}/dconf-editor-43.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664142680
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/dconf-editor
cp %{_builddir}/dconf-editor-%{version}/COPYING %{buildroot}/usr/share/package-licenses/dconf-editor/31a3d460bb3c7d98845187c716a30db81c44b615 || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang dconf-editor

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dconf-editor

%files data
%defattr(-,root,root,-)
/usr/share/applications/ca.desrt.dconf-editor.desktop
/usr/share/bash-completion/completions/dconf-editor
/usr/share/dbus-1/services/ca.desrt.dconf-editor.service
/usr/share/glib-2.0/schemas/ca.desrt.dconf-editor.gschema.xml
/usr/share/icons/hicolor/scalable/actions/ca.desrt.dconf-editor.big-rows-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/ca.desrt.dconf-editor.small-rows-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/ca.desrt.dconf-editor.Devel.svg
/usr/share/icons/hicolor/scalable/apps/ca.desrt.dconf-editor.svg
/usr/share/icons/hicolor/symbolic/apps/ca.desrt.dconf-editor-symbolic.svg
/usr/share/metainfo/ca.desrt.dconf-editor.appdata.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dconf-editor/31a3d460bb3c7d98845187c716a30db81c44b615

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dconf-editor.1

%files locales -f dconf-editor.lang
%defattr(-,root,root,-)

