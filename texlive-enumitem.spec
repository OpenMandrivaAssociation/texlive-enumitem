Name:		texlive-enumitem
Version:	51423
Release:	1
Summary:	Control layout of itemize, enumerate, description
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/enumitem
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enumitem.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enumitem.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/enumitem
%doc %{_texmfdistdir}/doc/latex/enumitem

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
