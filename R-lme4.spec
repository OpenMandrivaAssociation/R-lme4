%bcond_with bootstrap
%global packname  lme4
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.999999.0
Release:          1
Summary:          Linear mixed-effects models using S4 classes
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/lme4_0.999999-0.tar.gz
Requires:         R-methods R-Matrix R-lattice R-graphics R-nlme R-stats4
Requires:         R-stats 
%if %{without bootstrap}
Requires:         R-mlmRev R-MEMSS R-coda R-MASS R-sfsmisc R-MatrixModels
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    R-Matrix R-lattice R-graphics R-nlme R-stats4 R-stats
%if %{without bootstrap}
BuildRequires:    R-mlmRev R-MEMSS R-coda R-MASS R-sfsmisc R-MatrixModels
%endif
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
Fit linear and generalized linear mixed-effects models.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/*Rdata
