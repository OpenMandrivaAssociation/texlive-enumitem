Name:		texlive-enumitem
Version:	3.5.2
Release:	1
Summary:	Control layout of itemize, enumerate, description
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/enumitem
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enumitem.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enumitem.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package provides user control over the layout of the three
basic list environments: enumerate, itemize and description. It
supersedes both enumerate and mdwlist (providing well-
structured replacements for all their funtionality), and in
addition provides functions to compute the layout of labels,
and to 'clone' the standard environments, to create new
environments with counters of their own.

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
%{_texmfdistdir}/tex/latex/enumitem/enumitem.sty
%doc %{_texmfdistdir}/doc/latex/enumitem/README
%doc %{_texmfdistdir}/doc/latex/enumitem/enumitem.pdf
%doc %{_texmfdistdir}/doc/latex/enumitem/enumitem.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
