%define grantlee_major 5
%define grantlee_minor 0

Summary:	Qt string template engine based on the Django template system
Name:		grantlee
Version:	5.0.0
Release:	2
Group:		System/Libraries
License:	LGPLv2+
Url:		https://github.com/steveire/grantlee
Source0:	http://downloads.grantlee.org/%{name}-%{version}.tar.gz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	doxygen

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
%doc AUTHORS CHANGELOG COPYING.LIB README 
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
%setup -q
%cmake_kde5

%build
%ninja -C build

%if 0%{?apidox}
make docs
%endif

%install
%ninja_install -C build

%if 0%{?apidox}
mkdir -p %{buildroot}%{_docdir}/HTML/en/grantlee-apidocs
cp -prf build/apidocs/html/* %{buildroot}%{_docdir}/HTML/en/%{name}-apidocs
%endif

