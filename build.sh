#!/usr/bin/env bash

set -euo pipefail

# export Compiler=clang
# export Version=13
# export Runtime=MT
# export ClangTidy=clang-tidy

export Compiler=msvc
export Runtime=static
export RuntimeType=Debug

# export Arch=x86_64
export BuildType=Debug
export Sanitizer=ASan
export Tests=True

conan install . -if build --build outdated \
    -pr .conan/profiles/profile.jinja \
    -pr:b .conan/profiles/profile.jinja \
    -c tools.cmake.cmaketoolchain:generator=Ninja

conan build . -bf build
