vcpkg_from_git(
    OUT_SOURCE_PATH SOURCE_PATH
    URL             "git@github.com:y0sshi/vcpkg-lib-example.git"
    REF             bad830a277e346f4eb6935e0ad29be4b72d9b554  ## you can also set tag
    HEAD_REF        main
    )

vcpkg_cmake_configure(
    SOURCE_PATH "${SOURCE_PATH}"
    WINDOWS_USE_MSBUILD
    OPTIONS
        -DCMAKE_INSTALL_PREFIX=${CURRENT_PACKAGES_DIR}
        -DBUILD_SHARED_LIBS=ON
        -BUILD_TESTING=OFF
    )

vcpkg_cmake_install()
vcpkg_cmake_config_fixup(CONFIG_PATH lib/cmake/vcpkg-lib-example)
vcpkg_copy_pdbs()

file(INSTALL "${CMAKE_CURRENT_LIST_DIR}/usage"
    DESTINATION "${CURRENT_PACKAGE_DIR}/share/${PORT}")
file(REMOVE_RECURSE "${CURRENT_PACKAGE_DIR}/debug/include")
file(WRITE
    "${CURRENT_PACKAGE_DIR}/share/${PORT}/copyright"
    "Copyright (c) 2025 Naofumi, Yoshinaga\n")


# ==================================================
# The following settings are required in case of Header-Only library.
# ==================================================
#vcpkg_fixup_pkgconfig()
#set(VCPKG_POLICY_EMPTY_PACKAGE enabled)
#set(VCPKG_POLICY_HEADER_ONLY   enabled)

