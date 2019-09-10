#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dconf-editor
Version  : 3.34.1
Release  : 8
URL      : https://download.gnome.org/sources/dconf-editor/3.34/dconf-editor-3.34.1.tar.xz
Source0  : https://download.gnome.org/sources/dconf-editor/3.34/dconf-editor-3.34.1.tar.xz
Summary  : dconf Editor
Group    : Development/Tools
License  : GPL-3.0
Requires: dconf-editor-bin = %{version}-%{release}
Requires: dconf-editor-data = %{version}-%{release}
Requires: dconf-editor-license = %{version}-%{release}
Requires: dconf-editor-locales = %{version}-%{release}
Requires: dconf-editor-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : dconf-dev
BuildRequires : glib-dev
BuildRequires : pkgconfig(dconf)
BuildRequires : vala
Patch1: 0001-lookup-for-clearlinux-glib-schemas-cached-in-var.patch

%description
This is dconf-editor.  It used to be part of the 'dconf' package.

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
%setup -q -n dconf-editor-3.34.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568082686
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/dconf-editor
cp COPYING %{buildroot}/usr/share/package-licenses/dconf-editor/COPYING
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
/usr/share/icons/hicolor/16x16/apps/ca.desrt.dconf-editor.png
/usr/share/icons/hicolor/22x22/apps/ca.desrt.dconf-editor.png
/usr/share/icons/hicolor/24x24/apps/ca.desrt.dconf-editor.png
/usr/share/icons/hicolor/256x256/apps/ca.desrt.dconf-editor.png
/usr/share/icons/hicolor/32x32/apps/ca.desrt.dconf-editor.png
/usr/share/icons/hicolor/48x48/apps/ca.desrt.dconf-editor.png
/usr/share/icons/hicolor/64x64/apps/ca.desrt.dconf-editor.png
/usr/share/icons/hicolor/scalable/actions/ca.desrt.dconf-editor.big-rows-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/ca.desrt.dconf-editor.small-rows-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/ca.desrt.dconf-editor-symbolic.svg
/usr/share/metainfo/ca.desrt.dconf-editor.appdata.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dconf-editor/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dconf-editor.1

%files locales -f dconf-editor.lang
%defattr(-,root,root,-)

