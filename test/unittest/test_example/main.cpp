#include <gtest/gtest.h>

using TestIntSuite = ::testing::TestWithParam<int>;
using TestPairSuite = ::testing::TestWithParam<std::tuple<int, char>>;

TEST_P(TestIntSuite, Init)
{
    int const x = GetParam();
    EXPECT_EQ(x, x);
}

TEST_P(TestPairSuite, Init)
{
    auto const [x, y] = GetParam();
    EXPECT_EQ(x + y, y + x);
}

// clang-format off
INSTANTIATE_TEST_SUITE_P(TestRange, TestIntSuite, ::testing::Range(
    97, 105
));

INSTANTIATE_TEST_SUITE_P(TestValuesIn, TestIntSuite, ::testing::ValuesIn({
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
}));

INSTANTIATE_TEST_SUITE_P(TestCombine, TestPairSuite, ::testing::Combine(
    ::testing::Values(97, 122),
    ::testing::Values('a', 'z')
));

INSTANTIATE_TEST_SUITE_P(TestValuesInWithTuple, TestPairSuite, ::testing::ValuesIn({
    std::tuple{97, 'a'}, std::tuple{122, 'z'},
}));
// clang-format on

int main(int argc, char ** argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
