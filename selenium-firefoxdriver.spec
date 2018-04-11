Summary:	Firefox WebDriver support
Name:		selenium-firefoxdriver
Version:	3.8.0
Release:	1
License:	Distributable
Group:		Applications
Source0:	http://http.debian.net/debian/pool/non-free/s/selenium-firefoxdriver/%{name}_%{version}.orig.tar.gz
# Source0-md5:	e578d75398cd201c6cec5111be51a877
URL:		-
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

%prep
%setup -q -n selenium-%{version}

%build

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
%dir %{_libdir}/firefoxdriver/*6*
%attr(755,root,root) %{_libdir}/firefoxdriver/*6*/x_ignore_nofocus.so
