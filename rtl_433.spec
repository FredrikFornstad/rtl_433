%global gitversion f82c02561dcde055143903d0f65257eb3211d45b
%global gitshortver f82c025

Name:           rtl_433
Version:        20.02.%{gitshortver}
Release:        1%{dist}
Summary:        Turns RTL2832 dongle into a 433.92MHz generic data receiver
License:        GPL-2.0-only
Group:          Productivity/Hamradio/Other
URL:            https://github.com/merbanan/rtl_433.git
Source:         https://github.com/merbanan/rtl_433/archive/%{gitversion}.zip
BuildRequires:  cmake3 rtl-sdr-devel libusbx-devel pkgconfig libtool doxygen

%description
An application using librtlsdr to turn a RTL2832 dongle into a 433.92MHz generic data receiver.

%package devel
Summary:        Turns RTL2832 dongle into a 433.92MHz generic data receiver
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}

%description devel
Turns RTL2832 dongle into a 433.92MHz generic data receiver.

This package contains header files for developing applications that want
to make use of rtl_433.

%prep
%setup -q -n %{name}-%{gitversion}

%build
%cmake3 \
    -DBUILD_TESTING=OFF
make VERBOSE=1 %{?_smp_mflags}


%install
%make_install
install -d %{buildroot}%{_sysconfdir}/rtl_433
mv %{buildroot}/usr/etc/rtl_433/ %{buildroot}%{_sysconfdir}/


%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/rtl_433
%dir %{_sysconfdir}/rtl_433
%config %{_sysconfdir}/rtl_433/*.conf
%{_mandir}/man1/rtl_433.1.gz


%files devel
%{_includedir}/rtl_433.h
%{_includedir}/rtl_433_devices.h


%changelog
* Thu Jun 4 2020 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 20.02.f82c025-1
- First version for ClearOS
