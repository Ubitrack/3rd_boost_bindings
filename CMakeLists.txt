cmake_minimum_required(VERSION 3.3)
 
project(ut_boost_bindings)
 
# define the library
add_library(boost_bindings INTERFACE)
target_compile_definitions(boost_bindings
    INTERFACE LIBRARY_HEADER_ONLY
)

 
# install and export the library
 
install(DIRECTORY
    boost
  DESTINATION
    include/boost
)

install(TARGETS
    boost_bindings
  EXPORT library_targets
  INCLUDES DESTINATION include
)

install(EXPORT library_targets
  NAMESPACE ubitrack_boost_bindings::
  DESTINATION lib/cmake/ubitrack_boost_bindings
)
 
install(FILES ubitrack_boost_bindings-config.cmake
  DESTINATION lib/cmake/ubitrack_boost_bindings
)
