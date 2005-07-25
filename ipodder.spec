# TODO: Name vs spec filename
Summary:	IPodder - a Media Aggregator
Summary(pl):	IPodder - agregator multimediów
Name:		iPodder
Version:	2.0
Release:	0.rc4.1
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/ipodder/%{name}-linux-%{version}-rc4.tar.bz2
Source1:	%{name}.sh
Source10:	%{name}-16.png
Source11:	%{name}-32.png
Source12:	%{name}-48.png
URL:		http://ipodder.sourceforge.net/
Requires:	python-libxml2
Requires:	python-wxPython
Requires:	python-xmms
Requires:	pythonlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
iPodder jest technicznie "agregatorem multimediów" - programem
umo¿liwiaj±cym wybór i ¶ci±ganie plików d¼wiêkowych z dowolnego
miejsca w Internecie na pulpit.

iPodder czyni ten proces ³atwym pomagaj±c wybraæ pliki d¼wiêkowe
spo¶ród tysiêcy ¼róde³ d¼wiêku w sieci i ¶ci±gaj±c te pliki na
komputer. Po wybraniu ¼ród³a lub miejsca ¶ci±gnie pliki automatycznie
w podanym czasie, a pliki bêd± oczekiwa³y na komputerze, przez co nie
trzeba spêdzaæ du¿o czasu na rêcznym wybieraniu i oczekiwaniu na
¶ci±gniêcie. Mo¿na odtwarzaæ wybrane pliki d¼wiêkowe przy u¿yciu
iTunes lub innego programu w stylu "szafy graj±cej", albo wczytywaæ je
do iPoda czy innego przeno¶nego odtwarzacza plików multimedialnych w
celu odtworzenia w dowolnej chwili.

%prep
%setup -q -n %{name}-linux

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

install %{SOURCE1} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -f -R * $RPM_BUILD_ROOT%{_datadir}/%{name}
chmod 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/ipodder/*.py
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/*.linux
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/LICENSE

#menus
#install -d $RPM_BUILD_ROOT/%{_menudir}
#cat <<EOF >$RPM_BUILD_ROOT/%{_menudir}/%{name}
#?package(%{name}):command="%{_bindir}/%{name}" \
#                  icon=%{name}.png \
#                  needs="x11" \
#                  section="Multimedia/Sound" \
#                  title="Ipodder"\
#                  longtitle="%{summary}"
#EOF

#install %{SOURCE10} -D $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png
install %{SOURCE11} -D $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
#install %{SOURCE12} -D $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.linux NOTES.linux LICENSE Changelog.linux TODO.linux
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}.png
