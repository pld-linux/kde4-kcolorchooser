%define		_state		stable
%define		qtver		4.7.3

Summary:	Color chooser
Summary(pl.UTF-8):	Program do wybierania kolorów
Name:		kcolorchooser
Version:	4.7.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	95a77f2d4a07d99d2a34bee6963d3d0d
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	perl
BuildRequires:	phonon-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	xorg-lib-libX11-devel
Requires:	kde4-kdebase >= %{version}
Obsoletes:	kde4-kdegraphics-kcolorchooser
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Color chooser.

%description -l pl.UTF-8
Program do wybierania kolorów.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DGWENVIEW_SEMANTICINFO_BACKEND=Nepomuk \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcolorchooser
%{_desktopdir}/kde4/kcolorchooser.desktop
%{_iconsdir}/[!l]*/*/*/kcolorchooser.*
