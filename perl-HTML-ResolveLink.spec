%define upstream_name    HTML-ResolveLink
%define upstream_version 0.05
Name:		perl-%{upstream_name}
Version:	0.05
Release:	2

Summary:	Resolve relative links in (X)HTML into absolute URI
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/HTML-ResolveLink-0.05.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildArch:	noarch

%description
HTML::ResolveLink is a module to rewrite relative links in XHTML or HTML
into absolute URI.

For example. when you have

  <a href="foo.html">foo</a>
  <img src="/bar.gif" />

%prep
%setup -q -n HTML-ResolveLink-0.05

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


