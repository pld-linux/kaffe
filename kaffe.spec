#
# TODO:
# - cairo+pango
# - can more files be moved %%{name} -> devel?

Summary:	A free virtual machine for running Java(TM) code
Summary(es):	M�quina virtual free para ejecutar c�digo Java(tm)
Summary(pl):	Darmowa maszyna wirtualna Javy
Summary(pt_BR):	M�quina virtual free para rodar c�digo Java(tm)
Summary(ru):	�������� ���������������� ����������� ������ ��� ������� Java(tm) ����
Summary(uk):	������ ��������������� צ�������� ������ ��� ������� Java(tm) ����
Name:		kaffe
Version:	1.1.6
Release:	0.1
Epoch:		1
License:	GPL
Group:		Development/Languages/Java
Source0:	http://www.kaffe.org/ftp/pub/kaffe/v1.1.x-development/%{name}-%{version}.tar.gz
# Source0-md5:	29d4b9ec58080715d13a764e9e4cfc06
Patch0:		%{name}-alpha.patch
Patch1:		%{name}-dyn_ltdl.patch
Patch2:		%{name}-posix-sh.patch
Patch3:		%{name}-jredir.patch
Patch4:		%{name}-automake-1_9_4.patch
URL:		http://www.kaffe.org/
BuildRequires:	alsa-lib-devel >= 1.0.1
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9.4
BuildRequires:	esound-devel >= 0.2.1
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.2
BuildRequires:	gmp-devel >= 3.1.1
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	jikes >= 1.21
%ifarch ppc
BuildRequires:	libffi-devel
%endif
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	zip
Requires:	fastjar
Provides:	jre = 1.4
Obsoletes:	kaffe-bissawt
Conflicts:	ibm-java-sdk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_jredir	%{_libdir}/java
%ifarch %{ix86}
%define		_archdir %{_jredir}/lib/i386
%endif
%ifarch %{x8664}
%define		_archdir %{_jredir}/lib/x86_64
%endif
%ifarch alpha arm m68k mips sparc
%define		_archdir %{_jredir}/lib/%{_arch}
%endif
%ifarch ppc
%define		_archdir %{_jredir}/lib/powerpc
%endif

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
Kaffe es una m�quina virtual proyectada para ejecutar bytecode Java.
Esta m�quina puede ser configurada en dos modos. En uno, opera como un
interpretador puro de bytecode (como la m�quina de la JavaSoft); en el
segundo modo, ejecuta conversi�n de c�digo "just-in-time" del c�digo
abstracto para el c�digo nativo de m�quina. Esto permite la ejecuci�n
de c�digo Java en la misma velocidad que el c�digo compilado, con las
ventajas de la flexibilidad y independencia de c�digo.

%description -l pl
Kaffe jest darmow� maszyn� wirtualn� do uruchamiania bytecodu Javy.
Mo�e by� u�ywana w dw�ch trybach: w pierwszym jako czysty interpreter
bytecodu, w drugim przeprowadza "w locie" konwersj� bytecodu na kod
natywny maszyny. Drugi tryb pozwala uruchamia� kod Javy tak szybko jak
kod skompilowany, pozostawiaj�c niezale�no�� kodu od platformy.

%description -l pt_BR
Kaffe � uma m�quina virtual projetada para executar bytecode Java.
Esta m�quina pode ser configurada em dois modos. Em um modo ela opera
como um interpretador puro de bytecode (como a m�quina da JavaSoft);
no segundo modo ela executa convers�o de c�digo "just-in-time" do
c�digo abstrato para o c�digo nativo de m�quina. Isto permite a
execu��o de c�digo Java na mesma velocidade que o c�digo compilado,
com as vantagens da flexibilidade e independ�ncia de c�digo.

%description -l ru
��� -- Kaffe, ����������� ������ ������������� ��� ���������� ��������
Java. ��� ������ ����� ���� ������������ � ���� �������. � ������ ���
�������� ��� "������" ������������ �������� (������� ������ �� JDK/JRE
�� Javasoft'�); �� ������ ������ ��� ��������� ���������� ����
"just-in-time" (�� ���� ����������� �� ������������ ����-���� �
�������� ��� ����� �����������). ��� � ������� ����� ���������
����������, ���������� �� Java, ����������� � ��� �� ��������� ��� �
����������� ����������������� ��� �������� ��� ���� ��� ����������� �
�������� �������-������������ �������.

%description -l uk
�� -- Kaffe, צ�������� ������, ���������� ��� ��������� ��������
Java. �� ������ ���� ���� ����������� � ���� �������. � ������� ����
������ �� "������" ������������� �������� (��� ����, �� ������ �
JDK/JRE צ� Javasoft); � ������� - �����դ ���Ц��æ� "just-in-time"
(���������� � ������������ ����-���� � �������� ��� ����� ����������).
�� � ����̦ ���� ��������� ���������, ��������� �� Java, ������������
� ��� � ����˦���, �� � ����������� ����Ц�������� ���, ���Ҧ����� ���
����� ��� �������� �� ����˦��� �������-����������� Ц�����.

%package devel
Summary:	Headers and libtool files for kaffe
Summary(pl):	Pliki nag��wkowe i skrypty libtoola dla kaffe
Summary(pt_BR):	Bibliotecas e headers de desenvolvimento para o Kaffe
Summary(ru):	������ � ���������� ��� kaffe
Summary(uk):	������ �� ¦�̦����� ��� kaffe
Group:		Development/Languages/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	jikes >= 1.22-2
Provides:	jdk = 1.4

%description devel
Headers and libtool files for kaffe.

%description devel -l pl
Pliki nag��wkowe i skrypty libtoola dla kaffe.

%description devel -l pt_BR
Bibliotecas e headers de desenvolvimento para o Kaffe.

%description devel -l ru
������ � ���������� ��� ���������� � �������������� kaffe (�������
���������� java-��������).

%description devel -l uk
������ �� ¦�̦����� ��� �������� � ������������� kaffe (���������
���Ц��æ� java-�������).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f acinclude.m4
cp -f /usr/share/automake/config.sub scripts
cp -f /usr/share/automake/config.sub kaffe/kaffevm/boehm-gc/boehm
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--enable-ltdl-install=no \
	--with-jredir=%{_jredir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -s %{_bindir}/javac $RPM_BUILD_ROOT%{_jredir}/bin

rm -rf developers/{CVS,glibc-2.1.1-signal.patch,rpm-kaffe.spec} FAQ/CVS
rm -rf $RPM_BUILD_ROOT%{_bindir}/jar

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc FAQ/* ChangeLog* README WHATSNEW
%dir %{_jredir}
%dir %{_jredir}/bin
%attr(755,root,root) %{_jredir}/bin/java
%attr(755,root,root) %{_jredir}/bin/kaffe*
%attr(755,root,root) %{_jredir}/bin/rmiregistry
%dir %{_jredir}/lib
%{_jredir}/lib/gmpjavamath.jar
%{_jredir}/lib/rt.jar
%{_jredir}/lib/*.properties
%{_jredir}/lib/security
%attr(755,root,root) %{_archdir}
%attr(755,root,root) %{_bindir}/appletviewer
%attr(755,root,root) %{_bindir}/install-jar
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/kaffe*
%attr(755,root,root) %{_bindir}/native2ascii
%attr(755,root,root) %{_bindir}/rmi*
%attr(755,root,root) %{_bindir}/serialver
%{_libdir}/awt
%{_mandir}/man1/kaffe.1*

%files devel
%defattr(644,root,root,755)
%doc developers/*
%attr(755,root,root) %{_bindir}/javac
%attr(755,root,root) %{_bindir}/javadoc
%attr(755,root,root) %{_bindir}/javah
%attr(755,root,root) %{_bindir}/javap
%attr(755,root,root) %{_bindir}/jdb
%attr(755,root,root) %{_jredir}/bin/javac
%{_prefix}/lib/tools.jar
%{_includedir}/*
