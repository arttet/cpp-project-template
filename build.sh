#!/usr/bin/env bash

conan install . -g visual_studio --install-folder build --build=outdated -s arch_target=x86_64 -s build_type=Debug -s compiler.cppstd=17 -s compiler.version=16 -s compiler="Visual Studio" -s compiler.runtime=MTd -o with_tests=True -e CC=cl -e CXX=cl
conan build . -bf=build
