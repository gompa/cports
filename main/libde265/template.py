pkgname = "libde265"
pkgver = "1.0.14"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-option-checking"]
configure_gen = ["./autogen.sh"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Open H.265 codec implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "http://www.libde265.org"
source = f"https://github.com/strukturag/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "d368b771823e66715da65ee3213ef9c78c535b65ea6e18f91f347063a2ca0f00"
hardening = ["!cfi"]  # TODO


def post_install(self):
    # do not polute /usr/bin with junk
    for f in [
        "acceleration_speed",
        "bjoentegaard",
        "block-rate-estim",
        "gen-enc-table",
        "rd-curves",
        "tests",
        "yuv-distortion",
    ]:
        self.rm(self.destdir / "usr/bin" / f)


@subpackage("libde265-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libde265-progs")
def _progs(self):
    return self.default_progs()
