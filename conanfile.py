from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
import os

class UpCpp(ConanFile):
    name = "up-cpp"
    package_type = "library"
    license = "Apache-2.0 license"
    homepage = "https://github.com/eclipse-uprotocol"
    url = "https://github.com/conan-io/conan-center-index"
    description = "This module contains the data model structures as well as core functionality for building uProtocol"
    topics = ("utransport sdk", "transport")
    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    conan_version = None
    generators = "CMakeDeps", "PkgConfigDeps", "VirtualRunEnv", "VirtualBuildEnv"
    version = "0.1.1-dev"
    exports_sources = "CMakeLists.txt", "up-core-api/*", "include/*" ,"src/*" , "test/*", "cmake/*"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "build_testing": [True, False],
        "build_unbundled": [True, False],
        "build_cross_compiling": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": False,
        "build_testing": False,
        "build_unbundled": False,
        "build_cross_compiling": False,
    }

    def layout(self):
        cmake_layout(self)
        self.folders.build = os.path.join("build", str(self.settings.build_type))
        self.folders.install = "install"

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["BUILD_TESTING"] = self.options.build_testing
        tc.variables["BUILD_UNBUNDLED"] = self.options.build_unbundled
        tc.variables["BUILD_SHARED_LIBS"] = self.options.shared
        tc.variables["CMAKE_INSTALL_PREFIX"] = self.folders.install
        tc.generate()

    def requirements(self):
        self.requires("protobuf/3.21.12" + ("@cross/cross" if self.options.build_cross_compiling else ""))
        self.requires("spdlog/1.13.0")
        if self.options.build_testing:
            self.requires("gtest/1.14.0")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()