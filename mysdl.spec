Summary:	MySDL library
Summary(pl.UTF-8):	Biblioteka MySDL
Name:		mysdl
Version:	1.0.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://source.musgit.com/files/%{name}_%{version}.tar.bz2
# Source0-md5:	57338c671b01df9636cba1466f05be73
URL:		http://source.musgit.com/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL_image-devel
BuildRequires:	expat-devel
BuildRequires:	libvorbis-devel
BuildRequires:	scons
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySDL is a gaming framework and library based on SDL, OpenGL, OpenAL
and a few more open source libraries.

%description -l pl.UTF-8
MySDL to szkielet i biblioteka dla gier oparta na bibliotekach SDL,
OpenGL, OpenAL i kilku innych o otwartych źródłach.

%prep
%setup -q -n %{name}_%{version}

%build
sed -i "s/CXXFLAGS=\['-march=pentium'\]/CXXFLAGS=Split(ARGUMENTS.get('CXXFLAGS',''))/" SConstruct
sed -i 's/-O3//' SConstruct
%{__scons} \
	%{!?debug:dist=1} \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

cp -r dist/linux/include/* $RPM_BUILD_ROOT%{_includedir}
cp dist/linux/lib/* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}/*
