Summary:	"The Life of a Geek" game
Summary(pl):	Gra "The Life of a Geek"
Name:		lifegeek
Version:	0.2
Release:	0.1
License:	GPL
Group:		Applications/Games
Source0:	http://www.geocities.com/core_dump_000/files/%{name}-%{version}.tar.gz
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
...

%prep
%setup -q -n lifegeek

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}/
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp lifegeek $RPM_BUILD_ROOT/%{_bindir}
cp CHANGELOG LICENSE LIFEGEEK_VERSION NOTE TODO $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE LIFEGEEK_VERSION NOTE TODO
%attr(755,root,root) %{_bindir}/*
