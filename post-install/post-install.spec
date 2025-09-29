Name:           post-install
Version:        0.0
Release:        1%{?dist}
Summary:        Setup my workspace after installation

License:        MIT
URL:            https://copr.fedorainfracloud.org/coprs/tanasovich/post-install
Source0:        https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-%{fedora}.noarch.rpm
Source1:        dnf.conf

Requires:       dnf-plugins-core
Requires:       vscode-nonfree-release, docker-ce-free-release
Requires:       rpmfusion-free-release, rpmfusion-nonfree-release
Recommends:     arc-theme, fira-code-fonts, julietaula-montserrat-fonts
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
mkdir -p %{buildroot}%{_sysconfdir}/dnf/libdnf5.conf.d

install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/dnf/libdnf5.conf.d/20-user-settings.conf

%post
if [ "$1" -eq "1" ] && [ -f "/etc/yum.repos.d/fedora-cisco-openh264.repo" ]; then
    echo "Enabling fedora-cisco-openh264 repository..."
    sed -i 's/enabled=0/enabled=1/' /etc/yum.repos.d/fedora-cisco-openh264.repo
else
    echo "fedora-cisco-openh264 is not enabled!"
fi

%files
/etc/dnf/libdnf5.conf.d/20-user-settings.conf
%license
%doc



%changelog
