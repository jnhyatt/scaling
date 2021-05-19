cmake_minimum_required (VERSION 3.0)

project (scaling
    VERSION 0.1.0
    LANGUAGES CXX
)

include (${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup (TARGETS)

add_library (scaling src/scaling.cpp)
target_link_libraries (scaling CONAN_PKG::glm)
target_include_directories (scaling
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)
