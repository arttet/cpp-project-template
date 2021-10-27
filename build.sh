#!/usr/bin/env bash

set -euo pipefail

export Compiler=clang
export Version=13

# export Compiler="Visual Studio"

export Arch=x86_64
export BuildType=Release
# export Toolset=ClangCL
export Runtime=MT
# export Sanitizer=ASan
export Tests=True
# export ClangTidy=clang-tidy

conan install . -if build --build outdated \
    -pr .conan/profiles/profile.jinja -pr:b .conan/profiles/profile.jinja \
    -c tools.cmake.cmaketoolchain:generator=Ninja \
    -e CONAN_CMAKE_GENERATOR=Ninja

conan build . -bf build
