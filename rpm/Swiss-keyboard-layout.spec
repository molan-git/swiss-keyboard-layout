Name:       Swiss-keyboard-layout

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}

Summary:    Swiss-keyboard-layout
Version:    1.0
Release:    0
Group:      System/GUI/Other
License:    TBD
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qmake

%description
Swiss  Virtual keyboard for SailfishOS

%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5

%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%files
%defattr(-,root,root,-)
%{_datadir}/maliit/plugins/com/jolla/*
%{_datadir}/maliit/plugins/com/jolla/arrowboard/*
%{_datadir}/maliit/plugins/com/jolla/layouts/*

%post
systemctl-user restart maliit-server.service
