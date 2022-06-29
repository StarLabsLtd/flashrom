Summary: flashrom
Name: flashrom
Version: 1.2
Release: 9%{?dist}
License: GPLv2
URL: https://github.com/StarLabsLtd/flashrom.git
Source: https://github.com/StarLabsLtd/flashrom/archive/refs/tags/%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc

%description
flashrom is a utility for detecting, reading, writing, verifying and erasing
flash chips. It is often used to flash BIOS/EFI/coreboot/firmware images
in-system using a supported mainboard, but it also supports flashing of network
cards (NICs), SATA controller cards, and other external devices which can
program flash chips.

%prep
tar -C %{_builddir} -xf %{_sourcedir}/coreboot-%{version}.tar.xz
mv %{_builddir}/coreboot-%{version} %{_builddir}/flashrom-%{version}
cd %{_builddir}/flashrom-%{version}
DESTDIR=%{buildroot} PREFIX=%{_prefix} make
install -m755 flashrom %{buildroot}/%{_sbindir}/flashrom
install -m644 flashrom.8 %{buildroot}/usr/share/man/man8


%files
%{_sbindir}/%{name}

%changelog
* Tue Jul 5 2022 Sean Rhodes <sean@starlabs.systems> 4.17
- initial spec file
