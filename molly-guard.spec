Summary:	protects machines from accidental shutdowns/reboots
Name:		molly-guard
Version:	0.4.5
Release:	1
License:	Artistic Licence 2.0
Group:		Applications/System
Source0:	http://ftp.debian.org/debian/pool/main/m/molly-guard/%{name}_%{version}.orig.tar.gz
# Source0-md5:	bee1573a8740d5dcc25302490b18213a
Source1:	%{name}.sh
Source2:	%{name}.csh
Patch1:		docbook.patch
Patch2:		doubleslashes.patch
URL:		http://ftp.debian.org/debian/pool/main/m/molly-guard
BuildRequires:	docbook-style-xsl
BuildRequires:	libxslt-progs
BuildRequires:	sed >= 4.0
Requires:	procps
Requires:	rc-scripts >= 0.4.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package installs a shell script that overrides the existing
shutdown/reboot/halt/poweroff commands and first runs a set of
scripts, which all have to exit successfully, before molly-guard
invokes the real command.

One of the scripts checks for existing SSH sessions. If any of the
four commands are called interactively over an SSH session, the shell
script prompts you to enter the name of the host you wish to shut
down. This should adequately prevent you from accidental shutdowns and
reboots.

This shell script passes through the commands to the respective
binaries in /sbin and should thus not get in the way if called
non-interactively, or locally.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%{__sed} -i -e '/install/ s/-oroot -[og]root//' Makefile
%{__sed} -i -e '/chown/ s/root.root/%(id -un)/' Makefile

%build
%{__make} shutdown \
	etc_prefix=/ \
	prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} install \
	etc_prefix=/ \
	prefix=%{_prefix} \
	DEST=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/profile.d
cp -p %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/etc/profile.d

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%config(noreplace) %verify(not md5 mtime size) /etc/profile.d/molly-guard.csh
%config(noreplace) %verify(not md5 mtime size) /etc/profile.d/molly-guard.sh
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/run.d
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/run.d/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/rc
%attr(755,root,root) %{_sbindir}/halt
%attr(755,root,root) %{_sbindir}/poweroff
%attr(755,root,root) %{_sbindir}/reboot
%attr(755,root,root) %{_sbindir}/shutdown
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/shutdown
%{_mandir}/man8/%{name}.8*
