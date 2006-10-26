Summary:	"The Life of a Geek" game
Summary(pl):	Gra "The Life of a Geek" (�ycie geeka)
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

%description -l pl
Life of a Geek (�ycie geeka) to bardzo g�upia gra dzia�aj�ca na
terminalu tekstowym, w kt�rej gracz (geek) musi utrzyma� dzia�aj�cy
komputer do czasu uko�czenia uczelni. Musi szpera� po Internecie,
walcz�c z hakerami, aby zdoby� pieni�dze i lepsze bezpiecze�stwo dla
maszyny. Musi pi� du�o kawy, aby trzyma� si� na nogach, poniewa�
je�li za�nie, mo�e narazi� komputer na atak. Trzeba gromadzi�
fundusze, aby uczestniczy� w miesi�cznych kursach doskonal�c swoje
wykszta�cenie, ale jednocze�nie trzeba pami�ta�, �e po�wi�canie
uwagi nauce tak�e pozostawia komputer otwartym na atak. Gracz musi
znale�� prac� w miejscach typu restauracje fast-food czy sklepy
spo�ywcze, ale tu tak�e musi pami�ta�, �e w czasie nieobecno�ci
komputer pozostaje otwarty na ataki. W komputerze mog� pojawi� si�
tak�e wirusy, regularnie os�abiaj�c zdrowie komputera do czasu
usuni�cia ich.

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
