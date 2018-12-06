# http://github.com/pelletier/go-toml
%global goipath         github.com/pelletier/go-toml
%global commit          b8b5e7696574464b2f9bf303a7b37781bb52889f

%gometa -i

Name:           golang-github-pelletier-go-toml
Version:        1.0.0
Release:        0.7%{?dist}
Summary:        Go library for the TOML language
# Detected licences
# - MIT/X11 (BSD like) at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml
Patch0:         Fix-go1.10-build-errors.patch

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/BurntSushi/toml)
BuildRequires: golang(gopkg.in/yaml.v2)
BuildRequires: golang(github.com/davecgh/go-spew/spew)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%patch0 -p1

%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.6.gitb8b5e76
- Upload glide files

* Sun Mar 18 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.5.gitb8b5e76
- Bump to b8b5e7696574464b2f9bf303a7b37781bb52889f
  related: #1464882

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.4.git5ccdfb1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.3.git5ccdfb1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.2.git5ccdfb1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.1.git5ccdfb1
- Update to v1.0.0
  resolves: #1464882

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-0.2.git31055c2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 20 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git31055c2
- First package for Fedora
  resolves: #1387203
