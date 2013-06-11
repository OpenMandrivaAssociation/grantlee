%define apidox 0
%{?_without_apidox:%global compile_apidox 0}

Summary:	Qt string template engine based on the Django template system
Name:		grantlee
Version:	0.3.0
Release:	2
Group:		System/Libraries
License:	LGPLv2+
Url:		http://www.gitorious.org/grantlee/pages/Home
Source0:	http://downloads.%{name}.org/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	kde4-macros
BuildRequires:	qt4-devel
%if 0%{?apidocs}
BuildRequires:	doxygen
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
%doc AUTHORS CHANGELOG COPYING.LIB README GOALS
%{_libdir}/%{name}/?.?

#--------------------------------------------------------------------

%define grantlee_gui_major 0
%define libgrantlee_gui %mklibname grantlee_gui %{grantlee_gui_major}

%package -n %{libgrantlee_gui}
Summary:	Library files for %{name}
Group:		System/Libraries

%description  -n %{libgrantlee_gui}
Libraries for %{name}.

%files -n %{libgrantlee_gui}
%{_libdir}/libgrantlee_gui.so.%{grantlee_gui_major}*

#--------------------------------------------------------------------

%define grantlee_core_major 0
%define libgrantlee_core %mklibname grantlee_core %{grantlee_core_major}

%package -n %{libgrantlee_core}
Summary:	Library files for %{name}
Group:		System/Libraries

%description  -n %{libgrantlee_core}
Libraries for %{name}.

%files -n %{libgrantlee_core}
%{_libdir}/libgrantlee_core.so.%{grantlee_core_major}*

#--------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libgrantlee_gui} = %{version}-%{release}
Requires:	%{libgrantlee_core} = %{version}-%{release}

%description devel
Libraries and header files to develop applications that use %{name}.

%files devel
%{_libdir}/cmake/%{name}
%{_includedir}/%{name}
%{_includedir}/%{name}_core.h
%{_includedir}/%{name}_templates.h
%{_libdir}/lib%{name}*.so

#--------------------------------------------------------------------

%if 0%{?apidox}
%package apidocs
Group:		Development/Documentation
Summary:	Grantlee API documentation

%description apidocs
This package includes the Grantlee API documentation in HTML
format for easy browsing.

%files apidocs
%doc %{_docdir}/HTML/en/grantlee-apidocs
%endif
#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4

%make
%if 0%{?apidox}
make docs
%endif

%install
%makeinstall_std -C build

%if 0%{?apidox}
mkdir -p %{buildroot}%{_docdir}/HTML/en/grantlee-apidocs
cp -prf build/apidocs/html/* %{buildroot}%{_docdir}/HTML/en/%{name}-apidocs
%endif

