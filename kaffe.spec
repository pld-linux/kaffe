Summary:	A free virtual machine for running Java(TM) code.
Name:		kaffe
Version:	1.0.5
Release:	2
License:	GPL
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Source:		http://www.kaffe.org/ftp/pub/kaffe/kaffe-%{version}.tar.gz
Patch0:		kaffe-alpha.patch
Patch1:		kaffe-perlpath.patch
URL:		http://www.kaffe.org/
Obsoletes:	kaffe-bissawt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kaffe is a free virtual machine designed to execute Java(TM) bytecode. Kaffe
can be configured in two modes. In the first mode, it operates as a pure
bytecode interpreter (not unlike Javasoft's machine). In the second mode, it
performs "just-in-time" code conversion from the abstract code to the host
machine's native code. The second mode will ultimately allow execution of
Java code at the same speed as standard compiled code, while also
maintaining the advantages and flexibility of code independence.

%package devel
Summary:	Headers and libtool files for kaffe
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}

%description devel
Headers and libtool files for kaffe.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT{%{_libdir},%{_libdir}/kaffe}/*.so

rm -f developers/{glibc-2.1.1-signal.patch,rpm-kaffe.spec}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	FAQ/* ChangeLog* README WHATSNEW \
	developers/README*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ {ChangeLog*,README,WHATSNEW}.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libexecdir}/Kaffe
%attr(755,root,root) %{_libdir}/*.so
%dir %{_libdir}/kaffe
%attr(755,root,root) %{_libdir}/kaffe/*.so
%{_libdir}/kaffe/security
%{_mandir}/man1/kaffe.1.gz
%{_datadir}/kaffe

%files devel
%defattr(644,root,root,755)
%doc developers/*
%{_includedir}/kaffe
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/kaffe/*.la
