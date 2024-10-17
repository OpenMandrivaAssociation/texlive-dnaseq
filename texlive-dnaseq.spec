Name:		texlive-dnaseq
Version:	17194
Release:	2
Summary:	Format DNA base sequences
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dnaseq
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dnaseq.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dnaseq.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dnaseq.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines a means of specifying sequences of bases. The bases may
be numbered (per line) and you may specify that subsequences be
coloured. For a more 'vanilla-flavoured' way of typesetting
base sequences, the user might consider the seqsplit package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dnaseq/dnaseq.sty
%doc %{_texmfdistdir}/doc/latex/dnaseq/DNAtest.tex
%doc %{_texmfdistdir}/doc/latex/dnaseq/README
%doc %{_texmfdistdir}/doc/latex/dnaseq/dnaseq.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dnaseq/dnaseq.dtx
%doc %{_texmfdistdir}/source/latex/dnaseq/dnaseq.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
