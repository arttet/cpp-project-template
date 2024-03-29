#pragma once


#if defined(__GNUC__)

#define DO_PRAGMA(X)                  _Pragma(#X)
#define DISABLE_WARNING_PUSH          DO_PRAGMA(GCC diagnostic push)
#define DISABLE_WARNING_POP           DO_PRAGMA(GCC diagnostic pop)
#define DISABLE_WARNING(warning_name) DO_PRAGMA(GCC diagnostic ignored #warning_name)

// clang-format off
#define DISABLE_WARNING_UNREFERENCED_FORMAL_PARAMETER DISABLE_WARNING(-Wunused-parameter)
#define DISABLE_WARNING_UNREFERENCED_FUNCTION         DISABLE_WARNING(-Wunused-function)
// clang-format on

#define DISABLE_WARNING_CONDITIONAL_EXPRESSION_IS_CONSTANT

#elif defined(__clang__)

#define DO_PRAGMA(X)                  _Pragma(#X)
#define DISABLE_WARNING_PUSH          DO_PRAGMA(clang diagnostic push)
#define DISABLE_WARNING_POP           DO_PRAGMA(clang diagnostic pop)
#define DISABLE_WARNING(warning_name) DO_PRAGMA(clang diagnostic ignored #warning_name)

// clang-format off
#define DISABLE_WARNING_UNREFERENCED_FORMAL_PARAMETER DISABLE_WARNING(-Wunused-parameter)
#define DISABLE_WARNING_UNREFERENCED_FUNCTION         DISABLE_WARNING(-Wunused-function)
// clang-format on

#define DISABLE_WARNING_CONDITIONAL_EXPRESSION_IS_CONSTANT

#elif defined(_MSC_VER)

#define DISABLE_WARNING_PUSH            __pragma(warning(push))
#define DISABLE_WARNING_POP             __pragma(warning(pop))
#define DISABLE_WARNING(warning_number) __pragma(warning(disable : warning_number))

#define DISABLE_WARNING_UNREFERENCED_FORMAL_PARAMETER      DISABLE_WARNING(4100)
#define DISABLE_WARNING_CONDITIONAL_EXPRESSION_IS_CONSTANT DISABLE_WARNING(4127)
#define DISABLE_WARNING_UNREFERENCED_FUNCTION              DISABLE_WARNING(4505)

#else

#define DISABLE_WARNING_PUSH
#define DISABLE_WARNING_POP

#define DISABLE_WARNING_UNREFERENCED_FORMAL_PARAMETER
#define DISABLE_WARNING_CONDITIONAL_EXPRESSION_IS_CONSTANT
#define DISABLE_WARNING_UNREFERENCED_FUNCTION

#endif
