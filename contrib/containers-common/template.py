pkgname = "containers-common"
pkgver = "0.56.0"
pkgrel = 0
make_cmd = "gmake"
make_build_args = ["-C", "docs"]
make_install_args = list(make_build_args)
hostmakedepends = ["gmake", "go-md2man"]
pkgdesc = "Shared docs and configs for Containers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/common"
_base_url = url.removesuffix("/common")
_common_ver = pkgver
_storage_ver = "1.50.2"
_image_ver = "5.28.0"
_skopeo_ver = "1.13.3"
_shortnames_ver = "2023.02.20"
source = [
    f"{_base_url}/common/archive/v{_common_ver}.tar.gz",
    f"{_base_url}/storage/archive/v{_storage_ver}.tar.gz",
    f"{_base_url}/image/archive/v{_image_ver}.tar.gz",
    f"{_base_url}/skopeo/archive/v{_skopeo_ver}.tar.gz",
    f"{_base_url}/shortnames/archive/v{_shortnames_ver}.tar.gz",
]
sha256 = [
    "a981ff8746cf193fda0caccb9cd0deac121e334dfa0de6f441ad7ebb267f1109",
    "8ed20cea8cd9bb6ecb63220a0b3f32df63445fe06fb8074c50e3c942e7d1ca0f",
    "89f0aa574f65b1849c57ed2be660fac2cbaec5f43e2e14cdfebb3ff15556fd78",
    "0b788fc5725ac79327f7c29797821a2bafc1c3c87bbfcb2998c2a1be949e314d",
    "336ba679d4e510d2eb59cb11321bf16a36ef2dba58024e79dd76b89ffee539e6",
]
# no tests
options = ["!check"]


def do_build(self):
    self.do("gmake", wrksrc=f"common-{_common_ver}/docs")
    self.do("gmake", wrksrc=f"storage-{_storage_ver}/docs")
    self.do("gmake", "docs", wrksrc=f"image-{_image_ver}")


def do_install(self):
    self.install_dir("etc/containers/certs.d")
    self.install_dir("etc/containers/oci/hooks.d")
    self.install_dir("var/lib/containers/sigstore", empty=True)

    with self.pushd(f"common-{_common_ver}"):
        self.install_file("pkg/config/containers.conf", "etc/containers")
        self.install_file("pkg/config/containers.conf", "usr/share/containers")
        self.install_file("pkg/seccomp/seccomp.json", "etc/containers")
        self.install_file("pkg/seccomp/seccomp.json", "usr/share/containers")
        self.do(
            "gmake",
            "install",
            "PREFIX=/usr",
            f"DESTDIR={self.chroot_destdir}",
            wrksrc="docs",
        )

    with self.pushd(f"storage-{_storage_ver}"):
        self.install_file("storage.conf", "etc/containers")
        self.install_file("storage.conf", "usr/share/containers")
        self.do(
            "gmake", "install", f"DESTDIR={self.chroot_destdir}", wrksrc="docs"
        )

    with self.pushd(f"image-{_image_ver}"):
        self.install_file("registries.conf", "etc/containers")
        self.do("gmake", "install", f"DESTDIR={self.chroot_destdir}")

    with self.pushd(f"skopeo-{_skopeo_ver}"):
        self.install_file(
            "default-policy.json", "etc/containers", name="policy.json"
        )
        self.install_file("default.yaml", "etc/containers/registries.d")

    with self.pushd(f"shortnames-{_shortnames_ver}"):
        self.install_file(
            "shortnames.conf",
            "etc/containers/registries.conf.d",
            name="00-shortnames.conf",
        )
