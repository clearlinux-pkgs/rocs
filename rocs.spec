#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : rocs
Version  : 21.04.0
Release  : 6
URL      : https://download.kde.org/stable/release-service/21.04.0/src/rocs-21.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.04.0/src/rocs-21.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.04.0/src/rocs-21.04.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : EPL-1.0 GFDL-1.2 GPL-2.0 LGPL-2.1
Requires: rocs-bin = %{version}-%{release}
Requires: rocs-data = %{version}-%{release}
Requires: rocs-lib = %{version}-%{release}
Requires: rocs-license = %{version}-%{release}
Requires: rocs-locales = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : grantlee-dev
BuildRequires : kdoctools-dev
BuildRequires : ktexteditor-dev
BuildRequires : qtbase-dev
BuildRequires : syntax-highlighting-dev

%description
# Outline
This readme file currently covers the following topics (further topics will be
included in the future):

%package bin
Summary: bin components for the rocs package.
Group: Binaries
Requires: rocs-data = %{version}-%{release}
Requires: rocs-license = %{version}-%{release}

%description bin
bin components for the rocs package.


%package data
Summary: data components for the rocs package.
Group: Data

%description data
data components for the rocs package.


%package dev
Summary: dev components for the rocs package.
Group: Development
Requires: rocs-lib = %{version}-%{release}
Requires: rocs-bin = %{version}-%{release}
Requires: rocs-data = %{version}-%{release}
Provides: rocs-devel = %{version}-%{release}
Requires: rocs = %{version}-%{release}

%description dev
dev components for the rocs package.


%package doc
Summary: doc components for the rocs package.
Group: Documentation

%description doc
doc components for the rocs package.


%package lib
Summary: lib components for the rocs package.
Group: Libraries
Requires: rocs-data = %{version}-%{release}
Requires: rocs-license = %{version}-%{release}

%description lib
lib components for the rocs package.


%package license
Summary: license components for the rocs package.
Group: Default

%description license
license components for the rocs package.


%package locales
Summary: locales components for the rocs package.
Group: Default

%description locales
locales components for the rocs package.


%prep
%setup -q -n rocs-21.04.0
cd %{_builddir}/rocs-21.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619244648
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1619244648
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rocs
cp %{_builddir}/rocs-21.04.0/COPYING.1.GPL2 %{buildroot}/usr/share/package-licenses/rocs/0c10177c981f7c8d708265e640bd604777a5d38b
cp %{_builddir}/rocs-21.04.0/COPYING.2.LIB.LGPL-2.1 %{buildroot}/usr/share/package-licenses/rocs/9a1929f4700d2407c70b507b3b2aaf6226a9543c
cp %{_builddir}/rocs-21.04.0/COPYING.3.DOC %{buildroot}/usr/share/package-licenses/rocs/1bd373e4851a93027ba70064bd7dbdc6827147e1
cp %{_builddir}/rocs-21.04.0/libgraphtheory/fileformats/dot/autotests/testfiles/COPYING.TESTDATA.EPL-1 %{buildroot}/usr/share/package-licenses/rocs/3348e5430ba4fb49fa8eb6e9caf4f06266639d0d
pushd clr-build
%make_install
popd
%find_lang libgraphtheory
%find_lang rocs

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rocs

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.rocs.desktop
/usr/share/config.kcfg/rocs.kcfg
/usr/share/icons/hicolor/128x128/apps/rocs.png
/usr/share/icons/hicolor/16x16/apps/rocs.png
/usr/share/icons/hicolor/22x22/apps/rocs.png
/usr/share/icons/hicolor/32x32/apps/rocs.png
/usr/share/icons/hicolor/48x48/apps/rocs.png
/usr/share/icons/hicolor/64x64/apps/rocs.png
/usr/share/icons/hicolor/scalable/actions/rocsadvancedsetup.svgz
/usr/share/icons/hicolor/scalable/actions/rocsalignbottom.svgz
/usr/share/icons/hicolor/scalable/actions/rocsaligncircle.svgz
/usr/share/icons/hicolor/scalable/actions/rocsalignleft.svgz
/usr/share/icons/hicolor/scalable/actions/rocsalignmiddle.svgz
/usr/share/icons/hicolor/scalable/actions/rocsalignright.svgz
/usr/share/icons/hicolor/scalable/actions/rocsaligntop.svgz
/usr/share/icons/hicolor/scalable/actions/rocsaligntree.svgz
/usr/share/icons/hicolor/scalable/actions/rocsalignvmiddle.svgz
/usr/share/icons/hicolor/scalable/actions/rocsbidirectional.svgz
/usr/share/icons/hicolor/scalable/actions/rocsdelete.svgz
/usr/share/icons/hicolor/scalable/actions/rocsedge.svgz
/usr/share/icons/hicolor/scalable/actions/rocsnode.svgz
/usr/share/icons/hicolor/scalable/actions/rocsselect.svgz
/usr/share/icons/hicolor/scalable/actions/rocsunidirectional.svgz
/usr/share/icons/hicolor/scalable/actions/rocsvisible.svgz
/usr/share/icons/hicolor/scalable/apps/rocs.svgz
/usr/share/kxmlgui5/rocs/rocsui.rc
/usr/share/metainfo/org.kde.rocs.appdata.xml
/usr/share/rocs/kernelapi/console.xml
/usr/share/rocs/kernelapi/document.xml
/usr/share/rocs/kernelapi/edge.xml
/usr/share/rocs/kernelapi/node.xml
/usr/share/rocs/plugin/apidoc/objectApi.html
/usr/share/rocs/plugin/apidoc/overview.html
/usr/share/rocs/schemes/kernelapi.xsd

%files dev
%defattr(-,root,root,-)
/usr/include/rocs/edge.h
/usr/include/rocs/graphdocument.h
/usr/include/rocs/node.h
/usr/lib64/librocsgraphtheory.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/rocs/index.cache.bz2
/usr/share/doc/HTML/ca/rocs/index.docbook
/usr/share/doc/HTML/de/rocs/index.cache.bz2
/usr/share/doc/HTML/de/rocs/index.docbook
/usr/share/doc/HTML/en/rocs/force-based-layout-ui-screenshot.png
/usr/share/doc/HTML/en/rocs/hi22-action-rocsalignbottom.png
/usr/share/doc/HTML/en/rocs/hi22-action-rocsaligncircle.png
/usr/share/doc/HTML/en/rocs/hi22-action-rocsalignhmiddle.png
/usr/share/doc/HTML/en/rocs/hi22-action-rocsalignleft.png
/usr/share/doc/HTML/en/rocs/hi22-action-rocsalignright.png
/usr/share/doc/HTML/en/rocs/hi22-action-rocsaligntop.png
/usr/share/doc/HTML/en/rocs/hi22-action-rocsaligntree.png
/usr/share/doc/HTML/en/rocs/hi22-action-rocsalignvmiddle.png
/usr/share/doc/HTML/en/rocs/hi22-action-rocsproperties.png
/usr/share/doc/HTML/en/rocs/hi22-actions-control-stop.png
/usr/share/doc/HTML/en/rocs/hi22-actions-controls-run.png
/usr/share/doc/HTML/en/rocs/hi22-actions-rocsdelete.png
/usr/share/doc/HTML/en/rocs/hi22-actions-rocsedge.png
/usr/share/doc/HTML/en/rocs/hi22-actions-rocsnode.png
/usr/share/doc/HTML/en/rocs/hi22-actions-rocsselectmove.png
/usr/share/doc/HTML/en/rocs/index.cache.bz2
/usr/share/doc/HTML/en/rocs/index.docbook
/usr/share/doc/HTML/en/rocs/radial-tree-layout-ui-screenshot.png
/usr/share/doc/HTML/en/rocs/rocs-control-engine-debug.png
/usr/share/doc/HTML/en/rocs/rocs-control-engine-step.png
/usr/share/doc/HTML/en/rocs/rocs-interfaces.png
/usr/share/doc/HTML/en/rocs/rocs-screenshot.png
/usr/share/doc/HTML/es/rocs/apiConsole.docbook
/usr/share/doc/HTML/es/rocs/apiDatastructure.docbook
/usr/share/doc/HTML/es/rocs/apiGraphstructure.docbook
/usr/share/doc/HTML/es/rocs/apiLinkedListstructure.docbook
/usr/share/doc/HTML/es/rocs/apiRootedTreestructure.docbook
/usr/share/doc/HTML/es/rocs/chapterImportExport.docbook
/usr/share/doc/HTML/es/rocs/index.cache.bz2
/usr/share/doc/HTML/es/rocs/index.docbook
/usr/share/doc/HTML/es/rocs/scripting-api.docbook
/usr/share/doc/HTML/it/rocs/apiConsole.docbook
/usr/share/doc/HTML/it/rocs/apiDatastructure.docbook
/usr/share/doc/HTML/it/rocs/apiGraphstructure.docbook
/usr/share/doc/HTML/it/rocs/apiLinkedListstructure.docbook
/usr/share/doc/HTML/it/rocs/apiRootedTreestructure.docbook
/usr/share/doc/HTML/it/rocs/chapterImportExport.docbook
/usr/share/doc/HTML/it/rocs/index.cache.bz2
/usr/share/doc/HTML/it/rocs/index.docbook
/usr/share/doc/HTML/nl/rocs/apiConsole.docbook
/usr/share/doc/HTML/nl/rocs/apiDatastructure.docbook
/usr/share/doc/HTML/nl/rocs/apiGraphstructure.docbook
/usr/share/doc/HTML/nl/rocs/apiLinkedListstructure.docbook
/usr/share/doc/HTML/nl/rocs/apiRootedTreestructure.docbook
/usr/share/doc/HTML/nl/rocs/chapterImportExport.docbook
/usr/share/doc/HTML/nl/rocs/index.cache.bz2
/usr/share/doc/HTML/nl/rocs/index.docbook
/usr/share/doc/HTML/nl/rocs/scripting-api.docbook
/usr/share/doc/HTML/pt/rocs/index.cache.bz2
/usr/share/doc/HTML/pt/rocs/index.docbook
/usr/share/doc/HTML/pt_BR/rocs/index.cache.bz2
/usr/share/doc/HTML/pt_BR/rocs/index.docbook
/usr/share/doc/HTML/sv/rocs/index.cache.bz2
/usr/share/doc/HTML/sv/rocs/index.docbook
/usr/share/doc/HTML/uk/rocs/index.cache.bz2
/usr/share/doc/HTML/uk/rocs/index.docbook
/usr/share/doc/HTML/uk/rocs/rocs-interfaces.png
/usr/share/doc/HTML/uk/rocs/rocs-screenshot.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/librocsgraphtheory.so.0
/usr/lib64/qt5/plugins/rocs/editorplugins/assignvaluesplugin.so
/usr/lib64/qt5/plugins/rocs/editorplugins/generategraphplugin.so
/usr/lib64/qt5/plugins/rocs/editorplugins/graphlayoutplugin.so
/usr/lib64/qt5/plugins/rocs/editorplugins/transformedgesplugin.so
/usr/lib64/qt5/plugins/rocs/fileformats/dotfileformat.so
/usr/lib64/qt5/plugins/rocs/fileformats/gmlfileformat.so
/usr/lib64/qt5/plugins/rocs/fileformats/rocs1fileformat.so
/usr/lib64/qt5/plugins/rocs/fileformats/rocs2fileformat.so
/usr/lib64/qt5/plugins/rocs/fileformats/tgffileformat.so
/usr/lib64/qt5/plugins/rocs/fileformats/tikzfileformat.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rocs/0c10177c981f7c8d708265e640bd604777a5d38b
/usr/share/package-licenses/rocs/1bd373e4851a93027ba70064bd7dbdc6827147e1
/usr/share/package-licenses/rocs/3348e5430ba4fb49fa8eb6e9caf4f06266639d0d
/usr/share/package-licenses/rocs/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f libgraphtheory.lang -f rocs.lang
%defattr(-,root,root,-)

