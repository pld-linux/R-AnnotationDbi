%define		packname	AnnotationDbi

%undefine	_debugsource_packages
Summary:	Annotation Database Interface
Name:		R-%{packname}
Version:	1.72.0
Release:	1
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	https://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	dab5c3c6d38999d7f3d0c16dd93d1780
URL:		https://bioconductor.org/packages/release/bioc/html/AnnotationDbi.html
BuildRequires:	R-Biobase
BuildRequires:	R-BiocGenerics
BuildRequires:	R-cran-DBI
BuildRequires:	R-IRanges-devel
BuildRequires:	R-cran-RSQLite
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R-Biobase
Requires:	R-BiocGenerics
Requires:	R-cran-DBI
Requires:	R-IRanges
Requires:	R-cran-RSQLite
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides user interface and database connection code for annotation
data packages using SQLite data storage.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/NEWS
%doc %{_libdir}/R/library/%{packname}/TODO
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/DBschemas
%{_libdir}/R/library/%{packname}/extdata
%{_libdir}/R/library/%{packname}/NOTES-Herve
%{_libdir}/R/library/%{packname}/unitTests
