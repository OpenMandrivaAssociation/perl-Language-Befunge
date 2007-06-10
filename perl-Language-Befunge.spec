%define realname   Language-Befunge

Name:		perl-%{realname}
Version:    2.08
Release:    %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:    A Befunge-98 interpreter
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Language/Language-Befunge-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel

BuildArch: noarch

%description
This module implements the Funge-98 specifications on a 2D field (also called 
Befunge). In particular, be aware that this is not a Trefunge 
implementation (3D).

%prep
%setup -q -n Language-Befunge-%{version} 

%build
%{__perl} Makefile.PL -n INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Language/
%{_mandir}/man3/*