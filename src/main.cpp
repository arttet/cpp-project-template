#include <cpp-project-template/error/disable_warning.h>

DISABLE_WARNING_PUSH
DISABLE_WARNING_CONDITIONAL_EXPRESSION_IS_CONSTANT
#include <absl/strings/str_join.h>
DISABLE_WARNING_POP

#include <fmt/core.h>
#include <fmt/ranges.h>

#include <cstdlib>
#include <vector>

int main()
{
    std::vector<std::string> const v = {"foo", "bar", "baz"};
    std::string const s = absl::StrJoin(v, "-");

    fmt::print("{}\n", v);
    fmt::print("{}\n", s);

    return EXIT_SUCCESS;
}
