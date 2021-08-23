#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake
from conans.tools import os_info, SystemPackageTool, ChocolateyTool


class UtilsConan(ConanFile):
    name = "cpp-project-template"
    version = "0.0.1"
    description = "cpp project template"
    homepage = "https://github.com/arttet/cpp-project-template"
    license = "MIT"
    author = "Artyom Tetyukhin"
    settings = "os", "arch", "compiler", "build_type"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],

        "with_clang_tidy": "ANY",
        "with_cppcheck": "ANY",
        "with_cpplint": "ANY",
        "with_iwyu": "ANY",
        "with_lwyu": [True, False],

        "with_coverage": [True, False],
        "with_tests": [True, False],
    }

    default_options = {
        "shared": False,
        "fPIC": True,

        "with_clang_tidy": "",
        "with_cppcheck": "",
        "with_cpplint": "",
        "with_iwyu": "",
        "with_lwyu": False,

        "with_coverage": False,
        "with_tests": False,
    }

    generators = "cmake", "cmake_find_package"
    build_policy = "missing"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        pass

    def requirements(self):
        self.requires("fmt/8.0.1")
        self.requires("ms-gsl/3.1.0")

    def package_id(self):
        pass

    def build_requirements(self):
        if self.options.with_tests:
            self.build_requires("benchmark/1.5.6", force_host_context=True)
            self.build_requires("gtest/1.11.0", force_host_context=True)

    def build_id(self):
        pass

    def system_requirements(self):
        packages = []

        if self.options.with_clang_tidy != "" and os_info.is_linux:
            packages.append(self.options.with_clang_tidy)

        if self.options.with_coverage and os_info.is_linux:
            packages.append("lcov")

        if os_info.is_windows:
            installer = SystemPackageTool(tool=ChocolateyTool())
        else:
            installer = SystemPackageTool()

        if packages:
            installer.install(packages)

    def source(self):
        pass

    def imports(self):
        pass

    def build(self):
        cmake = CMake(self)

        # https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild-command-line-reference?view=vs-2019
        # cmake.msbuild_verbosity = "normal"
        # cmake.verbose = True

        cmake.definitions["CMAKE_CXX_CLANG_TIDY"] = self.options.with_clang_tidy
        cmake.definitions["CMAKE_CXX_CPPCHECK"] = self.options.with_cppcheck
        cmake.definitions["CMAKE_CXX_CPPLINT"] = self.options.with_cpplint
        cmake.definitions["CMAKE_CXX_INCLUDE_WHAT_YOU_USE"] = self.options.with_iwyu
        cmake.definitions["CMAKE_LINK_WHAT_YOU_USE"] = self.options.with_lwyu

        cmake.definitions["WITH_COVERAGE"] = self.options.with_coverage
        cmake.definitions["WITH_TESTS"] = self.options.with_tests

        cmake.configure()
        cmake.build()

    def package(self):
        pass

    def package_info(self):
        pass

    def deploy(self):
        pass
