Summary:	"The Life of a Geek" game
Summary(pl):	Gra "The Life of a Geek" (¯ycie geeka)
Name:		lifegeek
Version:	0.337
Release:	1
License:	GPL v2
Group:		Applications/Games
Source0:	http://www.geocities.com/core_dump_000/files/%{name}-%{version}.tar.gz
# Source0-md5:	d74ef629591e9b7fddb736c259d88e9c
Patch0:		%{name}-path.patch
URL:		http://www.geocities.com/core_dump_000/lifegeek.html
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
Life of a Geek (¯ycie geeka) to bardzo g³upia gra dzia³aj±ca na
terminalu tekstowym, w której gracz (geek) musi utrzymaæ dzia³aj±cy
komputer do czasu ukoñczenia uczelni. Musi szperaæ po Internecie,
walcz±c z hakerami, aby zdobyæ pieni±dze i lepsze bezpieczeñstwo dla
maszyny. Musi piæ du¿o kawy, aby trzymaæ siê na nogach, poniewa¿
je¶li za¶nie, mo¿e naraziæ komputer na atak. Trzeba gromadziæ
fundusze, aby uczestniczyæ w miesiêcznych kursach doskonal±c swoje
wykszta³cenie, ale jednocze¶nie trzeba pamiêtaæ, ¿e po¶wiêcanie
uwagi nauce tak¿e pozostawia komputer otwartym na atak. Gracz musi
znale¼æ pracê w miejscach typu restauracje fast-food czy sklepy
spo¿ywcze, ale tu tak¿e musi pamiêtaæ, ¿e w czasie nieobecno¶ci
komputer pozostaje otwarty na ataki. W komputerze mog± pojawiæ siê
tak¿e wirusy, regularnie os³abiaj±c zdrowie komputera do czasu
usuniêcia ich.

%prep
%setup -q -n %{name}
%patch -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install lifegeek $RPM_BUILD_ROOT%{_bindir}
install *.lg     $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG INSTALL LIFEGEEK_VERSION NOTE NOT_FINISHED_YET TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
