#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform

from conans import tools, ConanFile, CMake


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
    }

    default_options = {
        "shared": False,
        "fPIC": True,
    }

    generators = "cmake", "cmake_find_package"
    build_policy = "missing"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        pass

    def requirements(self):
        pass

    def package_id(self):
        pass

    def build_requirements(self):
        pass

    def build_id(self):
        pass

    def system_requirements(self):
        pass

    def source(self):
        pass

    def imports(self):
        pass

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.names["cmake_find_package"] = "cpp-project-template"
        self.cpp_info.names["cmake_find_package_multi"] = "cpp-project-template"

    def deploy(self):
        pass
