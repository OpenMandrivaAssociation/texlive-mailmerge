# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/mailmerge
# catalog-date 2009-11-09 23:10:10 +0100
# catalog-license lppl1.2
# catalog-version 1.0
Name:		texlive-mailmerge
Version:	1.0
Release:	1
Summary:	Repeating text field substitution
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mailmerge
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mailmerge.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mailmerge.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mailmerge.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package mailmerge provides an interface to produce text
from a template, where fields are replaced by actual data, as
in a database. The package may be used to produce several
letters from a template, certificates or other such documents.
It allows access to the entry number, number of entries and so
on.

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
%{_texmfdistdir}/tex/latex/mailmerge/mailmerge.sty
%doc %{_texmfdistdir}/doc/latex/mailmerge/README
%doc %{_texmfdistdir}/doc/latex/mailmerge/mailmerge.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mailmerge/mailmerge.dtx
%doc %{_texmfdistdir}/source/latex/mailmerge/mailmerge.ins
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
