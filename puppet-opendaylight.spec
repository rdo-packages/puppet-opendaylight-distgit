%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-opendaylight
%global commit 3768d5e01df2482a91a8815ca36604800bee1400
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-opendaylight
Version:        4.1.0
Release:        1%{?alphatag}%{?dist}
Summary:        Puppet module that installs and configures the OpenDaylight SDN controller
License:        BSD-2-Clause

URL:            https://github.com/opendaylight/integration-packaging-puppet-opendaylight

Source0:        https://github.com/opendaylight/integration-packaging-puppet-opendaylight/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 4.1.0-1.3768d5egit
- Pike update 4.1.0 (3768d5e01df2482a91a8815ca36604800bee1400)


