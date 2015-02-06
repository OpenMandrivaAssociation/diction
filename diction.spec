%define name	diction
%define version 1.11
%define epoch   1
%define release 3

Summary: 	Text diction and style analyzer
Name: 		%{name}
Version:	%{version}
Release: 	%{release}
Epoch:		%{epoch}
License: 	GPLv3+
Group: 		Text tools
Source:		%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: 		http://www.moria.de/~michael/diction/

%description
GNU diction and style are free implementations of old standard Unix
commands that are unavailable on many modern systems because they have
been unbundled. Diction identifies wordy and commonly misused phrases.
Style analyses surface characteristics of a document (e.g., sentence
length and various readability measures); unlike the original code, it
cannot analyze sentence type, word usage, and general sentence
beginnings. Both commands currently support English and German
documents.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING README NEWS INSTALL
%{_bindir}/*
%{_datadir}/diction/
%{_datadir}/locale/
%{_mandir}/man1/*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.11-2mdv2011.0
+ Revision: 610242
- rebuild

* Thu Feb 18 2010 Funda Wang <fwang@mandriva.org> 1:1.11-1mdv2010.1
+ Revision: 507667
- build with configure2_5x

* Tue Jan 20 2009 Lev Givon <lev@mandriva.org> 1:1.11-1mdv2009.1
+ Revision: 331831
- Update to 1.11.

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.11rc1-1mdv2009.0
+ Revision: 136364
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jun 21 2007 Lev Givon <lev@mandriva.org> 1.11rc1-1mdv2008.0
+ Revision: 42342
- Update to 1.11-rc1.


* Mon Jan 29 2007 Lev Givon <lev@mandriva.org> 1.10rc4-1mdv2007.0
+ Revision: 115035
- Import diction

* Mon Jan 29 2007 Lev Givon <lev@mandriva.org> 1.10rc4-1mdv2007.0
- Initial Mandriva package.

