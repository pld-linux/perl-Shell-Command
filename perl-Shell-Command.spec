#
# Conditional build:
%bcond_without	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Shell
%define	pnam	Command
Summary:	Shell::Command - cross-platform functions emulating common shell commands
Summary(pl.UTF-8):	Shell::Command - niezależne od platformy funkcje emulujące typowe polecania powłoki
Name:		perl-Shell-Command
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d3e42d3cb2ea325dc1059bb8706b47bb
URL:		http://search.cpan.org/dist/Shell-Command/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thin wrapper around ExtUtils::Command. See ExtUtils::Command for
a description of available commands.

%description -l pl.UTF-8
Mała nakładka na moduł ExtUtils::Command. Opis dostępnych
poleceń w dokumentacji do ExtUtils::Command.

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
%{perl_vendorlib}/Shell/Command.pm
%{_mandir}/man?/*
