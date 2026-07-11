%global tl_name dnaseq
%global tl_revision 17194

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.01
Release:	%{tl_revision}.1
Summary:	Format DNA base sequences
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dnaseq
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dnaseq.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dnaseq.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dnaseq.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines a means of specifying sequences of bases. The bases may be
numbered (per line) and you may specify that subsequences be coloured.
For a more 'vanilla-flavoured' way of typesetting base sequences, the
user might consider the seqsplit package.

