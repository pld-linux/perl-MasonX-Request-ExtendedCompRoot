#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MasonX
%define		pnam	Request-ExtendedCompRoot
Summary:	MasonX::Request::ExtendedCompRoot - extend functionality of Mason's component root
Summary(pl):	MasonX::Request::ExtendedCompRoot - rozszerzanie funkcjonalno¶ci korzenia komponentów Masona
Name:		perl-MasonX-Request-ExtendedCompRoot
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	487b2f30bed5462803330ebaff1701cb
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Mason >= 1.24
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MasonX::Request::ExtendedCompRoot lets you alter Mason's component
root during the lifetime of any given request or subrequest.

MasonX::Request::ExtendedCompRoot also provides syntactical glue to
enable calling a component in a specific component root that would
otherwise be inaccessible via the usual search path.

%description -l pl
MasonX::Request::ExtendedCompRoot umo¿liwia modyfikowanie korzenia
komponentów Masona w czasie istnienia dowolnych ¿±dañ lub pod¿±dañ.

MasonX::Request::ExtendedCompRoot dostarcza tak¿e "klej sk³adniowy"
umo¿liwiaj±cy wywo³ywanie komponentu w takim korzeniu komponentów,
który bez tego by³by niedostêpny w normalnej ¶cie¿ce wyszukiwañ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MasonX/*/*.pm
%{_mandir}/man3/*
