Summary: A free virtual machine for running Java(TM) code.
Name: kaffe
Version: 1.0.b4
Release: 2
Copyright: GPL
Url: http://www.kaffe.org/
Group: Development/Languages
Source0: ftp://ftp.transvirtual.com/pub/kaffe/kaffe-%{version}.tar.gz
Patch: kaffe-alpha.patch
Patch2: kaffe-perlpath.patch
Obsoletes: kaffe-bissawt
Buildroot: /var/tmp/kaffe-root

%description
Kaffe is a free virtual machine designed to execute Java(TM) bytecode.
Kaffe can be configured in two modes.  In the first mode, it operates as
a pure bytecode interpreter (not unlike Javasoft's machine).  In the
second mode, it performs "just-in-time" code conversion from the abstract
code to the host machine's native code.  The second mode will ultimately
allow execution of Java code at the same speed as standard compiled code,
while also maintaining the advantages and flexibility of code independence.

Install the kaffe package if you need a Java virtual machine.

%prep
%setup -q -n kaffe-1.0b4
%patch -p1 -b .alpha
%patch2 -p1
%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --libdir=/usr/lib/kaffe \
	--libexecdir=/usr/lib/kaffe
# hack hack hack
make || {
  cp -l kaffe/kaffevm/intrp/icode.h kaffe/kaffevm/jit
  make
 }

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr libdir=$RPM_BUILD_ROOT/usr/lib/kaffe \
	libexecdir=$RPM_BUILD_ROOT/usr/lib/kaffe \
	nativedir=$RPM_BUILD_ROOT/usr/lib/kaffe \
	classdir=$RPM_BUILD_ROOT/usr/share/kaffe install
#make prefix=$RPM_BUILD_ROOT/usr libdir=$RPM_BUILD_ROOT/usr/lib/kaffe \
#	libexecdir=$RPM_BUILD_ROOT/usr/lib/kaffe \
#	nativedir=$RPM_BUILD_ROOT/usr/lib/kaffe \
#	classdir=$RPM_BUILD_ROOT/usr/share/kaffe check
strip $RPM_BUILD_ROOT/usr/bin/* || echo
strip $RPM_BUILD_ROOT/usr/lib/kaffe/Kaffe
%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README FAQ license.terms developers
/usr/lib/kaffe
/usr/bin/*
/usr/man/*/*
/usr/share/kaffe
/usr/include/kaffe
