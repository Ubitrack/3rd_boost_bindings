from conans import ConanFile, CMake, tools
import os


class UbitrackboostbindingsConan(ConanFile):
    name = "ubitrack_boost_bindings"
    version = "1.0"
    settings = "os", "compiler", "arch", "build_type"
    license = "https://mathema.tician.de/software/boost-numeric-bindings/"
    url = "https://github.com/Ubitrack/3rd_boost_bindings"
    description = "Boost Bindings is a bindings library (not just) for Boost.Ublas. It offers an easy way of calling BLAS, LAPACK, UMFPACK, MUMPS and many other mature legacy numerical codes from within C++."
    no_copy_source = True
    exports_sources = "include/*", "CMakeLists.txt", "ubitrack_boost_bindingsConfig.cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_id(self):
        self.info.header_only()