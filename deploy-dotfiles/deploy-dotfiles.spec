Name:           deploy-dotfiles
Version:        0.0
Release:        1%{?dist}
Summary:        Deploys dotfiles from Git repository

License:        MIT
URL:            https://copr.fedorainfracloud.org/coprs/tanasovich/post-install
Source0:        deploy-dotfiles.sh

Requires:       bash, git

%description
Prepares home environment for dotfile management and deploys user's configs.

%prep


%build


%install
mkdir -p %{buildroot}%{_bindir}

install -D -m 755 %{SOURCE0} %{buildroot}%{_bindir}/

%post

%files
%{_bindir}/deploy-dotfiles.sh
%license
%doc



%changelog
