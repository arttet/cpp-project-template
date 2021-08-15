project(executable)

add_executable(${PROJECT_NAME})

target_sources(${PROJECT_NAME}
  PRIVATE
    main.cpp
)

target_link_libraries(${PROJECT_NAME}
  PRIVATE
    absl::absl
    fmt::fmt

    cpp-project-template-interface
)

install(
  TARGETS ${PROJECT_NAME}
  DESTINATION bin 
  COMPONENT client
)
