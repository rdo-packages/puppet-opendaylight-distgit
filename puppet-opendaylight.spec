%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name integration-packaging-puppet-opendaylight
%global commit bbe7ce51fd7d2d2ce6ed79d25567b1de570eb9fb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-opendaylight
Version:        8.4.3
Release:        1%{?alphatag}%{?dist}
Summary:        Puppet module that installs and configures the OpenDaylight SDN controller
License:        BSD-2-Clause

URL:            https://github.com/opendaylight/integration-packaging-puppet-opendaylight

Source0:        https://github.com/opendaylight/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
#Requires:       puppet-archive
Requires:       puppet-java
Requires:       puppet >= 2.7.0

%description
Puppet module that installs and configures the OpenDaylight SDN controller

%prep
%setup -q -n %{name}-%{upstream_version}

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
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 8.4.3-1.bbe7ce5git
- Update to post 8.4.3 (bbe7ce51fd7d2d2ce6ed79d25567b1de570eb9fb)



