cmake_minimum_required(VERSION 3.20 FATAL_ERROR)

project(cpp-project-template VERSION 0.0.1 LANGUAGES CXX)

############################################################################################

set(CMAKE_CXX_STANDARD 17)
set(CXX_STANDARD_REQUIRED YES)
set(CXX_EXTENSIONS OFF)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
set(CMAKE_INCLUDE_HEADERS_IN_COMPILE_COMMANDS ON)

############################################################################################

if (EXISTS "${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
  include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
  conan_basic_setup()
endif ()

############################################################################################

set(WITH_COVERAGE OFF CACHE BOOL "Enable coverage reporting")
set(WITH_DOC OFF CACHE BOOL "Build documentations")
set(WITH_TESTS OFF CACHE BOOL "Build test suites")

############################################################################################

if ((CMAKE_CXX_COMPILER_ID STREQUAL "Clang") OR (CMAKE_CXX_COMPILER_ID STREQUAL "GNU"))
  add_compile_options(
    "-Wextra"
    "-Wall"
    "-Werror"
  )

  if (WITH_COVERAGE)
    add_compile_options(
      "-O0"
      "-g"
      "--coverage"
    )

    add_link_options(
      "--coverage"
    )
  endif()

  if (CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    add_compile_options(
      "-Wno-c++98-compat"
      "-Wno-c++98-compat-pedantic"
      "-Wno-global-constructors"
      "-Wno-language-extension-token"
      "-Wno-undef"
      "-Wno-shift-sign-overflow"
      "-Wno-unused-command-line-argument"
    )
  endif()
endif()

if (MSVC)
  add_compile_options(
    "/WX"
    "/W4"
    "/EHsc"
  )

  add_compile_definitions(_SCL_SECURE_NO_WARNINGS)
  add_compile_definitions(_SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING)
  add_compile_definitions(_SILENCE_ALL_CXX17_DEPRECATION_WARNINGS)
endif ()

############################################################################################

find_package(absl REQUIRED)
find_package(fmt REQUIRED)

if (WITH_TESTS)
  find_package(GTest REQUIRED)
  find_package(benchmark REQUIRED)
endif()

############################################################################################

add_subdirectory(include)
add_subdirectory(src)

if (WITH_TESTS)
  enable_testing()
  add_subdirectory(test)
endif()

############################################################################################

set_property(GLOBAL PROPERTY USE_FOLDERS ON)

macro(set_folders dir)
    get_property(subdirectories
      DIRECTORY ${dir}
      PROPERTY SUBDIRECTORIES
    )

    foreach(subdir ${subdirectories})
      set_folders(${targets} ${subdir})
    endforeach()

    get_property(current_target
      DIRECTORY ${dir}
      PROPERTY BUILDSYSTEM_TARGETS
    )

    if (TARGET ${current_target})
      string(REPLACE "${CMAKE_SOURCE_DIR}" "" folder ${dir})
      set_target_properties(${current_target}
        PROPERTIES
          FOLDER "${folder}"
      )
    endif()
endmacro()

set_folders(${CMAKE_CURRENT_SOURCE_DIR})

if (WITH_COVERAGE)
  add_custom_target(coverage
      COMMAND $<TARGET_FILE:executable>
      COMMAND $<TARGET_FILE:benchmark_example>
      COMMAND ctest -C $<CONFIGURATION> --output-on-failure
      WORKING_DIRECTORY ${CMAKE_BUILD_DIR}
      VERBATIM
  )
endif()

############################################################################################

include(GNUInstallDirs)

install(FILES LICENSE README.md DESTINATION .)

set(CPACK_PACKAGE_VERSION_MAJOR ${PROJECT_VERSION_MAJOR})
set(CPACK_PACKAGE_VERSION_MINOR ${PROJECT_VERSION_MINOR})
set(CPACK_PACKAGE_VERSION_PATCH ${PROJECT_VERSION_PATCH})

set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_SOURCE_DIR}/LICENSE")
set(CPACK_RESOURCE_FILE_README  "${CMAKE_SOURCE_DIR}/README.md")

set(CPACK_PACKAGE_FILE_NAME "${CMAKE_PROJECT_NAME}-${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}.${PROJECT_VERSION_PATCH}")
include(CPack)
