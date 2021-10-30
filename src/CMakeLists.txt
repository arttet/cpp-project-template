project(project-template)

add_executable(${PROJECT_NAME})

target_sources(${PROJECT_NAME}
  PRIVATE
    main.cpp
)

target_link_libraries(${PROJECT_NAME}
  PRIVATE
    fmt::fmt
    Microsoft.GSL::GSL

    ${CMAKE_PROJECT_NAME}::include
    ${CMAKE_PROJECT_NAME}::lib-template
)

add_test(
  NAME ${PROJECT_NAME}
  COMMAND ${PROJECT_NAME}
)

install(
  TARGETS ${PROJECT_NAME}
  DESTINATION ${CMAKE_INSTALL_BINDIR}
  COMPONENT Runtime
)
