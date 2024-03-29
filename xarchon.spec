Summary:	Archon game
Summary(pl.UTF-8):	Gra Archon
Name:		xarchon
Version:	0.50
Release:	4
License:	GPL
Group:		X11/Applications/Games
Source0:	http://xarchon.seul.org/%{name}-%{version}.tar.gz
# Source0-md5:	491dea5b4e61ed13cd988d1c184a8ef0
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-ac.patch
URL:		http://xarchon.seul.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel > 1.2.1
BuildRequires:	glib-devel
BuildRequires:	esound-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X ARCHON, as the name implies, is a clone of the original (about
15-years old) ARCHON game. And, it's for the X Window System.

%description -l pl.UTF-8
X ARCHON to klon (ok. 15-letniej) gdy ARCHON przeznaczony dla systemu
X Window.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--with-x
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man*/*
