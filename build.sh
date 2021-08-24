#!/usr/bin/env bash

set -euo pipefail

# # ClangCL
# conan install . -g cmake -if build -b outdated \
#     -s build_type=Debug -s arch_target=x86_64 -s compiler.cppstd=17 \
#     -s compiler.version=16 -s compiler="Visual Studio" -s compiler.runtime=MTd -s compiler.toolset=ClangCL \
#     -e CC=clang-cl -e CXX=clang-cl \
#     -o tests=True

# Clang
conan install . -g cmake -if build -b outdated \
    -s build_type=Debug -s arch_target=x86_64 -s compiler.cppstd=17 \
    -s compiler.version=12 -s compiler=clang \
    -e CC=clang -e CXX=clang++ -e CONAN_CMAKE_GENERATOR=Ninja \
    -e CXXFLAGS="-Wno-unused-command-line-argument -Wno-microsoft-enum-value" \
    -o tests=True \
    # -o system_requirements=False \
    # -o clang_tidy="clang-tidy" \
    # -o cppcheck=cppcheck \
    # -o cpplint=cpplint \

# # Visual Studio
# conan install . -g cmake -if build -b outdated \
#     -s build_type=Debug -s arch_target=x86_64 -s compiler.cppstd=17 \
#     -s compiler.version=16 -s compiler="Visual Studio" -s compiler.runtime=MTd -s compiler.toolset=v142 \
#     -o tests=True

conan build . -bf build
