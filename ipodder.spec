%define	_name	iPodder
Summary:	IPodder - a Media Aggregator
Summary(pl):	IPodder - agregator multimediów
Name:		ipodder
Version:	2.1.1
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/ipodder/%{_name}-linux-%{version}.tar.bz2
# Source0-md5:	6f07e89024244dda633c4e0d50f3febb
Patch0:		%{name}-fixes.patch
URL:		http://ipodder.sourceforge.net/
Requires:	python-libxml2
Requires:	python-wxPython
Requires:	python-xmms
Requires:	python-modules
BuildArch:	noarch
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
%setup -q -n %{_name}-linux
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install -D iPodder.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

cp -f -R * $RPM_BUILD_ROOT%{_datadir}/%{name}
chmod 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/ipodder/*.py
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/*.linux
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/LICENSE

cat << EOF > $RPM_BUILD_ROOT/%{_bindir}/%{name}
#!/bin/sh
cd %{_datadir}/%{name}
exec %{_bindir}/python iPodderGui.py
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog KNOWN-ISSUES NOTES README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}.png
