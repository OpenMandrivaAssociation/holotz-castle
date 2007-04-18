%define name holotz-castle
%define version 1.3.9
%define release %mkrel 1

%define Summary Holotz's Castle - A strategy platform scroller

Name: %{name}
Version: %{version}
Release: %{release}
URL: http://www.mainreactor.net/holotzcastle/en/index_en.html
Source0: http://www.mainreactor.net/holotzcastle/download/%{name}-%{version}-src.tar.bz2
#additionnal levels from Milan B.
Source1: http://abrick.sourceforge.net/milanb-hc-levels.zip
Source10: hc-48x48.png
Source11: hc-32x32.png
Source12: hc-16x16.png
Source20: %{name}-editor-48x48.png
Source21: %{name}-editor-32x32.png
Source22: %{name}-editor-16x16.png
Patch0: %{name}-1.3.6-install.patch
Patch1: %{name}-1.3.8-warnings-fixes.patch
License: GPL
Group: Games/Arcade
Summary: %{Summary}
BuildRequires: SDL-devel SDL_mixer-devel SDL_image-devel SDL_ttf-devel
BuildRequires: dos2unix, unzip
BuildRequires: MesaGLU-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%package -n %{name}-editor
License: GPL
Group: Games/Arcade
Summary: Holotz's Castle level editor
Requires: %{name} == %{version}

%description
A great mystery is hidden beyond the walls of Holotz's Castle. Will you be
able to help Ybelle and Ludar to escape alive from the castle?

Test your dexterity with this tremendously exciting platform game!

%description -n %{name}-editor
This package contains a level editor for Holotz's Castle.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p0
unzip -o %{SOURCE1}
dos2unix res/playlist.txt res/README.txt
rm -f res/savedata/empty.txt
%patch1 -p1

%build
make

%install
rm -rf %buildroot
%makeinstall INSTALL_ROOT=%buildroot

install -d 755 %buildroot%{_mandir}/man6/
install -m 644 doc/%{name}.6 %buildroot%{_mandir}/man6/
install -d 755 %buildroot%{_liconsdir}
install -d 755 %buildroot%{_miconsdir}
install -m 644 %{SOURCE10} -D %buildroot%{_liconsdir}/%{name}.png
install -m 644 %{SOURCE11} -D %buildroot%{_iconsdir}/%{name}.png
install -m 644 %{SOURCE12} -D %buildroot%{_miconsdir}/%{name}.png
#game
install -d 755 %buildroot%{_menudir}
cat << EOF > %buildroot/%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}"\
 icon="%{name}.png"\
 needs="x11"\
 section="More Applications/Games/Arcade"\
 title="%{Summary}"\
 longtitle="%{Summary}"\
 xdg=true"
EOF

#game, xdg
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Holotz's Castle
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
Encoding=UTF-8
EOF

#editor
install -m 644 doc/%{name}-editor.6 %buildroot%{_mandir}/man6/
install -m 644 %{SOURCE20} -D %buildroot%{_liconsdir}/%{name}-editor.png
install -m 644 %{SOURCE21} -D %buildroot%{_iconsdir}/%{name}-editor.png
install -m 644 %{SOURCE22} -D %buildroot%{_miconsdir}/%{name}-editor.png
cat << EOF > %buildroot/%{_menudir}/%{name}-editor
?package(%{name}-editor):command="%{_gamesbindir}/%{name}-editor"\
 icon="%{name}-editor.png"\
 needs="x11"\
 section="More Applications/Games/Arcade"\
 title="Holotz's Castle Editor"\
 longtitle="Level editor for Holotz's Castle"\
 xdg="true"
EOF

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
Encoding=UTF-8
EOF

%post
%update_menus

%postun
%clean_menus

%post -n %{name}-editor
%update_menus

%postun -n %{name}-editor
%clean_menus

%clean
rm -rf %buildroot

%files
%defattr(644,root,games,755)
%doc LICENSE.txt MANUAL_EN.txt MANUAL_ES.txt MANUAL_EU.txt MANUAL_FR.txt
%doc MANUAL_RU.txt MANUAL_UA.txt
%attr(0755,root,games) %{_gamesbindir}/%{name}
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/game
%{_mandir}/man6/%{name}.6*
%{_menudir}/%{name}
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
%{_menudir}/%{name}-editor
%{_liconsdir}/%{name}-editor.png
%{_iconsdir}/%{name}-editor.png
%{_miconsdir}/%{name}-editor.png
%{_datadir}/applications/mandriva-%{name}-editor.desktop

