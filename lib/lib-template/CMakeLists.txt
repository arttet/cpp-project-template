project(lib-template)
set(PROJECT_PATH lib_template)

add_library(${PROJECT_NAME})
add_library(${CMAKE_PROJECT_NAME}::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

include(GenerateExportHeader)
GENERATE_EXPORT_HEADER(${PROJECT_NAME}
    EXPORT_FILE_NAME _public/${PROJECT_PATH}/export.h
)

target_include_directories(${PROJECT_NAME}
  PUBLIC
    $<BUILD_INTERFACE:${PROJECT_BINARY_DIR}/_public>
    $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
)

target_link_libraries(${PROJECT_NAME}
  PRIVATE
    ${CMAKE_PROJECT_NAME}::include
)

target_sources(${PROJECT_NAME}
  PRIVATE
    src/lib_template.cpp
)

install(
  FILES
    ${PROJECT_BINARY_DIR}/_public/${PROJECT_PATH}/export.h
    include/${PROJECT_PATH}/lib_template.h
  DESTINATION
    ${CMAKE_INSTALL_INCLUDEDIR}/${CMAKE_PROJECT_NAME}/${PROJECT_PATH}
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
