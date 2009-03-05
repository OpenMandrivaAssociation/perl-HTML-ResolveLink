%define realname   HTML-ResolveLink
%define version    0.05
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Resolve relative links in (X)HTML into absolute URI
Source:     http://www.cpan.org/modules/by-module/HTML/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(HTML::Parser)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildArch: noarch

%description
HTML::ResolveLink is a module to rewrite relative links in XHTML or HTML
into absolute URI.

For example. when you have

  <a href="foo.html">foo</a>
  <img src="/bar.gif" />

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*
