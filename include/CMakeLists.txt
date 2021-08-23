project(include)

add_library(${PROJECT_NAME} INTERFACE)
add_library(${CMAKE_PROJECT_NAME}::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

target_sources(${PROJECT_NAME}
  PRIVATE
    cpp-project-template/error/disable_warning.h
)

target_include_directories(${PROJECT_NAME}
  INTERFACE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
    $<INSTALL_INTERFACE:include>
)

install(
  DIRECTORY ${CMAKE_PROJECT_NAME}
  DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
  COMPONENT Development
)

install(
  TARGETS ${PROJECT_NAME}
  EXPORT ${PROJECT_NAME}-target
  COMPONENT Development
)

install(
  EXPORT ${PROJECT_NAME}-target
  FILE ${PROJECT_NAME}-target.cmake
  NAMESPACE ${CMAKE_PROJECT_NAME}::
  DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/${CMAKE_PROJECT_NAME}/cmake
  COMPONENT Development
)
