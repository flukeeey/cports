pkgname = "vulkan-loader"
pkgver = "1.3.295"
pkgrel = 0
build_style = "cmake"
configure_args = [
    f"-DVULKAN_HEADERS_INSTALL_DIR={self.profile().sysroot / 'usr'}",
    "-DBUILD_TESTS=OFF",  # needs gtest downloaded
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python",
]
makedepends = [
    "gtest-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "libxrandr-devel",
    "vulkan-headers",
    "wayland-devel",
]
pkgdesc = "Vulkan Installable Client Driver (ICD) loader"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Loader/archive/v{pkgver}.tar.gz"
)
sha256 = ["9241b99fb70c6e172cdb8cb4c3d291c129e9499126cfe4c12aa854b71e035518"]
hardening = ["vis", "!cfi"]
# tests disabled
options = ["!check"]


@subpackage("vulkan-loader-devel")
def _(self):
    return self.default_devel()
