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

        "with_coverage": [True, False],
        "with_tests": [True, False],
    }

    default_options = {
        "shared": False,
        "fPIC": True,

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
        self.requires("abseil/20210324.2")
        self.requires("fmt/8.0.1")

    def package_id(self):
        pass

    def build_requirements(self):
        if self.options.with_tests:
            self.build_requires("gtest/1.11.0", force_host_context=True)
            self.build_requires("benchmark/1.5.5", force_host_context=True)

    def build_id(self):
        pass

    def system_requirements(self):
        packages = []

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
