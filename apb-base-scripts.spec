%if 0%{?copr}
%define build_timestamp .%(date +"%Y%m%d%H%M%%S")
%else
%define build_timestamp %{nil}
%endif

Name: apb-base-scripts
Version:	1.1.0
Release:	1%{build_timestamp}%{?dist}
Summary:	Scripts for the apb-base container image

License:	ASL 2.0
URL:		https://github.com/fusor/apb-examples
Source0:	https://github.com/fusor/apb-examples/archive/%{name}-%{version}.tar.gz
BuildArch:  noarch

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/apb-secrets
install -m 755 files/usr/bin/bind-init %{buildroot}%{_bindir}
install -m 755 files/usr/bin/broker-bind-creds %{buildroot}%{_bindir}
install -m 755 files/usr/bin/test-retrieval-init %{buildroot}%{_bindir}
install -m 755 files/usr/bin/test-retrieval %{buildroot}%{_bindir}
install -m 755 files/usr/bin/entrypoint.sh %{buildroot}%{_bindir}
install -m 755 files/usr/bin/oc-login.sh %{buildroot}%{_bindir}

%files
%doc
%{_bindir}/test-retrieval-init
%{_bindir}/test-retrieval
%{_bindir}/bind-init
%{_bindir}/broker-bind-creds
%{_bindir}/entrypoint.sh
%{_bindir}/oc-login.sh
%dir %{_sysconfdir}/apb-secrets

%changelog
* Tue Nov 07 2017 Jason Montleon <jmontleo@redhat.com> 1.0.5-1
- Bug 1510299 add missing /etc/apb-secrets (jmontleo@redhat.com)
- Fixed link to ansible-asb-modules for canary (cchase@redhat.com)
- Adding Apache License Version 2.0 file (matzew@apache.org)
- update tito releasers (jmontleo@redhat.com)

* Fri Oct 13 2017 Jason Montleon <jmontleo@redhat.com> 1.0.4-1
- 1498185 - Removed version label from apb-base (dymurray@redhat.com)

* Tue Sep 19 2017 Jason Montleon <jmontleo@redhat.com> 1.0.3-1
- new package built with tito

* Fri Aug 18 2017 Jason Montleon <jmontleo@redhat.com> 1.0.2-1
- apply role path on the command line (#115) (jmontleo@redhat.com)
- Fix canary build and stop overwriting files rpm RPM's in latest (#114)
  (jmontleo@redhat.com)

* Fri Aug 18 2017 Jason Montleon <jmontleo@redhat.com> 1.0.1-1
- new package built with tito

