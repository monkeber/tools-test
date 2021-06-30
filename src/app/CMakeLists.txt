project(tools-test)

set(${PROJECT_NAME}_INCLUDES
    include/test_class.h
    include/sub_test_folder/sub_test_class.h
)

set(${PROJECT_NAME}_SOURCES
    src/main.cpp
)

source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR}
    FILES
        ${${PROJECT_NAME}_INCLUDES} ${${PROJECT_NAME}_SOURCES}
)

add_executable(${PROJECT_NAME}
    ${${PROJECT_NAME}_INCLUDES}
    ${${PROJECT_NAME}_SOURCES}
)

# Folder property is assigned to the target after its creation, in our case it is the executable.
set_target_properties(${PROJECT_NAME} PROPERTIES FOLDER executables)
