cmake_minimum_required(VERSION 3.20 FATAL_ERROR)

project(cpp-project-template VERSION 0.0.1 LANGUAGES CXX)

############################################################################################

set(CMAKE_CXX_STANDARD 17)
set(CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

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

include(CMakePrintHelpers)
cmake_print_variables(WITH_COVERAGE)
cmake_print_variables(WITH_DOC)
cmake_print_variables(WITH_TESTS)

# Linters
cmake_print_variables(CMAKE_CXX_CLANG_TIDY)
cmake_print_variables(CMAKE_CXX_CPPCHECK)
cmake_print_variables(CMAKE_CXX_CPPLINT)
cmake_print_variables(CMAKE_CXX_INCLUDE_WHAT_YOU_USE)
cmake_print_variables(CMAKE_LINK_WHAT_YOU_USE)

# Verbose output
cmake_print_variables(CMAKE_VERBOSE_MAKEFILE)

############################################################################################

if (CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
  add_compile_options(
    "-Wall"
    "-Wextra"
  )

  add_compile_options(
    "-Wno-c++98-compat"
    "-Wno-c++98-compat-pedantic"
  )

  if (CMAKE_CXX_COMPILER_FRONTEND_VARIANT STREQUAL "MSVC")
    # Using clang with clang-cl front end
  elseif (CMAKE_CXX_COMPILER_FRONTEND_VARIANT STREQUAL "GNU")
    # Using clang with regular front end
    add_compile_options(
      "-Werror"
    )
  endif()
elseif (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
  add_compile_options(
    "-Wextra"
    "-Wall"
    "-Werror"
  )
elseif (CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
  add_compile_definitions(
    UNICODE
    _UNICODE

    _SCL_SECURE_NO_WARNINGS
    _SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING
    _SILENCE_ALL_CXX17_DEPRECATION_WARNINGS
  )

  add_compile_options(
    "/WX"
    "/W4"
    "/EHsc"
  )
endif()

############################################################################################

if (CMAKE_CXX_CLANG_TIDY)
  list(APPEND CMAKE_CXX_CLANG_TIDY
    "-format-style='file'"
  )
endif()

if (WITH_COVERAGE)
  add_compile_options(
    "--coverage"
  )

  add_link_options(
    "--coverage"
  )
endif()

############################################################################################

find_package(fmt REQUIRED)
find_package(Microsoft.GSL REQUIRED)

if (WITH_TESTS)
  find_package(benchmark REQUIRED)
  find_package(GTest REQUIRED)
endif()

############################################################################################

enable_testing()

add_subdirectory(include)
add_subdirectory(src)

if (WITH_TESTS)
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

############################################################################################

install(FILES LICENSE DESTINATION licenses)

set(CPACK_PACKAGE_VENDOR "")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "")
set(CPACK_PACKAGE_FILE_NAME "${CMAKE_PROJECT_NAME}-${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}.${PROJECT_VERSION_PATCH}")

set(CPACK_PACKAGE_VERSION_MAJOR ${PROJECT_VERSION_MAJOR})
set(CPACK_PACKAGE_VERSION_MINOR ${PROJECT_VERSION_MINOR})
set(CPACK_PACKAGE_VERSION_PATCH ${PROJECT_VERSION_PATCH})

set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_SOURCE_DIR}/LICENSE")
set(CPACK_RESOURCE_FILE_README  "${CMAKE_SOURCE_DIR}/README.md")

include(CPack)
