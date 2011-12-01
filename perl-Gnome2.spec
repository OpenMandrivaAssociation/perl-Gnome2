%define upstream_name    Gnome2
%define upstream_version 1.042

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 9

Summary:    Perl module for the gnome2-2.x core libraries
License:    GPL or Artistic
Group:      Development/GNOME and GTK+
Url:        http://gtk2-perl.sf.net/
# http://sourceforge.net/project/showfiles.php?group_id=64773&package_id=91219
Source:     %{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires: gnomeui2-devel 
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Gnome2::VFS)    >= 1.00
BuildRequires: perl(Gnome2::Canvas)
BuildRequires: perl(Gtk2)           >= 1.00
Buildrequires: perl-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Conflicts: drakxtools < 9.1-15mdk
Requires:  perl(Gtk2) >= 1.00

%description
This module provides perl access to GNOME-2.x core libraries.

GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window manager
for the X Window System. GNOME is similar in purpose and scope to CDE and KDE,
but GNOME (like KDE) is based completely on Open Source software.

GNOME libraries provide extra widgets on top of the gtk+ toolkit.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
export GTK2_PERL_CFLAGS="$RPM_OPT_FLAGS"
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS LICENSE examples/*
%{_mandir}/*/*
%{perl_vendorarch}/%{upstream_name}
%{perl_vendorarch}/%{upstream_name}.pm
%{perl_vendorarch}/auto/*
