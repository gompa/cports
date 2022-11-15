pkgname = "gnome-shell-extensions"
pkgver = "43.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "gettext-tiny"]
depends = [f"gnome-shell~{pkgver[:-2]}", "nautilus", "gnome-menus"]
pkgdesc = "Optional extensions for GNOME shell"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/GnomeShell/Extensions"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "adde04bd946a13113557e4c34c890bbe9077505a6a3f0755f17bea1c6e4a2d17"
