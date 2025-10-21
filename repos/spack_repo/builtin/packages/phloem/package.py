# Copyright 2023 Lawrence Livermore National Security, LLC and other
# Benchpark Project Developers. See the top-level COPYRIGHT file for details.
# Initially developed by August Knox for LLNL.
# 
# SPDX-License-Identifier: Apache-2.0

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *

class Phloem(MakefilePackage):
    """MPI Benchmarks featuring subcommunicator collectives and topological network performance
    graphs."""

    url = "https://github.com/LLNL/phloem/archive/refs/tags/v1.4.5.tar.gz"
    git = "https://github.com/LLNL/phloem"

    maintainers("nhanford", "cchambreau")

    version("master", branch="master")
    version("1.4.5", tag="v1.4.5")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("mpi")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        mkdir(prefix.doc)
        install("mpigraph-1.6/mpiBench/mpiBench", prefix.bin)
        install("sqmr-1.1.0/sqmr", prefix.bin)
        install("mpigraph-1.6/mpiGraph/mpiGraph", prefix.bin)
        install("presta-1.3.0/com", prefix.bin)
        install("presta-1.3.0/bw.message.sizes", prefix.bin)
        install("presta-1.3.0/latency.message.sizes", prefix.bin)
        install("README", prefix.doc)
