%define name	diction
%define version 1.11
%define epoch   1
%define release %mkrel 1

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
%configure 
%make

%install
%__rm -rf %{buildroot}
%make DESTDIR=%{buildroot} install

%clean
%__rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING README NEWS INSTALL
%{_bindir}/*
%{_datadir}/diction/
%{_datadir}/locale/
%{_mandir}/man1/*
