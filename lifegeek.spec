Summary:	"The Life of a Geek" game
Summary(pl.UTF-8):   Gra "The Life of a Geek" (Życie geeka)
Name:		lifegeek
Version:	1.04stable
Release:	1
License:	GPL v2
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/lifegeek/%{name}-%{version}.tar.gz
# Source0-md5:	f5cbd668e36bc7f023eb8268cee1620a
Patch0:		%{name}-path.patch
URL:		http://www.pikecountycomputer.com/lifegeek/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Life of a Geek is very silly console game in which you (a geek)
must keep a computer running until you graduate college. Surf around
on the Internet, battling hackers to gain money and better security
for your box. Drink lots of caffeine to keep yourself awake, since if
you go to sleep, you risk an attack on your computer. Save up money to
take a month-long college course and improve your education, but
remember that paying attention to schoolwork also leaves your computer
open to attack. Find a quick job for a month at places like fast-food
restaurants and grocery stores, but remember again that time away from
your computer leaves it open to attack. Virii may also appear on your
computer, weakening your computer's health points regularly until
cleaned.

%description -l pl.UTF-8
Life of a Geek (Życie geeka) to bardzo głupia gra działająca na
terminalu tekstowym, w której gracz (geek) musi utrzymać działający
komputer do czasu ukończenia uczelni. Musi szperać po Internecie,
walcząc z hakerami, aby zdobyć pieniądze i lepsze bezpieczeństwo dla
maszyny. Musi pić dużo kawy, aby trzymać się na nogach, ponieważ
jeśli zaśnie, może narazić komputer na atak. Trzeba gromadzić
fundusze, aby uczestniczyć w miesięcznych kursach doskonaląc swoje
wykształcenie, ale jednocześnie trzeba pamiętać, że poświęcanie
uwagi nauce także pozostawia komputer otwartym na atak. Gracz musi
znaleźć pracę w miejscach typu restauracje fast-food czy sklepy
spożywcze, ale tu także musi pamiętać, że w czasie nieobecności
komputer pozostaje otwarty na ataki. W komputerze mogą pojawić się
także wirusy, regularnie osłabiając zdrowie komputera do czasu
usunięcia ich.

%prep
%setup -q -n lginst
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_var}/games/%{name}}

install lifegeek $RPM_BUILD_ROOT%{_bindir}
install *.lg     $RPM_BUILD_ROOT%{_datadir}/%{name}
install scores.lgs $RPM_BUILD_ROOT%{_var}/games/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changes readme todo
%attr(2755,root,games) %{_bindir}/*
%attr(775,root,games) %dir %{_var}/games/lifegeek
%attr(664,root,games) %{_var}/games/lifegeek/scores.lgs
%{_datadir}/%{name}
