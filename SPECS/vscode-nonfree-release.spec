Name:           vscode-nonfree-release
Version:        0.0
Release:        1%{?dist}
Summary:        Provides VS Code repository and keys

License:        
URL:            https://code.visualstudio.com
Source0:        vscode.repo
Source1:        https://packages.microsoft.com/keys/microsoft.asc

%description


%prep


%install
mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d
mkdir -p %{buildroot}%{_sysconfdir}/pki/rpm-gpg

install -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-vscode-nonfree

%files
/etc/yum.repos.d/vscode.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-vscode-nonfree
%license
%doc



%changelog
