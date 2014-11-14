%define		_state		stable
%define		orgname		kcolorchooser
%define		qtver		4.8.1

Summary:	Color chooser
Summary(pl.UTF-8):	Program do wybierania kolorów
Name:		kde4-kcolorchooser
Version:	4.14.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	93a8a1b6998d38a33852245859b70c42
URL:		http://www.kde.org/
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	xorg-lib-libX11-devel
Requires:	kde4-kdebase >= %{version}
Obsoletes:	kde4-kdegraphics-kcolorchooser < 4.6.99
Obsoletes:	kcolorchooser < 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Color chooser.

%description -l pl.UTF-8
Program do wybierania kolorów.

%prep
%setup -q -n %{orgname}-%{version}

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
