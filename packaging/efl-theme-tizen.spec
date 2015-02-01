Name:          efl-theme-tizen
Summary:       Tizen theme files
Version:       1.1.52
Release:       1
Group:         TO_BE/FILLED_IN
License:       BSD 2-Clause
Source0:       %{name}-%{version}.tar.gz
BuildRequires: edje-bin
%define _unpackaged_files_terminate_build 0

%description
Tizen heme for EFL

%prep
%setup -q

%build
export CFLAGS+=" --fPIC"
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed -Wl,--rpath=/usr/lib"

%if "%{?tizen_profile_name}" == "wearable"
    export TARGET=2.3-wearable
    export SIZE=HVGA
%elseif "%{?tizen_profile_name}" == "mobile"
    export TARGET=2.3-mobile
    export SIZE=WVGA
%endif

make

%install

%if "%{?tizen_profile_name}" == "wearable"
    export TARGET=2.3-wearable
    export SIZE=HVGA
%elseif "%{?tizen_profile_name}" == "mobile"
    export TARGET=2.3-mobile
    export SIZE=WVGA
%endif

make install prefix=%{_prefix} DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/%{_datadir}/license/%{name}

%files
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/*.edj
%{_datadir}/license/%{name}
%manifest %{name}.manifest
