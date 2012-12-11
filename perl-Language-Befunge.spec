%define upstream_name    Language-Befunge
%define upstream_version 4.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A generic funge interpreter
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Language/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-aliased
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Class::XSAccessor)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Output)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

%description
This module implements the Funge-98 specifications on a 2D field (also called 
Befunge).  It can also work as a n-funge implementation (3D and more).


%prep
%setup -q -n Language-Befunge-%{upstream_version} 

%build
perl Makefile.PL -n INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/jqbef98
%{perl_vendorlib}/Language
%{_mandir}/man1/jqbef98*
%{_mandir}/man3/*

%changelog
* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 4.130.0-1mdv2011.0
+ Revision: 552378
- update to 4.13

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 4.120.0-1mdv2010.0
+ Revision: 406067
- rebuild using %%perl_convert_version

* Wed Jul 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.12-1mdv2010.0
+ Revision: 393527
- update to new version 4.12

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.11-1mdv2010.0
+ Revision: 383770
- update to new version 4.11

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.10-1mdv2010.0
+ Revision: 370135
- update to new version 4.10

* Tue Jan 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.09-1mdv2009.1
+ Revision: 331699
- update to new version 4.09
- update to new version 4.09

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.08-1mdv2009.1
+ Revision: 305735
- update to new version 4.08

* Sun Nov 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.07-1mdv2009.1
+ Revision: 303807
- update to new version 4.07

* Thu Nov 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.06-1mdv2009.1
+ Revision: 302847
- new version

* Wed Jul 30 2008 Michael Scherer <misc@mandriva.org> 4.04-1mdv2009.0
+ Revision: 255039
- update to new version 4.04

* Sun Jul 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.03-1mdv2009.0
+ Revision: 232108
- update to new version 4.03

* Fri Jul 04 2008 Michael Scherer <misc@mandriva.org> 4.02-3mdv2009.0
+ Revision: 231607
- rebuild

* Fri Jul 04 2008 Michael Scherer <misc@mandriva.org> 4.02-2mdv2009.0
+ Revision: 231606
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 4.02

* Fri Jun 13 2008 Jérôme Quelin <jquelin@mandriva.org> 4.01-1mdv2009.0
+ Revision: 218699
- perl.prov remove modules without caps, so require perl-aliased directly
- some more missing buildrequires
- fix buildrequires
- updated summary & description
- update to new version 4.01

* Fri Jan 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.05-1mdv2008.1
+ Revision: 158140
- update to new version 3.05
- update to new version 3.05

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.04-1mdv2008.1
+ Revision: 152835
- update to new version 3.04

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.02-1mdv2008.1
+ Revision: 113423
- update to new version 3.02

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.01-1mdv2008.1
+ Revision: 105472
- new version

* Sun Jun 10 2007 Michael Scherer <misc@mandriva.org> 2.08-1mdv2008.0
+ Revision: 37835
- update to new version 2.08

* Thu May 24 2007 Michael Scherer <misc@mandriva.org> 2.06-1mdv2008.0
+ Revision: 30813
- Import perl-Language-Befunge



* Thu May 24 2007 Michael Scherer <misc@mandriva.org> 2.06-1mdv2008.0
- First Mandriva package
