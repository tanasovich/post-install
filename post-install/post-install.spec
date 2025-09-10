Name:           post-install
Version:        0.0
Release:        1%{?dist}
Summary:        Setup my workspace after installation

License:        MIT
URL:            https://copr.fedorainfracloud.org/coprs/tanasovich/post-install
Source0:        https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-%{fedora}.noarch.rpm
Source1:        https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-%{fedora}.noarch.rpm
Source2:        dnf.conf

Requires:       dnf-plugins-core, vscode-nonfree-release, docker-ce-free-release
Recommends:     arc-theme, fira-code-fonts
Recommends:     firefox, thunderbird, telegram-desktop, transmission
Recommends:     code
Recommends:     libreoffice
Recommends:     gimp, inkscape
Recommends:     vlc

%description
Add cool repos, install configs, speed up DNF, import wallpapers.
Automating routing post-installation configuration process.

%prep


%build


%install
mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d
mkdir -p %{buildroot}%{_sysconfdir}/pki/rpm-gpg

install -D -m 644 %{SOURCE0} %{buildroot}/tmp/rpmfusion-free-release.rpm
install -D -m 644 %{SOURCE1} %{buildroot}/tmp/rpmfusion-nonfree-release.rpm

rpm2cpio %{buildroot}/tmp/rpmfusion-free-release.rpm | cpio -idv --quiet
rpm2cpio %{buildroot}/tmp/rpmfusion-nonfree-release.rpm | cpio -idv --quiet

mkdir -p %{buildroot}%{_sysconfdir}/libdnf5.conf.d

install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/dnf/libdnf5.conf.d/20-user-settings.conf

%post
if [ "$1" -eq "1" ] && [ -f "/etc/yum.repos.d/fedora-cisco-openh264.repo" ]; then
    echo "Enabling fedora-cisco-openh264 repository..."
    sed -i 's/enabled=0/enabled=1/' /etc/yum.repos.d/fedora-cisco-openh264.repo
else
    echo "fedora-cisco-openh264 is not enabled!"
fi

%files
/etc/yum.repos.d/rpmfusion-free.repo
/etc/yum.repos.d/rpmfusion-free-updates.repo
/etc/yum.repos.d/rpmfusion-free-updates-testing.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-2020
/etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-%{fedora}
/etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-%{eval:%{fedora} + 1}
/etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-%{eval:%{fedora} + 2}
/etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-latest
/etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-rawhide
/etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-2020
/etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-%{fedora}
/etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-%{eval:%{fedora} + 1}
/etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-%{eval:%{fedora} + 2}
/etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-latest
/etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-rawhide
/etc/yum.repos.d/rpmfusion-nonfree.repo
/etc/yum.repos.d/rpmfusion-nonfree-updates.repo
/etc/yum.repos.d/rpmfusion-nonfree-updates-testing.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-%{fedora}
/etc/dnf/libdnf5.conf.d/20-user-settings.conf
%license
%doc



%changelog
