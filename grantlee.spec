# FIXME at the moment, file names are identical between
# Qt5 and Qt6 builds, so we can build only one
%bcond_with qt6

%define grantlee_major 5
%define grantlee_minor 3

Summary:	Qt string template engine based on the Django template system
Name:		grantlee
Version:	5.3.1
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		https://github.com/steveire/grantlee
Source0:	https://github.com/steveire/grantlee/releases/download/v%{version}/grantlee-%{version}.tar.gz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	doxygen
%if %{with qt6}
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6DBusTools)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6QmlIntegration)
BuildRequires:	cmake(Qt6QmlTools)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6)
%endif

%description
Grantlee is a plugin based String Template system written using the Qt
framework. The goals of the project are to make it easier for application
developers to separate the structure of documents from the data they
contain, opening the door for theming.

The syntax is intended to follow the syntax of the Django template
system, and the design of Django is reused in Grantlee. Django is covered
by a BSD style license.

Part of the design of both is that application developers can extend the
syntax by implementing their own tags and filters. For details of how to
do that, see the API documentation.

For template authors, different applications using Grantlee will present
the same interface and core syntax for creating new themes. For details
of how to write templates, see the documentation.

%files
%doc AUTHORS CHANGELOG COPYING.LIB
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{grantlee_major}.%{grantlee_minor}
%{_libdir}/%{name}/%{grantlee_major}.%{grantlee_minor}/*

#--------------------------------------------------------------------

%define libgrantlee_template %mklibname grantlee_template %{grantlee_major}

%package -n %libgrantlee_template
Summary:        Library files for %{name}
Group:          System/Libraries

%description  -n %libgrantlee_template
Libraries for %{name}.

%files -n %libgrantlee_template
%{_libdir}/libGrantlee_Templates.so.%{grantlee_major}.%{grantlee_minor}*
%{_libdir}/libGrantlee_Templates.so.%{grantlee_major}

#--------------------------------------------------------------------

%define libgrantlee_textdocument %mklibname grantlee_textdocument %{grantlee_major}

%package -n %libgrantlee_textdocument
Summary:    Library files for %{name}
Group:      System/Libraries

%description  -n %libgrantlee_textdocument
Libraries for %{name}.

%files -n %libgrantlee_textdocument
%{_libdir}/libGrantlee_TextDocument.so.%{grantlee_major}.%{grantlee_minor}*
%{_libdir}/libGrantlee_TextDocument.so.%{grantlee_major}

#--------------------------------------------------------------------

%package devel
Summary:       Development files for %{name}
Group:         Development/KDE and Qt
Requires:      %name = %{version}-%{release}
Requires:      %libgrantlee_template = %{version}-%{release}
Requires:      %libgrantlee_textdocument = %{version}-%{release}

%description devel
Libraries and header files to develop applications that use %{name}.

%files devel
%{_includedir}/%{name}
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/cmake/Grantlee5

%prep
%autosetup -p1
%cmake_kde5
cd ..

%if %{with qt6}
export CMAKE_BUILD_DIR=build-qt6
%cmake \
	-DGRANTLEE_BUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%endif

%build
%ninja_build -C build

%if %{with qt6}
%ninja_build -C build-qt6
%endif

%install
%if %{with qt6}
%ninja_install -C build-qt6
%endif

%ninja_install -C build
