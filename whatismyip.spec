%define _unpackaged_files_terminate_build 0
%define  debug_package %{nil}
Name:	whatismyip
Version: 0.1
Release: 1%{?dist}
Summary: golang daemon which returns ip of visitor

License: GPLv2
URL: https://github.com/Jmainguy/whatismyip
Source0: whatismyip.tar.gz

%description
golang daemon which returns ip of visitor

%prep
%setup -q -n whatismyip
%build
export GOPATH=/usr/src/go
/usr/bin/go build
%install
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/opt/whatismyip
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d/
install -m 0755 $RPM_BUILD_DIR/whatismyip/whatismyip %{buildroot}/usr/sbin
install -m 0755 $RPM_BUILD_DIR/whatismyip/service/whatismyip.sysv %{buildroot}/etc/rc.d/init.d/whatismyip

%files
/usr/sbin/whatismyip
/etc/rc.d/init.d/whatismyip
%dir /opt/whatismyip
%doc

%pre
getent group whatismyip >/dev/null || groupadd -r whatismyip
getent passwd whatismyip >/dev/null || \
    useradd -r -g whatismyip -d /opt/whatismyip -s /sbin/nologin \
    -c "User to run whatismyip" whatismyip
exit 0
%post
/sbin/chkconfig whatismyip on
/etc/init.d/whatismyip restart
chown -R whatismyip:whatismyip /opt/whatismyip

%changelog
* Wed Jun 06 2018 Jonathan Mainguy <jon@soh.re> - 0.1-1
- Initial init

