Summary:	A free virtual machine for running Java(TM) code
Name:		kaffe
Version:	1.0.6
Release:	4
Epoch:		1
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	http://www.kaffe.org/ftp/pub/kaffe/%{name}-%{version}.tar.gz
Patch0:		%{name}-alpha.patch
Patch1:		%{name}-perlpath.patch
Patch2:		%{name}-getBytes.patch
Patch3:		%{name}-sparc.patch
Patch4:		%{name}-jlong.patch
Patch5:		%{name}-time.patch
URL:		http://www.kaffe.org/
Obsoletes:	kaffe-bissawt
Provides:	java
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/kaffe

%description
Kaffe is a free virtual machine designed to execute Java(TM) bytecode.
Kaffe can be configured in two modes. In the first mode, it operates
as a pure bytecode interpreter (not unlike Javasoft's machine). In the
second mode, it performs "just-in-time" code conversion from the
abstract code to the host machine's native code. The second mode will
ultimately allow execution of Java code at the same speed as standard
compiled code, while also maintaining the advantages and flexibility
of code independence.

%package devel
Summary:	Headers and libtool files for kaffe
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}

%description devel
Headers and libtool files for kaffe.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -rf developers/{glibc-2.1.1-signal.patch,rpm-kaffe.spec} FAQ/CVS

gzip -9nf FAQ/* ChangeLog* README WHATSNEW \
	developers/README*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ/*.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libexecdir}/Kaffe
%attr(755,root,root) %{_libdir}/*.so
%dir %{_libdir}/kaffe
%attr(755,root,root) %{_libdir}/kaffe/*.so
%{_libdir}/kaffe/security
%{_mandir}/man1/kaffe.1*
%{_datadir}/kaffe

%files devel
%defattr(644,root,root,755)
%doc *.gz developers/*
%{_includedir}/kaffe
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/kaffe/*.la
