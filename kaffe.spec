Summary:	A free virtual machine for running Java(TM) code
Summary(es):	Máquina virtual free para ejecutar código Java(tm)
Summary(pl):	Darmowa maszyna wirtualna Javy
Summary(pt_BR):	Máquina virtual free para rodar código Java(tm)
Name:		kaffe
Version:	1.0.6
Release:	8
Epoch:		1
License:	GPL
Group:		Development/Languages/Java
Source0:	http://www.kaffe.org/ftp/pub/kaffe/%{name}-%{version}.tar.gz
Patch0:		%{name}-alpha.patch
Patch1:		%{name}-perlpath.patch
Patch2:		%{name}-getBytes.patch
Patch3:		%{name}-sparc.patch
Patch4:		%{name}-jlong.patch
Patch5:		%{name}-time.patch
Patch6:		%{name}-acfix.patch
Patch7:		%{name}-amfix.patch
Patch8:		%{name}-ltfix.patch
URL:		http://www.kaffe.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmp-devel >= 3.1.1
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libungif-devel
ExcludeArch:	ia64 s390 s390x
Provides:	jre = 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kaffe-bissawt
Conflicts:	ibm-java-sdk

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

%description -l es
Kaffe es una máquina virtual proyectada para ejecutar bytecode Java.
Esta máquina puede ser configurada en dos modos. En uno, opera como un
interpretador puro de bytecode (como la máquina de la JavaSoft); en el
segundo modo, ejecuta conversión de código "just-in-time" del código
abstracto para el código nativo de máquina. Esto permite la ejecución
de código Java en la misma velocidad que el código compilado, con las
ventajas de la flexibilidad y independencia de código.

%description -l pl
Kaffe jest darmow± maszyn± wirtualn± do uruchamiania bytecodu Javy.
Mo¿e byæ u¿ywana w dwóch trybach: w pierwszym jako czysty interpreter
bytecodu, w drugim przeprowadza "w locie" konwersjê bytecodu na kod
natywny maszyny. Drugi tryb pozwala uruchamiaæ kod Javy tak szybko jak
kod skompilowany, pozostawiaj±c niezale¿no¶æ kodu od platformy.

%description -l pt_BR
Kaffe é uma máquina virtual projetada para executar bytecode Java.
Esta máquina pode ser configurada em dois modos. Em um modo ela opera
como um interpretador puro de bytecode (como a máquina da JavaSoft);
no segundo modo ela executa conversão de código "just-in-time" do
código abstrato para o código nativo de máquina. Isto permite a
execução de código Java na mesma velocidade que o código compilado,
com as vantagens da flexibilidade e independência de código.

%package devel
Summary:	Headers and libtool files for kaffe
Summary(pl):	Pliki nag³ówkowe i skrypty libtoola dla kaffe
Summary(pt_BR):	Bibliotecas e headers de desenvolvimento para o Kaffe
Group:		Development/Languages/Java
Requires:	%{name} = %{version}

%description devel
Headers and libtool files for kaffe.

%description devel -l pl
Pliki nag³ówkowe i skrypty libtoola dla kaffe.

%description devel -l pt_BR
Bibliotecas e headers de desenvolvimento para o Kaffe.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
rm -f acinclude.m4
libtoolize --copy --force --ltdl
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -rf developers/{glibc-2.1.1-signal.patch,rpm-kaffe.spec} FAQ/CVS

gzip -9nf FAQ/* ChangeLog* README WHATSNEW \
	developers/README*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
