%define apidox 0


Name:           grantlee
Summary:        Qt string template engine based on the Django template system
Group:          System Environment/Libraries
Version:        0.1.1
Release:        %mkrel 1
License:        LGPLv2+
URL:            http://www.gitorious.org/grantlee/pages/Home
Source0:        http://downloads.%{name}.org/%{name}-v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	cmake
BuildRequires:	qt4-devel
%if 0%{?apidocs}   
BuildRequires:  doxygen
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG COPYING.LIB README GOALS
%{_libdir}/lib%{name}*.so.*
%{_libdir}/%{name}

%description
Grantlee is a plugin based String Template system written using the Qt framework.
The goals of the project are to make it easier for application developers to
separate the structure of documents from the data they contain, opening the door
for theming.

The syntax is intended to follow the syntax of the Django template system, and
the design of Django is reused in Grantlee. Django is covered by a BSD style license.

Part of the design of both is that application developers can extend the syntax by
implementing their own tags and filters. For details of how to do that, see the API
documentation.

For template authors, different applications using Grantlee will present the same
interface and core syntax for creating new themes. For details of how to write
templates, see the documentation.


%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_includedir}/%{name}_core.h
%{_libdir}/lib%{name}*.so

%description devel
Libraries and header files to develop applications that use %{name}.


%if 0%{?apidox}
%package apidocs
Group:		Development/Documentation
Summary:	Grantlee API documentation

%files apidocs
%{_docdir}/HTML/en/grantlee-apidocs

%description apidocs
This package includes the Grantlee API documentation in HTML
format for easy browsing.
%endif


%prep
%setup -qn %{name}-v%{version}
sed -i 's,${CMAKE_INSTALL_PREFIX}/lib${LIB_SUFFIX},%{_libdir},' CMakeLists.txt

%build
%cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=/usr
%make

%if 0%{?apidocs}
make docs
%endif

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%if 0%{?apidocs}
mkdir -p %{buildroot}%{_docdir}/HTML/en/grantlee-apidocs
cp -prf %{_target_platform}/apidocs/html/* %{buildroot}%{_docdir}/HTML/en/%{name}-apidocs
%endif

%clean
rm -rf %{buildroot}


