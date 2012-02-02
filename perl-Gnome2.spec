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
