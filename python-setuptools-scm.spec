# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-setuptools-scm
Epoch: 100
Version: 8.0.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Blessed package to manage your versions by SCM tags
License: MIT
URL: https://github.com/pypa/setuptools_scm/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-importlib-metadata >= 4.6
BuildRequires: python3-packaging >= 20
BuildRequires: python3-rich
BuildRequires: python3-setuptools >= 61
BuildRequires: python3-tomli

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
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-setuptools_scm
Summary: Blessed package to manage your versions by SCM tags
Requires: python3
Requires: python3-importlib-metadata >= 4.6
Requires: python3-packaging >= 20
Requires: python3-setuptools >= 61
Requires: python3-tomli >= 1.0.0
Requires: python3-typing-extensions
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
Requires: python3-importlib-metadata >= 4.6
Requires: python3-packaging >= 20
Requires: python3-setuptools >= 61
Requires: python3-tomli >= 1.0.0
Requires: python3-typing-extensions
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
