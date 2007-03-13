Summary: A multithreaded backup utility to include modified files from packages (using RPMdb) and new files.
Name: baubau
Version: 1.0
Release: 0
License: GPL
Source:%{name}-%{version}.tar.bz2
Group: Development/Debuggers
BuildArch: noarch
BuildRoot: %{_builddir}/%{name}-root
URL: http://www.navid.it
Packager: navid@navid.it
%description
zzz is not a real tool, it's an example showing one way
to build an rpm.

%prep

%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
install -m 755 baubau $RPM_BUILD_ROOT/usr/sbin/baubau
install -m 644 baubau.1 $RPM_BUILD_ROOT/usr/man/man1/baubau.1
install -d -m 750 etc-baubau $RPM_BUILD_ROOT/etc/baubau
install -m 640 etc-baubau/exclude_files $RPM_BUILD_ROOT/etc/baubau/exclude_files
install -m 640 etc-baubau/include_files $RPM_BUILD_ROOT/etc/baubau/include_files

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/sbin/baubau
/etc/baubau/include_files
/etc/baubau/exclude_files

%doc
/usr/man/man1/baubau.1.gz

%changelog
* Tue Mar  13 2007  Navid Sheikhol-Eslami <navid@navid.it>
- Initial release
