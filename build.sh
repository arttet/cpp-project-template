#!/usr/bin/env bash

set -euo pipefail

# ClangCL
# conan install . -g cmake -if build -b outdated -s arch_target=x86_64 -s build_type=Debug -s compiler.cppstd=17 -s compiler.version=16 -s compiler="Visual Studio" -s compiler.runtime=MTd -s compiler.toolset=ClangCL -e CC=clang-cl -e CXX=clang-cl -o with_tests=True

# Clang
conan install . -g cmake -if build -b outdated -s arch_target=x86_64 -s build_type=Debug -s compiler.cppstd=17 -s compiler.version=12 -s compiler=clang -e CC=clang -e CXX=clang++ -e CONAN_CMAKE_GENERATOR=Ninja -e CXXFLAGS="-Wno-unused-command-line-argument -Wno-microsoft-enum-value" -o with_clang_tidy="clang-tidy" -o with_lwyu=True # -o with_tests=True

# Visual Studio
# conan install . -g cmake -if build -b outdated -s arch_target=x86_64 -s build_type=Debug -s compiler.cppstd=17 -s compiler.version=16 -s compiler="Visual Studio" -s compiler.runtime=MTd -s compiler.toolset=v142 -o with_tests=True

conan build . -bf build
