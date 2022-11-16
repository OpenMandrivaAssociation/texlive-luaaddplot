Name:		texlive-luaaddplot
Version:	62842
Release:	1
Summary:	An extension to pgfplots' \addplot macro
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/luaaddplot
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaaddplot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaaddplot.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaaddplot.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is an extension to pgfplots. It extends the
\addplot macro by a facility which allows modification of data
files while they are read. With luaaddplot it is no longer
necessary to pre-process data files generated by measuring
devices with external scripts. This package can be used with
plain LuaTeX or LuaLaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/luatex/luaaddplot
%{_texmfdistdir}/tex/luatex/luaaddplot
%doc %{_texmfdistdir}/doc/luatex/luaaddplot

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
