# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Rocshmem(CMakePackage):
    """rocSHMEM intra-kernel networking runtime for AMD dGPUs on the ROCm platform."""

    homepage = "https://github.com/ROCm/rocSHMEM"
    # url = "https://github.com/ROCm/rocSHMEM/archive/refs/tags/rocm-6.4.0.tar.gz"
    git = "https://github.com/ROCm/rocm-systems.git"
    tags = ["rocm"]

    maintainers("afzpatel", "srekolam", "renjithravindrankannath")

    license("MIT")

    version("develop", branch=develop)

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on(f"rocm-core")

    # depends_on("ucx@1.17: +rocm")
    depends_on("cray-mpich-gtl +rocm")

    def cmake_args(self):
        args = []
        args.append(self.define("ROCM_PATH", self.spec["rocm-core"].prefix))
        args.append()
        return args
