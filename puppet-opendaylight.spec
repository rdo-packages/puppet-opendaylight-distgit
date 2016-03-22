Name:			puppet-opendaylight
Version:		XXX
Release:		XXX
Summary:		Puppet module that installs and configures the OpenDaylight SDN controller
License:		BSD-2-Clause

URL:			https://github.com/dfarrell07/puppet-opendaylight

Source0:		https://github.com/dfarrell07/puppet-opendaylight/archive/%{version}.tar.gz

BuildArch:		noarch

Requires:		puppet-stdlib
Requires:		puppet-archive
Requires:		puppet-java
Requires:		puppet >= 2.7.0

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

