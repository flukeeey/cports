pkgname = "python-braceexpand"
pkgver = "0.1.7"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Bash-style brace expansion for Python"
license = "MIT"
url = "https://github.com/trendels/braceexpand"
source = f"https://files.pythonhosted.org/packages/54/93/badd4f5ccf25209f3fef2573073da9fe4a45a3da99fca2f800f942130c0f/braceexpand-{pkgver}.tar.gz"
sha256 = "e6e539bd20eaea53547472ff94f4fb5c3d3bf9d0a89388c4b56663aba765f705"


def post_install(self):
    self.install_license("LICENSE")
