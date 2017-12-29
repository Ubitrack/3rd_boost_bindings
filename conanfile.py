from conans import ConanFile, tools
import os


class UbitrackboostbindingsConan(ConanFile):
    name = "ubitrack_boost_bindings"
    version = "1.0"
    license = "https://mathema.tician.de/software/boost-numeric-bindings/"
    url = "https://github.com/Ubitrack/3rd_boost_bindings"
    description = "Boost Bindings is a bindings library (not just) for Boost.Ublas. It offers an easy way of calling BLAS, LAPACK, UMFPACK, MUMPS and many other mature legacy numerical codes from within C++."
    no_copy_source = True
    exports_sources = "include/*"
    # No settings/options are necessary, this is header only

    def package(self):
        self.copy("*.h")

    def package_id(self):
        self.info.header_only()