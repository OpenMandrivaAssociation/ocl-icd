%define libname %mklibname opencl 1
%define devname %mklibname opencl -d

%global optflags %{optflags} -O3

Name:           ocl-icd
Version:        2.2.12
Release:        3
Summary:        OpenCL ICD (Installable Client Driver) Bindings

License:        BSD
URL:            https://forge.imag.fr/projects/ocl-icd/
# See also https://github.com/OCL-dev/ocl-icd
Source0:        https://forge.imag.fr/frs/download.php/836/%{name}-%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  mesa-opencl-devel
BuildRequires:	ruby rubygems
# Once we've packaged all of this
#Recommends:     beignet
#Recommends:     mesa-libOpenCL
#Recommends:     pocl

%description
%{summary}.

%package -n %{libname}
Summary:	OpenCL Installable Client Driver library
Group:		System/Libraries

%description -n %{libname}
OpenCL Installable Client Driver library

%package -n %{devname}
Summary:        Development files for %{name}
Provides:	opencl-devel = %{version}-%{release}
Requires:	%{libname}%{?_isa} = %{version}-%{release}
Requires:       mesa-opencl-devel

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%autosetup -p1

%build
autoreconf -vfi
%configure
%make_build

%install
%make_install
rm -vrf %{buildroot}%{_defaultdocdir}

%check
make check

%files -n %{libname}
%license COPYING
%doc NEWS README
%{_libdir}/libOpenCL.so.*

%files -n %{devname}
%doc ocl_icd_loader_gen.map ocl_icd_bindings.c
%{_includedir}/ocl_icd.h
%{_libdir}/libOpenCL.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/OpenCL.pc
%optional %{_mandir}/man7/*
