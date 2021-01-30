Summary:	Firefox WebDriver support
Summary(pl.UTF-8):	Obsługa interfejsu WebDriver dla Firefoksa
Name:		selenium-firefoxdriver
Version:	3.8.0
Release:	1
License:	Distributable
Group:		Applications
Source0:	http://http.debian.net/debian/pool/non-free/s/selenium-firefoxdriver/%{name}_%{version}.orig.tar.gz
# Source0-md5:	e578d75398cd201c6cec5111be51a877
Obsoletes:	firefox-addon-selenium < 3.11.0-5
Obsoletes:	iceweasel-addon-selenium < 2.47.1-5
Obsoletes:	python-selenium-iceweasel-addon < 2.1
ExclusiveArch:	%{x8664} %{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebDriver is designed to provide a simpler, more concise programming
interface in addition to addressing some limitations in the
Selenium-RC API. Selenium-WebDriver was developed to better support
dynamic web pages where elements of a page may change without the page
itself being reloaded. WebDriver's goal is to supply a well-designed
object-oriented API that provides improved support for modern advanced
web-app testing problems.

%description -l pl.UTF-8
WebDriver to interfejs zaprojektowany jako prostszy, bardziej zwięzły,
ponadto rozwiązujący niektóre ograniczenia API Selenium-RC.
Selenium-WebDriver powstał, aby lepiej obsługiwać dynamiczne strony
WWW, gdzie elementy strony mogą się zmieniać bez przeładowania samej
strony. Celem WebDrivera jest dostarczenie dobrze zaprojektowanego,
zorientowanego obiektowo API zapewniającego lepsze wsparcie dla
zagadnień związanych z testowaniem bardziej nowoczesnych,
zaawansowanych aplikacji WWW.

%prep
%setup -q -n selenium-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/firefoxdriver

cp -p selenium/webdriver/firefox/webdriver.xpi $RPM_BUILD_ROOT%{_datadir}/firefoxdriver
%ifarch %{x8664}
install -d $RPM_BUILD_ROOT%{_libdir}/firefoxdriver/amd64
cp -p selenium/webdriver/firefox/amd64/x_ignore_nofocus.so $RPM_BUILD_ROOT%{_libdir}/firefoxdriver/amd64/
%endif
%ifarch %{ix86}
install -d $RPM_BUILD_ROOT%{_libdir}/firefoxdriver/x86
cp -p selenium/webdriver/firefox/x86/x_ignore_nofocus.so $RPM_BUILD_ROOT%{_libdir}/firefoxdriver/x86/
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README.rst
%{_datadir}/firefoxdriver
%dir %{_libdir}/firefoxdriver
%ifarch %{x8664}
%dir %{_libdir}/firefoxdriver/amd64
%attr(755,root,root) %{_libdir}/firefoxdriver/amd64/x_ignore_nofocus.so
%endif
%ifarch %{ix86}
%dir %{_libdir}/firefoxdriver/x86
%attr(755,root,root) %{_libdir}/firefoxdriver/x86/x_ignore_nofocus.so
%endif
