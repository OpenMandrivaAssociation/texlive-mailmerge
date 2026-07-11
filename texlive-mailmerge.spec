%global tl_name mailmerge
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Repeating text field substitution
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mailmerge
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mailmerge.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mailmerge.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mailmerge.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package mailmerge provides an interface to produce text from a
template, where fields are replaced by actual data, as in a database.
The package may be used to produce several letters from a template,
certificates or other such documents. It allows access to the entry
number, number of entries and so on.

