pkgname = "usbguard"
pkgver = "1.1.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--with-crypto-library=sodium",
    "--without-bundled-catch",
    "--without-bundled-pegtl",
    "--without-dbus",
    "--without-ldap",
    "--without-polkit",
]
hostmakedepends = ["automake", "gsed", "slibtool", "pkgconf"]
makedepends = [
    "catch2-devel",
    "dinit-chimera",
    "libcap-ng-devel",
    "libqb-devel",
    "libseccomp-devel",
    "libsodium-devel",
    "pegtl-devel",
    "protobuf-devel",
]
pkgdesc = (
    "Software framework for implementing USB device authorization policies"
)
license = "GPL-2.0-or-later"
url = "https://usbguard.github.io"
source = f"https://github.com/USBGuard/usbguard/releases/download/usbguard-{pkgver}/usbguard-{pkgver}.tar.gz"
sha256 = "7d76b75e779e3c9e6c2fc10e7389dfa34056864c9f0c6eaca722687b7e75893c"
hardening = ["vis", "cfi"]
# todo: test-unit failed
options = ["!check"]
exec_wrappers = [("/usr/bin/gsed", "sed")]


def post_prepare(self):
    with open(self.cwd / "usbguard-tmpfiles.conf", "a") as f:
        # Why doesn't upstream add these rules already? The daemon requires
        # them anyway.
        f.write("d /etc/usbguard/rules.d 0700 root root -\n")
        f.write("d /etc/usbguard/IPCAccessControl.d 0700 root root -\n")


def post_install(self):
    self.install_service(self.files_path / "usbguard-daemon")
    self.install_completion("scripts/usbguard-zsh-completion", "zsh")


@subpackage(f"{pkgname}-devel")
def _(self):
    return self.default_devel()
