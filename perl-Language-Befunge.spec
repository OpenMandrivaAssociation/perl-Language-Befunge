%define module   Language-Befunge

Name:		perl-%{module}
Version:    4.11
Release:    %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:    A generic funge interpreter
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Language/%{module}-%{version}.tar.gz
BuildRequires:  perl-aliased
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:	perl(Readonly)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Output)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch: noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module implements the Funge-98 specifications on a 2D field (also called 
Befunge).  It can also work as a n-funge implementation (3D and more).


%prep
%setup -q -n Language-Befunge-%{version} 

%build
%{__perl} Makefile.PL -n INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/jqbef98
%{perl_vendorlib}/Language
%{_mandir}/man1/jqbef98*
%{_mandir}/man3/*
