# This rpm is in the SVN
# $Id: rpmconstant.spec 36944 2006-06-11 13:44:56Z nanardon $

%define name rpmconstant
%define version 0.1.2
%define release %mkrel 1

%define major 0
%define libname %mklibname %name %major

Summary: A library to bind rpm constant
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://rpm.zarb.org/download/%{name}-%{version}.tar.bz2
License: LGPL 
Group: Development/C
Url: http://rpm.zarb.org/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: rpm-devel

%description
This library provides basics functions to map internal rpm constant value
with their name. This is useful for perl/python or other language which has
binding over rpmlib.

%package -n %libname
Summary: A library to bind rpm constant
Group: Development/C
Provides: lib%{name} = %version-%release

%description -n %libname
This library provides basics functions to map internal rpm constant value
with their name. This is useful for perl/python or other language which has
binding over rpmlib.

%package -n %libname-devel
Summary: Development files from librpmconstant
Group: Development/C
Provides: %name-devel = %version-%release
Provides: lib%{name}-devel = %version-%release
Requires: %libname = %version-%release

%description -n %libname-devel
This library provides basics functions to map internal rpm constant value
with their name. This is useful for perl/python or other language which has
binding over rpmlib.

You need this package to build applications using librpmconstant.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%_bindir/%name

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%_libdir/lib%name.so.*

%files -n %libname-devel
%defattr(-,root,root)
%doc constant.c AUTHORS ChangeLog README
%_includedir/%name/%name.h
%_libdir/lib%name.so
%_libdir/lib%name.a
%_libdir/lib%name.la

