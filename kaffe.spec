Summary:	A free virtual machine for running Java(TM) code
Summary(es):	MАquina virtual free para ejecutar cСdigo Java(tm)
Summary(pl):	Darmowa maszyna wirtualna Javy
Summary(pt_BR):	MАquina virtual free para rodar cСdigo Java(tm)
Summary(ru):	Свободно распространяемая виртуальная машина для запуска Java(tm) кода
Summary(uk):	В╕льно розповсюджувана в╕ртуальна машина для запуску Java(tm) коду
Name:		kaffe
Version:	1.0.6
Release:	11
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
Patch9:		%{name}-dyn_ltdl.patch
URL:		http://www.kaffe.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmp-devel >= 3.1.1
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libungif-devel
%ifarch ppc
BuildRequires:	libffi-devel
%endif
ExcludeArch:	ia64 s390 s390x
Provides:	jre = 1.1
Requires:	fastjar
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
Kaffe es una mАquina virtual proyectada para ejecutar bytecode Java.
Esta mАquina puede ser configurada en dos modos. En uno, opera como un
interpretador puro de bytecode (como la mАquina de la JavaSoft); en el
segundo modo, ejecuta conversiСn de cСdigo "just-in-time" del cСdigo
abstracto para el cСdigo nativo de mАquina. Esto permite la ejecuciСn
de cСdigo Java en la misma velocidad que el cСdigo compilado, con las
ventajas de la flexibilidad y independencia de cСdigo.

%description -l pl
Kaffe jest darmow╠ maszyn╠ wirtualn╠ do uruchamiania bytecodu Javy.
Mo©e byФ u©ywana w dwСch trybach: w pierwszym jako czysty interpreter
bytecodu, w drugim przeprowadza "w locie" konwersjЙ bytecodu na kod
natywny maszyny. Drugi tryb pozwala uruchamiaФ kod Javy tak szybko jak
kod skompilowany, pozostawiaj╠c niezale©no╤Ф kodu od platformy.

%description -l pt_BR
Kaffe И uma mАquina virtual projetada para executar bytecode Java.
Esta mАquina pode ser configurada em dois modos. Em um modo ela opera
como um interpretador puro de bytecode (como a mАquina da JavaSoft);
no segundo modo ela executa conversЦo de cСdigo "just-in-time" do
cСdigo abstrato para o cСdigo nativo de mАquina. Isto permite a
execuГЦo de cСdigo Java na mesma velocidade que o cСdigo compilado,
com as vantagens da flexibilidade e independЙncia de cСdigo.

%description -l ru
Это -- Kaffe, виртуальная машина разработанная для выполнения байткода
Java. Эта машина может быть использована в двух режимах. В первом она
работает как "чистый" интепретатор байткода (подобно машине из JDK/JRE
от Javasoft'а); во втором режиме она выполняет компиляцию типа
"just-in-time" (то есть преобразует из абстрактного байт-кода в
машинный код перед исполнением). Это в пределе может позволить
программам, написанным на Java, исполняться с той же скоростью как и
стандартный откомпилированный код сохранив при этом все премущества и
гибкость машинно-независимого подхода.

%description -l uk
Це -- Kaffe, в╕ртуальна машина, розроблена для виконання байткоду
Java. Ця машина може бути використана в двох режимах. В першому вона
працю╓ як "чистий" ╕нтерпретатор байткоду (так само, як машина з
JDK/JRE в╕д Javasoft); в другому - викону╓ комп╕ляц╕ю "just-in-time"
(перетворю╓ з абстрактного байт-коду в машинний код перед виконанням).
Це в ╕деал╕ може дозволити програмам, написаним на Java, виконуватися
з тою ж швидк╕стю, як ╕ стандартний скомп╕льований код, збер╕гаючи при
цьому все переваги та гнучк╕сть машинно-незалежного п╕дходу.

%package devel
Summary:	Headers and libtool files for kaffe
Summary(pl):	Pliki nagЁСwkowe i skrypty libtoola dla kaffe
Summary(pt_BR):	Bibliotecas e headers de desenvolvimento para o Kaffe
Summary(ru):	Хедеры и библиотеки для kaffe
Summary(uk):	Хедери та б╕бл╕отеки для kaffe
Group:		Development/Languages/Java
Requires:	%{name} = %{version}
Provides:	jdk = 1.1

%description devel
Headers and libtool files for kaffe.

%description devel -l pl
Pliki nagЁСwkowe i skrypty libtoola dla kaffe.

%description devel -l pt_BR
Bibliotecas e headers de desenvolvimento para o Kaffe.

%description devel -l ru
Хедеры и библиотеки для разработок с использованием kaffe (включая
компиляцию java-программ).

%description devel -l uk
Хедери та б╕бл╕отеки для розробок з використанням kaffe (включаючи
комп╕ляц╕ю java-програм).

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
%patch9

%build
rm -f missing acinclude.m4
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure \
	--enable-ltdl-install=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -rf developers/{glibc-2.1.1-signal.patch,rpm-kaffe.spec} FAQ/CVS
rm -rf $RPM_BUILD_ROOT%{_bindir}/jar

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc FAQ/* ChangeLog* README WHATSNEW developers/README*
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
