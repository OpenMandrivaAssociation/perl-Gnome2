%define module	Gnome2
%define upstream_version 1.042

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	12

Summary:	Perl module for the gnome2-2.x core libraries
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
# http://sourceforge.net/project/showfiles.php?group_id=64773&package_id=91219
Source0:	%{module}-%{upstream_version}.tar.bz2

BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Gnome2::VFS)
BuildRequires:	perl(Gnome2::Canvas)
BuildRequires:	perl(Gtk2)
Buildrequires:	perl-devel

Conflicts:	drakxtools < 9.1-15mdk
Requires:	perl(Gtk2) >= 1.00

%description
This module provides perl access to GNOME-2.x core libraries.

GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window manager
for the X Window System. GNOME is similar in purpose and scope to CDE and KDE,
but GNOME (like KDE) is based completely on Open Source software.

GNOME libraries provide extra widgets on top of the gtk+ toolkit.


%prep
%setup -q -n %{module}-%{upstream_version}
find -type d -name CVS | rm -rf 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc AUTHORS LICENSE examples/*
%{_mandir}/*/*
%{perl_vendorarch}/%{module}
%{perl_vendorarch}/%{module}.pm
%{perl_vendorarch}/auto/*


%changelog
* Thu Feb 02 2012 Per √òyvind Karlsen <peroyvind@mandriva.org> 1.42.0-12
+ Revision: 770562
- clean up spec
- use pkgconfig() deps
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for perl-5.14.2
    - rebuilt for perl-5.14.x

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.42.0-9
+ Revision: 702772
- rebuilt against libpng-1.5.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.42.0-8
+ Revision: 667180
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.42.0-7mdv2011.0
+ Revision: 564476
- rebuild for perl 5.12.1

* Sun Feb 14 2010 J√©r√¥me Quelin <jquelin@mandriva.org> 1.42.0-6mdv2011.0
+ Revision: 505732
- rebuild using %%perl_convert_version

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.042-5mdv2010.0
+ Revision: 426448
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.042-4mdv2009.0
+ Revision: 223770
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.042-3mdv2008.1
+ Revision: 152646
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Aug 13 2007 Thierry Vignaud <tv@mandriva.org> 1.042-1mdv2008.0
+ Revision: 62755
- new release

* Tue Jun 26 2007 Thierry Vignaud <tv@mandriva.org> 1.041-2mdv2008.0
+ Revision: 44599
- rebuild


* Thu Jan 04 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.041-1mdv2007.0
+ Revision: 104202
- new release

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Gnome2

* Thu Mar 16 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.040-1mdk
- new release

* Tue Jan 03 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.030-1mdk
- new release

* Tue Oct 11 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 1.023-4mdk
- Fix previous mistake

* Fri Sep 30 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 1.023-3mdk
- fix buildrequires

* Sat Jul 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.023-2mdk
- fix build on x86_64

* Fri Jun 24 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.023-1mdk
- new release

* Wed Jun 08 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.022-1mdk
- new release

* Tue Feb 08 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.020-2mdk
- rebuilt for new perl

* Fri Sep 17 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.020-1mdk
- new release

* Tue Aug 31 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.014-1mdk
- new release

* Sat Aug 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.013-1mdk
- new release

* Tue Aug 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.012-1mdk
- new release

* Wed Jun 30 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.011-1mdk
- new release

* Fri Jun 04 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.010-1mdk
- new release
- now Gnome2 {Build,}requires Gnome2-Canvas

* Wed Mar 31 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.00-1mdk
- new release

* Sat Jan 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.90-1mdk
- new release

