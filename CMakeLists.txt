cmake_minimum_required(VERSION 3.3)
 
project(ubitrack_boost_bindings)
 

include(GNUInstallDirs)

set(PROJECT_VER_PATCH 0)
set(PROJECT_VER_MINOR 0)
set(PROJECT_VER_MAJOR 1)
set(ubitrack_boost_bindings_VERSION "${PROJECT_VER_MAJOR}.${PROJECT_VER_MINOR}.${PROJECT_VER_PATCH}")

# define the library
add_library(ubitrack_boost_bindings INTERFACE)
target_compile_definitions(ubitrack_boost_bindings INTERFACE LIBRARY_HEADER_ONLY)

target_include_directories(ubitrack_boost_bindings INTERFACE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)

# install and export the library
 
install(TARGETS ubitrack_boost_bindings
  EXPORT "ubitrack_boost_bindingsTargets"
  INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

include(CMakePackageConfigHelpers)
write_basic_package_version_file("${CMAKE_CURRENT_SOURCE_DIR}/ubitrack_boost_bindingsConfigVersion.cmake"
  VERSION ${ubitrack_boost_bindings_VERSION}
  COMPATIBILITY SameMajorVersion)

install (FILES "ubitrack_boost_bindingsConfig.cmake" "ubitrack_boost_bindingsConfigVersion.cmake"
  DESTINATION lib/cmake/ubitrack_boost_bindings)

install(EXPORT ubitrack_boost_bindingsTargets
	FILE ubitrack_boost_bindingsTargets.cmake
	NAMESPACE ubitrack_boost_bindings::
	DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/ubitrack_boost_bindings
)
