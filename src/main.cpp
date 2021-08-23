#include <fmt/ranges.h>
#include <gsl/span>

#include <cstdlib>

int main(int argc, char ** argv) // NOLINT
{
    auto const args = gsl::span(argv, size_t(argc));
    fmt::print(u8"Hello, 世界: args = {}", fmt::join(args, ", "));

    return EXIT_SUCCESS;
}
