#!/usr/bin/env bash

set -euo pipefail

version=12
apt-get install llvm-${version}-dev libclang-${version}-dev clang-${version}

source=include-what-you-use-0.16
build=${source}/build

wget -O ${source}.tar.gz https://github.com/include-what-you-use/include-what-you-use/archive/refs/tags/0.16.tar.gz
tar -xzf ${source}.tar.gz

CC="clang-${version}" CXX="clang++-${version}" cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=/usr/lib/llvm-${version} -S ${source} -B ${build}
cmake --build ${build}
cmake --install ${build}
