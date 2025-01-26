##############################################################################
#
# To you, dear reader:
#
# If you are a normal user, we recommend not reading further. Its probably not
# the file your looking for.
#
# If you are looking at using this file as a base for your own work, please
# don't. It is a horrible example. Please look elsewhere.
#
# If you are a package maintainer, please read on. We recognize this spec file
# is blasphemous, a terrible abomination, a crime against nature, and more. We
# regret needing to produce it, but had to in order to attract enough users to
# find you. We beseech thee, kind and generous package maintainer, please help
# us mend our wicked ways by joining us and help us produce proper packaging.
# You are our only hope.
#
##############################################################################

%define ARCH %(echo %{_arch} | sed s/aarch64/arm64/)

Summary:    K8s SPIFFE Workload Auth Config
Name:       k8s-spiffe-workload-auth-config
Version:    0.0.8
Release:    1
Group:      Applications/Internet
License:    Apache-2.0
URL:        https://spiffe.io
Source0:    https://github.com/spiffe/k8s-spiffe-workload-auth-config/releases/download/v%{version}/k8s-spiffe-workload-auth-config_Linux_%{ARCH}.tar.gz
Requires:  spiffe-helper

%description
K8s SPIFFE Workload Auth Config

%global _missing_build_ids_terminate_build 0
%global debug_package %{nil}

%prep

%setup -c

%build

%install
mkdir -p "%{buildroot}/usr/bin"
mkdir -p "%{buildroot}/etc/spiffe"
mkdir -p "%{buildroot}/etc/kubernetes"
mkdir -p "%{buildroot}/usr/lib/systemd/system"
cp -a k8s-spiffe-workload-auth-config %{buildroot}/usr/bin
cp -a config/k8s-spiffe-workload-auth-config.env %{buildroot}/etc/spiffe
cp -a config/auth-config.yaml %{buildroot}/etc/kubernetes/
cp -a systemd/k8s-spiffe-workload-auth-config.service %{buildroot}/usr/lib/systemd/system

%clean
rm -rf %{buildroot}

%files
/usr/bin/k8s-spiffe-workload-auth-config
/usr/lib/systemd/system/k8s-spiffe-workload-auth-config.service
%config(noreplace) /etc/spiffe/k8s-spiffe-workload-auth-config.env
%config(noreplace) /etc/kubernetes/auth-config.yaml
