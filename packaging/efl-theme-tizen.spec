Name:          efl-theme-tizen
Summary:       Tizen theme files
Version:       1.2.34
Release:       1
Group:         TO_BE/FILLED_IN
License:       BSD 2-Clause and Flora-1.1
Source0:       %{name}-%{version}.tar.gz
#BuildRequires: sec-product-features
BuildRequires: edje-bin
%define _unpackaged_files_terminate_build 0

%description
Tizen heme for EFL

%prep
%setup -q

%build
export CFLAGS+=" --fPIC"
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed -Wl,--rpath=/usr/lib"
export TIZEN_VER=2.4


%if "%{?tizen_profile_name}" == "wearable"
    %if "%{?model_build_feature_formfactor}" == "circle"
     export TARGET=wearable-circle
    %else
     export TARGET=wearable
    %endif
    export SIZE=HVGA
%else
 %if "%{?tizen_profile_name}" == "mobile"
    export TARGET=mobile
    export SIZE=HD
 %else
   %if "%{?tizen_profile_name}" == "tv"
    #FIXME: JUST FIX Build ERROR. HAVE TO CHANGE TV-PROFILE.
    export TARGET=tv
    export SIZE=UHD
    %endif
 %endif
%endif

make

%install
export TIZEN_VER=2.4

%if "%{?tizen_profile_name}" == "wearable"
    %if "%{?model_build_feature_formfactor}" == "circle"
     export TARGET=wearable-circle
    %else
     export TARGET=wearable
    %endif
    export SIZE=HVGA
%else
 %if "%{?tizen_profile_name}" == "mobile"
    export TARGET=mobile
    export SIZE=HD
 %else
   %if "%{?tizen_profile_name}" == "tv"
    export TARGET=tv
    export SIZE=UHD
    %endif
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
