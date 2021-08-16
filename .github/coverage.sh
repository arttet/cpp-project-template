#!/bin/bash

set -euo pipefail

find . -type f -name "*.gcda" -exec lcov --directory {} --capture --output-file $(basename {}).info \;
find . -type f -name "*.gcno" -exec lcov --directory {} --capture --output-file $(basename {}).info \;
find . -type f -name "*.info" -exec echo "--add-tracefile {}" \; | xargs lcov --output-file coverage.info

lcov --remove coverage.info '/usr/*' "${HOME}"'/.conan/*' --output-file coverage.info
lcov --list coverage.info

genhtml -o report coverage.info
