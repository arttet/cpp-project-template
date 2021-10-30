#include <benchmark/benchmark.h>

void benchmark_string_creation(benchmark::State & state)
{
    while (state.KeepRunning()) { // NOLINT (altera-unroll-loops)
        std::string const empty_string;
    }
}

void benchmark_string_copy(benchmark::State & state)
{
    std::string x = "hello";
    while (state.KeepRunning()) { // NOLINT (altera-unroll-loops)
        std::string copy(x);      // NOLINT (performance-unnecessary-copy-initialization)
    }
}

BENCHMARK(benchmark_string_creation); // NOLINT
BENCHMARK(benchmark_string_copy);     // NOLINT

BENCHMARK_MAIN(); // NOLINT
