Name:           nishbox
Version:        0.0.0
Release:        1%{?dist}
Summary:        Open-source multiplayer sandbox game

License:        BSD-3-Clause
URL:            https://github.com/pyrite-dev/nishbox
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  premake 
BuildRequires:  gcc 
BuildRequires:  make
BuildRequires:  pkgconfig(sdl2)

Requires:       pkgconfig(sdl2)

%description    
Open-source multiplayer sandbox game

%prep
%setup -q

%build          
premake5 gmake --engine=dynamic
make config=release_native -j$(nproc) 

%install
./install.sh

%files
%{_bindir}/nishbox/
%{_datadir}/NishBox/base.pak
%{_libdir}/libgoldfish.a

%license COPYING

%changelog
* Tue Jun 24 2025 IoIxD <alphaproject217@gmail.com>
- there is no changelog.
