#
# spec file for package libscew
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libscew
%define lname	libscew1
Version:        1.2.0
Release:        0
Url:            http://nongnu.org/scew/
Summary:        Simple C Expat Wrapper
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++

#Git-Clone:	git://git.savannah.nongnu.org/scew
Source:         http://savannah.nongnu.org/download/scew/scew-%version.tar.gz
BuildRoot:      %{_tmppath}/scew-%{version}-build
BuildRequires:  expat-devel
BuildRequires:  pkg-config

%description
SCEW provides an easy interface around the Expat XML parser, as well
as a simple interface for creating new XML documents. It provides
functions to load and access XML elements without the need to create
Expat event handling routines.

%package -n libscew1
Summary:        Simple C Expat Wrapper library
Group:          System/Libraries

%description -n libscew1
SCEW provides an easy interface around the Expat XML parser, as well
as a simple interface for creating new XML documents. It provides
functions to load and access XML elements without the need to create
Expat event handling routines.

%package devel
Summary:        Development files for the Simple C Expat Wrapper library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
SCEW provides an easy interface around the Expat XML parser, as well
as a simple interface for creating new XML documents. It provides
functions to load and access XML elements without the need to create
Expat event handling routines.

This subpackage contains the development headers for SCEW.

%prep
%setup -qn scew-%version

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}/%{_libdir}/libscew.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-, root, root)
%{_libdir}/libscew.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/libscew.so
%{_libdir}/pkgconfig/scew.pc

%changelog

