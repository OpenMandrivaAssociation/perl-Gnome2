%define modname	Gnome2
%define modver	1.042

Summary:	Perl modname	for the gnome2-2.x core libraries
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	19
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
# http://sourceforge.net/project/showfiles.php?group_id=64773&package_id=91219
Source0:	%{modname}-%{modver}.tar.bz2
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Gnome2::VFS)
BuildRequires:	perl(Gnome2::Canvas)
BuildRequires:	perl(Gtk2)
Buildrequires:	perl-devel
Requires:	perl(Gtk2) >= 1.00

%description
This modname	provides perl access to GNOME-2.x core libraries.

GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window manager
for the X Window System. GNOME is similar in purpose and scope to CDE and KDE,
but GNOME (like KDE) is based completely on Open Source software.

GNOME libraries provide extra widgets on top of the gtk+ toolkit.


%prep
%setup -qn %{modname}-%{modver}
find -type d -name CVS | rm -rf 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc AUTHORS LICENSE examples/*
%{perl_vendorarch}/%{modname}
%{perl_vendorarch}/%{modname}.pm
%{perl_vendorarch}/auto/*
%{_mandir}/man3/*

