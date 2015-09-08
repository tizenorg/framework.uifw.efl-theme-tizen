Name:          efl-theme-tizen
Summary:       Tizen theme files
Version:       1.1.58
Release:       1
Group:         TO_BE/FILLED_IN
License:       BSD 2-Clause and Flora-1.1
Source0:       %{name}-%{version}.tar.gz
BuildRequires: model-build-features
BuildRequires: edje-bin
%define _unpackaged_files_terminate_build 0

%description
Tizen heme for EFL

%prep
%setup -q

%build
export CFLAGS+=" --fPIC"
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed -Wl,--rpath=/usr/lib"

%if "%{?model_build_feature_formfactor}" == "circle"
    export TARGET=2.3-wearable-circle
%else
	%if "%{?tizen_profile_name}" == "wearable"
        export TARGET=2.3-wearable
    %else
        export TARGET=2.3-mobile
        export SIZE=WVGA
    %endif
%endif

make

%install
%if "%{?model_build_feature_formfactor}" == "circle"
    export TARGET=2.3-wearable-circle
%else
	%if "%{?tizen_profile_name}" == "wearable"
        export TARGET=2.3-wearable
    %else
        export TARGET=2.3-mobile
        export SIZE=WVGA
    %endif
%endif

make install prefix=%{_prefix} DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/%{_datadir}/license/%{name}

%files
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/*.edj
%{_datadir}/license/%{name}
%manifest %{name}.manifest
