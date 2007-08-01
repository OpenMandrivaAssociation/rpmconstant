%define name	rpmconstant
%define version	0.1.2
%define release	%mkrel 2

%define major		0
%define libname		%mklibname %name %major
%define develname	%mklibname %name -d

Summary: A library to bind RPM constant values
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://rpm4.zarb.org/download/%{name}-%{version}.tar.bz2
License: LGPLv2.1
Group: Development/C
Url: http://rpm.zarb.org/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: rpm-devel

%description
This library provides basic functions to map internal RPM constant values
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

%package -n %develname
Summary: Development files from librpmconstant
Group: Development/C
Provides: %name-devel = %version-%release
Provides: lib%{name}-devel = %version-%release
Requires: %libname = %version-%release
Obsoletes: %mklibname rpmconstant 0 -d

%description -n %develname
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
%_libdir/lib%name.so.*

%files -n %develname
%defattr(-,root,root)
%doc constant.c AUTHORS ChangeLog README
%_includedir/%name/%name.h
%_libdir/lib%name.so
%_libdir/lib%name.a
%_libdir/lib%name.la

