pkgname = "pegtl"
pkgver = "3.2.8"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Parsing Expression Grammar Template Library"
license = "MIT"
url = "https://github.com/taocpp/PEGTL"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "319e8238daebc3a163f60c88c78922a8012772076fdd64a8dafaf5619cd64773"
hardening = ["vis", "cfi"]
# todo: 1 failure
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage(f"{pkgname}-devel")
def _(self):
    return self.default_devel()
