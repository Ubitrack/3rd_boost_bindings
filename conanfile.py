from conans import ConanFile, tools
import os


class UbitrackboostbindingsConan(ConanFile):
    name = "ubitrack_boost_bindings"
    version = "1.0"
    license = "https://mathema.tician.de/software/boost-numeric-bindings/"
    url = "https://github.com/Ubitrack/3rd_boost_bindings"
    description = "Boost Bindings is a bindings library (not just) for Boost.Ublas. It offers an easy way of calling BLAS, LAPACK, UMFPACK, MUMPS and many other mature legacy numerical codes from within C++."
    no_copy_source = True
    # No settings/options are necessary, this is header only

    def source(self):
        '''retrieval of the source code here. Remember you can also put the code in the folder and
        use exports instead of retrieving it with this source() method
        '''
        #self.run("git clone ...") or
        #tools.download("url", "file.zip")
        #tools.unzip("file.zip" )

    def package(self):
        self.copy("*.h", dst="include/boost", src="boost")
