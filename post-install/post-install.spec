Name:           post-install
Version:        0.0
Release:        1%{?dist}
Summary:        Setup my workspace after installation

License:        MIT
URL:            
Source0:        https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
Source1:        https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
Source2:        https://download.docker.com/linux/fedora/docker-ce.repo
Source3:        dnf.conf

BuildRequires:  bash, rpm, rpkg
Requires:       dnf-plugins-core, 
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

rpm --install --root=%{buildroot} %{SOURCE0}
rpm --install --root=%{buildroot} %{SOURCE1}

install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/yum.repos.d/

mkdir -p %{buildroot}%{_sysconfdir}/libdnf5.conf.d

install -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/libdnf5.conf.d/20-user-settings.conf

%post
if [ "$1" -eq "1" ] && [ -f "/etc/yum.repos.d/some-repo.repo" ]; then
    echo "Enabling fedora-cisco-openh264 repository..."
    sed -i 's/enabled=0/enabled=1/' /etc/yum.repos.d/fedora-cisco-openh264.repo
else
    echo "fedora-cisco-openh264 is not enabled!"
fi

%files
/etc/yum.repos.d/rpmfusion-free.repo
/etc/yum.repos.d/rpmfusion-free-updates.repo
/etc/yum.repos.d/rpmfusion-free-updates-testing.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$(rpm -E %fedora)
/etc/yum.repos.d/rpmfusion-nonfree.repo
/etc/yum.repos.d/rpmfusion-nonfree-updates.repo
/etc/yum.repos.d/rpmfusion-nonfree-updates-testing.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-$(rpm -E %fedora)
/etc/yum.repos.d/docker-ce.repo
%license
%doc



%changelog
