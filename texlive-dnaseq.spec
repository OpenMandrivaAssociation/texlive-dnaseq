# revision 17194
# category Package
# catalog-ctan /macros/latex/contrib/dnaseq
# catalog-date 2010-02-24 21:28:09 +0100
# catalog-license lppl
# catalog-version 0.01
Name:		texlive-dnaseq
Version:	0.01
Release:	1
Summary:	Format DNA base sequences
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dnaseq
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dnaseq.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dnaseq.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dnaseq.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Defines a means of specifying sequences of bases. The bases may
be numbered (per line) and you may specify that subsequences be
coloured. For a more 'vanilla-flavoured' way of typesetting
base sequences, the user might consider the seqsplit package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
