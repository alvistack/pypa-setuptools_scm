%global debug_package %{nil}

Name: python-setuptools-scm
Epoch: 100
Version: 6.3.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Blessed package to manage your versions by SCM tags
License: MIT
URL: https://github.com/pypa/setuptools_scm/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
setuptools_scm handles managing your Python package versions in SCM
metadata. It also handles file finders for the supported SCMs.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-setuptools_scm
Summary: Blessed package to manage your versions by SCM tags
Requires: python3
Requires: python3-packaging
Requires: python3-setuptools >= 42
Requires: python3-tomli >= 1.0.0
Provides: python3-setuptools_scm = %{epoch}:%{version}-%{release}
Provides: python3dist(setuptools-scm) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-setuptools_scm = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(setuptools-scm) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(setuptools-scm) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-setuptools_scm = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-setuptools_scm
setuptools_scm handles managing your Python package versions in SCM
metadata. It also handles file finders for the supported SCMs.

%files -n python%{python3_version_nodots}-setuptools_scm
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-setuptools_scm
Summary: Blessed package to manage your versions by SCM tags
Requires: python3
Requires: python3-packaging
Requires: python3-setuptools >= 42
Requires: python3-tomli >= 1.0.0
Provides: python3-setuptools_scm = %{epoch}:%{version}-%{release}
Provides: python3dist(setuptools-scm) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-setuptools_scm = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(setuptools-scm) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(setuptools-scm) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-setuptools_scm = %{epoch}:%{version}-%{release}

%description -n python3-setuptools_scm
setuptools_scm handles managing your Python package versions in SCM
metadata. It also handles file finders for the supported SCMs.

%files -n python3-setuptools_scm
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
