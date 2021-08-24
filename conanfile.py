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

        "system_requirements": [True, False],

        "clang_tidy": "ANY",
        "cppcheck": "ANY",
        "cpplint": "ANY",
        "iwyu": "ANY",
        "lwyu": [True, False],

        "coverage": [True, False],
        "tests": [True, False],
    }

    default_options = {
        "shared": False,
        "fPIC": True,

        "system_requirements": True,

        "clang_tidy": "",
        "cppcheck": "",
        "cpplint": "",
        "iwyu": "",
        "lwyu": False,

        "coverage": False,
        "tests": False,
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
        if self.options.tests:
            self.build_requires("benchmark/1.5.6", force_host_context=True)
            self.build_requires("gtest/1.11.0", force_host_context=True)

    def build_id(self):
        pass

    def system_requirements(self):
        if not self.options.system_requirements:
            return

        packages = []
        if self.options.clang_tidy:
            packages.append(
                "llvm" if os_info.is_windows else f"{self.options.clang_tidy}")

        if self.options.cppcheck:
            packages.append("cppcheck")

        if self.options.cpplint:
            packages.append("cpplint")

        if self.options.iwyu:
            packages.append("include-what-you-use")

        if self.options.coverage:
            packages.append("lcov")

        if os_info.is_windows:
            installer = SystemPackageTool(tool=ChocolateyTool())
        else:
            installer = SystemPackageTool()

        if packages:
            installer.install_packages(packages)

    def source(self):
        pass

    def imports(self):
        pass

    def build(self):
        cmake = CMake(self)

        # https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild-command-line-reference?view=vs-2019
        # cmake.msbuild_verbosity = "normal"
        # cmake.verbose = True

        cmake.definitions["CMAKE_CXX_CLANG_TIDY"] = self.options.clang_tidy
        cmake.definitions["CMAKE_CXX_CPPCHECK"] = self.options.cppcheck
        cmake.definitions["CMAKE_CXX_CPPLINT"] = self.options.cpplint
        cmake.definitions["CMAKE_CXX_INCLUDE_WHAT_YOU_USE"] = self.options.iwyu
        cmake.definitions["CMAKE_LINK_WHAT_YOU_USE"] = self.options.lwyu

        cmake.definitions["WITH_COVERAGE"] = self.options.coverage
        cmake.definitions["WITH_TESTS"] = self.options.tests

        cmake.configure()
        cmake.build()

    def package(self):
        pass

    def package_info(self):
        pass

    def deploy(self):
        pass
