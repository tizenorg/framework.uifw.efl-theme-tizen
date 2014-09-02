Name:          efl-theme-tizen-hd
Summary:       Tizen theme files
Version:       1.0.34
Release:       0
Group:         Graphics & UI Framework/Configuration
License:       LGPL-2.1
Source0:       %{name}-%{version}.tar.gz
BuildRequires: edje, edje-bin, embryo, embryo-bin


%description
Tizen HD theme for EFL


%package -n efl-theme-tizen-devel
Summary: Development package


%description -n efl-theme-tizen-devel
Development package


%prep
%setup -q


%build
export CFLAGS+=" --fPIC"
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed -Wl,--rpath=/usr/lib"

%__make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%files
%defattr(-,root,root,-)
%license COPYING
%{_datadir}/elementary/themes/tizen-hd.edj


%files -n efl-theme-tizen-devel
%defattr(-,root,root,-)
%license COPYING
/opt/var/efl-theme-tizen-edc/*
