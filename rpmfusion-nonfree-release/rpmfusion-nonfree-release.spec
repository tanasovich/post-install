#global _repo free
%global _repo nonfree
%global israwhide 0

Name:           rpmfusion-%{_repo}-release
Version:        41
Release:        1%{?dist}
Summary:        RPM Fusion (%{_repo}) Repository Configuration

License:        BSD
URL:            http://rpmfusion.org
Source0:        https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-%{version}.noarch.rpm
BuildArch:      noarch

%description
RPM Fusion %{_repo} package repository files for yum and dnf
along with gpg public keys


%prep
echo "Nothing to prep"

%build
echo "Nothing to build"

%install
mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d
mkdir -p %{buildroot}%{_sysconfdir}/pki/rpm-gpg
mkdir -p %{buildroot}/tmp

install -D -m 644 %{SOURCE0} %{buildroot}/tmp/rpmfusion-nonfree-release.rpm

rpm2cpio %{buildroot}/tmp/rpmfusion-nonfree-release.rpm | cpio -idv --quiet -D %{buildroot}

rm -r %{buildroot}/tmp

%files
%config %{_sysconfdir}/pki/rpm-gpg/*
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmfusion-%{_repo}.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmfusion-%{_repo}-updates*.repo

%changelog
