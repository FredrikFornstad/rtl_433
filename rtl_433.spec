%global gitversion f3f04c07a998a783325ded2cd782aaa2d3721564

Name:           rtl_433
Version:        20.11.113
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
sed -i 's/\[Unreleased\]/Release %{version}-%{release} (2021-04-14)/' CHANGELOG.md

%build
%cmake3 \
    -DBUILD_TESTING=OFF
make VERBOSE=1 %{?_smp_mflags}


%install
%make_install
install -d %{buildroot}%{_sysconfdir}/rtl_433
mv %{buildroot}/usr/etc/rtl_433/ %{buildroot}%{_sysconfdir}/

%post
if [ $1 -gt 1 ] ; then
systemctl try-restart domoticz &> /dev/null || :
fi

%postun
systemctl try-restart domoticz &> /dev/null || :

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
* Wed Apr 14 2021 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 20.11.113-1
- Updated to latest upstream build

* Sun Apr 11 2021 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 20.11.109-1
- Updated to latest upstream build

* Sat Jun 6 2020 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 20.02.61-3
- Patch so that rtl_433 -V will return build version

* Thu Jun 4 2020 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 20.02.61-2
- Corrected build version
- Restart Domoticz at install and uninstall in case it was running

* Thu Jun 4 2020 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 20.02.f82c025-1
- First version for ClearOS
