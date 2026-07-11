%global tl_name enumitem
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.11
Release:	%{tl_revision}.1
Summary:	Control layout of itemize, enumerate, description
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/enumitem
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/enumitem.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/enumitem.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides user control over the layout of the three basic
list environments: enumerate, itemize and description. It supersedes
both enumerate and mdwlist (providing well-structured replacements for
all their functionality), and in addition provides functions to compute
the layout of labels, and to 'clone' the standard environments, to
create new environments with counters of their own.

