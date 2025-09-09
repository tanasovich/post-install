Name:           docker-ce-free-release
Version:        0.0
Release:        1%{?dist}
Summary:        Provides Docker CE repository

License:        Apache License 2.0
URL:            https://www.docker.com
Source0:        https://download.docker.com/linux/fedora/docker-ce.repo

BuildRequires:  
Requires:       

%description


%prep


%build


%install
mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d

install -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/


%files
/etc/yum.repos.d/docker-ce.repo
%license
%doc



%changelog
