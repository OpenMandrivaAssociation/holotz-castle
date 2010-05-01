Name:			holotz-castle
Version:		1.3.14
Release:		%mkrel 1

Summary:	Holotz's Castle - A strategy platform scroller
License:	GPLv2+
Group:		Games/Arcade
URL:		http://www.mainreactor.net/holotzcastle/en/index_en.html
Source0:	http://www.mainreactor.net/holotzcastle/download/%{name}-%{version}-src.tar.gz
Source10:	hc-48x48.png
Source11:	hc-32x32.png
Source12:	hc-16x16.png
Source20:	holotz-castle-editor-48x48.png
Source21:	holotz-castle-editor-32x32.png
Source22:	holotz-castle-editor-16x16.png
Patch0:		holotz-castle-1.3.6-install.patch
Patch1:		holotz-castle-1.3.11-compile-fixes.patch
Patch2:		holotz-castle-1.3.14-compile-fixes.patch

BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:  MesaGLU-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%package -n %{name}-editor
License:	GPLv2+
Group:		Games/Arcade
Summary:	Holotz's Castle level editor
Requires:	%{name} == %{version}

%description
A great mystery is hidden beyond the walls of Holotz's Castle. Will you be
able to help Ybelle and Ludar to escape alive from the castle?

Test your dexterity with this tremendously exciting platform game!

%description -n %{name}-editor
This package contains a level editor for Holotz's Castle.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p0
%patch1 -p1
%patch2 -p1
perl -pi -e s"|\r\n|\n|g" res/playlist.txt
rm -f res/savedata/empty.txt

%build
make

%install
rm -rf %{buildroot}
%makeinstall INSTALL_ROOT=%{buildroot}

install -d -m 755 %{buildroot}%{_mandir}/man6/
install -m 644 man/%{name}.6 %{buildroot}%{_mandir}/man6/
install -d -m 755 %{buildroot}%{_liconsdir}
install -d -m 755 %{buildroot}%{_miconsdir}
install -m 644 %{_sourcedir}/hc-48x48.png -D %{buildroot}%{_liconsdir}/%{name}.png
install -m 644 %{_sourcedir}/hc-32x32.png -D %{buildroot}%{_iconsdir}/%{name}.png
install -m 644 %{_sourcedir}/hc-16x16.png -D %{buildroot}%{_miconsdir}/%{name}.png
#game

#game, xdg
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Holotz's Castle
Comment=%{summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

#editor
install -m 644 man/%{name}-editor.6 %{buildroot}%{_mandir}/man6/
install -m 644 %{_sourcedir}/holotz-castle-editor-48x48.png -D %{buildroot}%{_liconsdir}/%{name}-editor.png
install -m 644 %{_sourcedir}/holotz-castle-editor-32x32.png -D %{buildroot}%{_iconsdir}/%{name}-editor.png
install -m 644 %{_sourcedir}/holotz-castle-editor-16x16.png -D %{buildroot}%{_miconsdir}/%{name}-editor.png

#editor, xdg
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}-editor.desktop << EOF
[Desktop Entry]
Name=Holotz's Castle Editor
Comment=Level editor for Holotz's Castle
Exec=%{_gamesbindir}/%{name}-editor
Icon=%{name}-editor
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%if %mdkversion < 200900
%post -n %{name}-editor
%update_menus
%endif

%if %mdkversion < 200900
%postun -n %{name}-editor
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,games,755)
%doc LICENSE.txt doc/*.txt
%attr(0755,root,games) %{_gamesbindir}/%{name}
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/game
%{_mandir}/man6/%{name}.6*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop

%files -n %{name}-editor
%defattr(644,root,games,755)
%doc LICENSE.txt
%attr(0755,root,games) %{_gamesbindir}/%{name}-editor
%{_gamesdatadir}/%{name}/editor
%{_mandir}/man6/%{name}-editor.6*
%{_liconsdir}/%{name}-editor.png
%{_iconsdir}/%{name}-editor.png
%{_miconsdir}/%{name}-editor.png
%{_datadir}/applications/mandriva-%{name}-editor.desktop

