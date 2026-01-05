pkgname = "libqb"
pkgver = "2.0.9"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["libxml2-devel"]
pkgdesc = "Library providing high performance logging, tracing, ipc, and poll"
license = "LGPL-2.1-only"
url = "http://clusterlabs.github.io/libqb"
source = f"https://github.com/ClusterLabs/libqb/releases/download/v{pkgver}/libqb-{pkgver}.tar.gz"
sha256 = "57288f02c64a67b096fc73641f90db5b885dc1edcdb0e66b6d861c600d4e000d"


@subpackage(f"{pkgname}-devel")
def _(self):
    return self.default_devel()
