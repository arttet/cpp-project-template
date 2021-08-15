project(cpp-project-template-interface)

add_library(${PROJECT_NAME} INTERFACE)

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
  DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
  FILES_MATCHING PATTERN "*.h"
)
