# revision 24146
# category Package
# catalog-ctan /macros/latex/contrib/enumitem
# catalog-date 2011-09-28 17:37:11 +0200
# catalog-license lppl
# catalog-version 3.5.2
Name:		texlive-enumitem
Version:	3.5.2
Release:	3
Summary:	Control layout of itemize, enumerate, description
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/enumitem
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enumitem.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enumitem.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides user control over the layout of the three
basic list environments: enumerate, itemize and description. It
supersedes both enumerate and mdwlist (providing well-
structured replacements for all their funtionality), and in
addition provides functions to compute the layout of labels,
and to 'clone' the standard environments, to create new
environments with counters of their own.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.5.2-2
+ Revision: 751471
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.5.2-1
+ Revision: 718337
- texlive-enumitem
- texlive-enumitem
- texlive-enumitem
- texlive-enumitem

