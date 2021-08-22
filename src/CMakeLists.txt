project(executable)

add_executable(${PROJECT_NAME})

target_sources(${PROJECT_NAME}
  PRIVATE
    main.cpp
)

target_link_libraries(${PROJECT_NAME}
  PRIVATE
    fmt::fmt
    Microsoft.GSL::GSL
)

add_test(
  NAME system_${PROJECT_NAME}
  COMMAND ${PROJECT_NAME}
)

install(
  TARGETS ${PROJECT_NAME}
  DESTINATION bin
  COMPONENT client
)
