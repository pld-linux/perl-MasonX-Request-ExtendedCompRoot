#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MasonX
%define	pnam	Request-ExtendedCompRoot
Summary:	MasonX::Request::ExtendedCompRoot - Extend functionality of Mason's component root
#Summary(pl):	
Name:		perl-MasonX-Request-ExtendedCompRoot
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	487b2f30bed5462803330ebaff1701cb
BuildRequires:	perl-devel >= 1:5.8
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(HTML::Mason) >= 1.24
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C<MasonX::Request::ExtendedCompRoot> lets you alter Mason's component
root during the lifetime of any given request or subrequest.

C<MasonX::Request::ExtendedCompRoot> also provides syntactical glue
to enable calling a component in a specific component root that would
otherwise be inaccessible via the usual search path.

# %description -l pl
# TODO

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
%{perl_vendorlib}/%{pdir}/*/*.pm
%{_mandir}/man3/*
