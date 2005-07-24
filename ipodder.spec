%define name iPodder
%define version 2.0
%define release 0.rc4.1%{_my_ext}
%define __libtoolize /bin/true
%define __cputoolize /bin/true
Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	IPodder is a Media Aggregator
Vendor:		%{vendor}
License:	GPL
URL:		http://ipodder.sourceforge.net/
Group:		Sound
######		Unknown group!
Source0:	http://dl.sourceforge.net/ipodder/%{name}-linux-%{version}-rc4.tar.bz2
Source1:	%{name}.sh
Source10:	%{name}-16.png
Source11:	%{name}-32.png
Source12:	%{name}-48.png
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	wxPythonGTK
Requires:	pyxmms pythonlib libxml2-python

%description
iPodder is technically a "Media Aggregator," a program that allows you
to select and download audio files from anywhere on the Internet to
your desktop.

iPodder makes the process easy by helping you select audio files from
among the thousands of audio sources on the web and downloading those
files to your computer. Once you select a feed or location, it will
download those files automatically at times you specify and have the
files waiting for you on your computer, so you don't have to spend a
lot of time manually selecting and waiting for downloads. You can play
your selected audio files using iTunes or other "jukebox" software, or
load them on to your iPod or other portable digital media player to
play anytime you want.

%prep
%setup -q -n %{name}-linux

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/%{_datadir}/%{name}
install %{SOURCE1} -D $RPM_BUILD_ROOT/%{_bindir}/%{name}
cp -f -R * $RPM_BUILD_ROOT/%{_datadir}/%{name}
chmod 755 $RPM_BUILD_ROOT/%{_datadir}/%{name}/ipodder/*.py
rm -f $RPM_BUILD_ROOT/%{_datadir}/%{name}/*.linux
rm -f $RPM_BUILD_ROOT/%{_datadir}/%{name}/LICENSE

#menus
install -d $RPM_BUILD_ROOT/%{_menudir}
cat <<EOF >$RPM_BUILD_ROOT/%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/%{name}" \
                  icon=%{name}.png \
                  needs="x11" \
                  section="Multimedia/Sound" \
                  title="Ipodder"\
                  longtitle="%{summary}"
EOF

install %{SOURCE10} -D $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png
install %{SOURCE11} -D $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
install %{SOURCE12} -D $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.linux NOTES.linux LICENSE Changelog.linux TODO.linux
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}/*
%_menudir/%{name}
%{_iconsdir}/%{name}.png
%_liconsdir/%{name}.png
%_miconsdir/%{name}.png

%post
%{update_menus}

%postun
%{clean_menus}
