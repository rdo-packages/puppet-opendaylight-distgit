%define upstream_name puppet-opendaylight


Name:           puppet-opendaylight
Version:        4.0.0
Release:        1%{?dist}
Summary:        Puppet module that installs and configures the OpenDaylight SDN controller
License:        BSD-2-Clause

URL:            https://github.com/dfarrell07/puppet-opendaylight

Source0:        https://github.com/dfarrell07/%{upstream_name}/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
#Requires:       puppet-archive
Requires:       puppet-java
Requires:       puppet >= 2.7.0

%description
Puppet module that installs and configures the OpenDaylight SDN controller

%prep
%setup -q -n %{name}-%{version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/opendaylight/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/opendaylight/



%files
%{_datadir}/openstack-puppet/modules/opendaylight/


%changelog
* Tue Apr 11 2017 Jon Schlueter <jschluet@redhat.com> 4.0.0-1
- Update to 4.0.0

* Thu Feb 09 2017 Alfredo Moralejo <amoralej@redhat.com> 3.7.0-2.7261876git
- Ocata update 3.7.0 (726187652054ad46c7ff980f2fe9e56c9ad5b3b5)

