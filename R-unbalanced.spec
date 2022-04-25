#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-unbalanced
Version  : 2.0
Release  : 10
URL      : https://cran.r-project.org/src/contrib/unbalanced_2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/unbalanced_2.0.tar.gz
Summary  : Racing for Unbalanced Methods Selection
Group    : Development/Tools
License  : GPL-3.0
Requires: R-FNN
Requires: R-RANN
Requires: R-doParallel
Requires: R-foreach
Requires: R-mlr
BuildRequires : R-FNN
BuildRequires : R-RANN
BuildRequires : R-doParallel
BuildRequires : R-foreach
BuildRequires : R-mlr
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n unbalanced
cd %{_builddir}/unbalanced

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641142197

%install
export SOURCE_DATE_EPOCH=1641142197
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library unbalanced
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library unbalanced
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library unbalanced
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc unbalanced || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/unbalanced/DESCRIPTION
/usr/lib64/R/library/unbalanced/INDEX
/usr/lib64/R/library/unbalanced/Meta/Rd.rds
/usr/lib64/R/library/unbalanced/Meta/data.rds
/usr/lib64/R/library/unbalanced/Meta/features.rds
/usr/lib64/R/library/unbalanced/Meta/hsearch.rds
/usr/lib64/R/library/unbalanced/Meta/links.rds
/usr/lib64/R/library/unbalanced/Meta/nsInfo.rds
/usr/lib64/R/library/unbalanced/Meta/package.rds
/usr/lib64/R/library/unbalanced/NAMESPACE
/usr/lib64/R/library/unbalanced/R/unbalanced
/usr/lib64/R/library/unbalanced/R/unbalanced.rdb
/usr/lib64/R/library/unbalanced/R/unbalanced.rdx
/usr/lib64/R/library/unbalanced/data/ubIonosphere.rda
/usr/lib64/R/library/unbalanced/help/AnIndex
/usr/lib64/R/library/unbalanced/help/aliases.rds
/usr/lib64/R/library/unbalanced/help/paths.rds
/usr/lib64/R/library/unbalanced/help/unbalanced.rdb
/usr/lib64/R/library/unbalanced/help/unbalanced.rdx
/usr/lib64/R/library/unbalanced/html/00Index.html
/usr/lib64/R/library/unbalanced/html/R.css
