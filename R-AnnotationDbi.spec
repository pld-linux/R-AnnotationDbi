%define		packname	AnnotationDbi

Summary:	Annotation Database Interface
Name:		R-%{packname}
Version:	1.20.1
Release:	1
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	71a39e9607d54c8cad77f4595f16897c
URL:		http://bioconductor.org/packages/release/bioc/html/%{packname}.html
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
