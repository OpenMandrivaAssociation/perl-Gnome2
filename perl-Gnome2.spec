%define module Gnome2

Summary: Perl module for the gnome2-2.x core libraries
Name:    perl-%module
Version: 1.042
Release: %mkrel 1
License: GPL or Artistic
Group:   Development/GNOME and GTK+
# http://sourceforge.net/project/showfiles.php?group_id=64773&package_id=91219
Source:  %module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/
BuildRequires: gnomeui2-devel 
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-Gnome2-VFS >= 1.00 
BuildRequires: perl-Gtk2 => 1.00
BuildRequires: perl-Gnome2-Canvas
Buildrequires: perl-devel
BuildRequires: perl-ExtUtils-PkgConfig
Requires: perl-Gtk2 >= 1.00
Conflicts: drakxtools < 9.1-15mdk

%description
This module provides perl access to GNOME-2.x core libraries.

GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window manager
for the X Window System. GNOME is similar in purpose and scope to CDE and KDE,
but GNOME (like KDE) is based completely on Open Source software.

GNOME libraries provide extra widgets on top of the gtk+ toolkit.


%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
export GTK2_PERL_CFLAGS="$RPM_OPT_FLAGS"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc AUTHORS LICENSE examples/*
%{_mandir}/*/*
%{perl_vendorarch}/%module
%{perl_vendorarch}/%module.pm
%{perl_vendorarch}/auto/*


