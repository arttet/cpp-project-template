project(benchmark_example)

add_executable(${PROJECT_NAME})

target_sources(${PROJECT_NAME}
  PRIVATE
    main.cpp
)

target_link_libraries(${PROJECT_NAME}
  PRIVATE
    benchmark::benchmark
)

install(TARGETS ${PROJECT_NAME} DESTINATION test COMPONENT test)
