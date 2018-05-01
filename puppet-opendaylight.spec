%{!?upstream_version: %global upstream_version %{commit}}
%if 0%{?dlrn}
%define upstream_name puppet-opendaylight
%else
%define upstream_name integration-packaging-puppet-opendaylight
%endif
%global commit 38977efdb9d7a585a1748cf6122040776ed542f1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

%{?dlrn: %global tarsources %{sname}-%{upstream_version}}
%{!?dlrn: %global tarsources package}


Name:           puppet-opendaylight
Version:        8.1.2
Release:        1%{?alphatag}%{?dist}
Summary:        Puppet module that installs and configures the OpenDaylight SDN controller
License:        BSD-2-Clause

URL:            https://github.com/opendaylight/%{upstream_name}

Source0:        https://github.com/opendaylight/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

# patches_base=38977efdb9d7a585a1748cf6122040776ed542f1

BuildArch:      noarch

Requires:       puppet-stdlib
#Requires:       puppet-archive
Requires:       puppet-java
Requires:       puppet >= 2.7.0

%description
Puppet module that installs and configures the OpenDaylight SDN controller

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
* Tue May 01 2018 Jon Schlueter <jschluet@redhat.com> 8.1.2-1.38977efgit
- Update to 8.1.2 (38977efdb9d7a585a1748cf6122040776ed542f1)

* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 7.0.0-1.d3b32a4git
- Update to post 7.0.0 (d3b32a4d44b9d0f345d845790737714b10d76d05)



