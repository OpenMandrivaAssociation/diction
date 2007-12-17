%define name diction
%define realversion 1.11
%define epoch   rc1
%define release 1

Summary: 	Text diction and style analyzer
Name: 		%{name}
Version:	%{realversion}%{epoch}
Release: 	%mkrel %{release}
License: 	GPL
Group: 		Text tools
Source:		diction-%{realversion}-%{epoch}.tar.bz2
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
%setup -q -n %{name}-%{realversion}

%build
%configure 
%make

%install
rm -rf %{buildroot}
%make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING README NEWS INSTALL
%{_bindir}/*
%{_datadir}/diction/
%{_datadir}/locale/
%{_mandir}/man1/*


