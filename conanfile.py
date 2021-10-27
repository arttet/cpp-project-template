from conan.tools.cmake import CMake, CMakeToolchain
from conans import ConanFile
from conans.tools import ChocolateyTool, SystemPackageTool, os_info


class ProjectTemplateConan(ConanFile):
    name = "cpp-project-template"
    version = "0.0.1"

    # Optional metadata
    license = "MIT"
    author = "Artyom Tetyukhin"
    url = "https://github.com/arttet/cpp-project-template"
    description = "cpp project template"
    topics = ("cpp")

    # Binary configuration
    build_policy = "missing"
    generators = "CMakeDeps", "CMakeToolchain"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "sanitizer": [None, "ASan", "TSan", "UBSan"],
        "coverage": [True, False],
        "tests": [True, False],

        "system_requirements": [True, False],
        "clang_tidy": "ANY",
        "cppcheck": "ANY",
        "cpplint": "ANY",
        "iwyu": "ANY",
        "lwyu": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "sanitizer": None,
        "coverage": False,
        "tests": False,

        "system_requirements": False,
        "clang_tidy": "",
        "cppcheck": "",
        "cpplint": "",
        "iwyu": "",
        "lwyu": False,
    }

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def requirements(self):
        self.requires("fmt/8.0.1")
        self.requires("ms-gsl/3.1.0")

    def build_requirements(self):
        if self.options.tests:
            self.build_requires("benchmark/1.6.0", force_host_context=True)
            self.build_requires("gtest/1.11.0", force_host_context=True)

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

    def generate(self):
        tc = CMakeToolchain(self)

        tc.variables["CMAKE_CXX_CLANG_TIDY"] = self.options.clang_tidy
        tc.variables["CMAKE_CXX_CPPCHECK"] = self.options.cppcheck
        tc.variables["CMAKE_CXX_CPPLINT"] = self.options.cpplint
        tc.variables["CMAKE_CXX_INCLUDE_WHAT_YOU_USE"] = self.options.iwyu
        tc.variables["CMAKE_LINK_WHAT_YOU_USE"] = self.options.lwyu

        tc.variables["WITH_TESTS"] = self.options.tests

        tc.generate()

    def build(self):
        cmake = CMake(self)

        # https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild-command-line-reference?view=vs-2019
        # cmake.msbuild_verbosity = "normal"
        # cmake.verbose = True

        cmake.configure()
        cmake.build()
