# Uprotocol C++ Library 

## Welcome!

This is the C++ library that extends up-core-api to provide serializers, validators, and language specific interface definitions for uProtocol. 

*_IMPORTANT NOTE:_ This project is under active development*

The core functional factory methods that make it more intuitive to create URIs that are used to configure source and sink (destination) elements in the uProtocol and additional helper methods.


## Getting Started

The library is built and packaged using conan dependency management. 

### Requirements:
- Compiler: GCC/G++ 11 or Clang 13
- Conan : 1.59 or latest 2.X
- Ubuntu 22.04

## How to Use the Library
To add up-cpp to your conan build dependencies, simply add the following to your conanfile.txt:
```
[requires]
up-cpp/0.1

[generators]
CMakeDeps
CMakeToolchain

[layout]
cmake_layout
```
**NOTE:** If using conan version 1.59 Ensure that the conan profile is configured to use ABI 11 (libstdc++11: New ABI.) standards according to https://docs.conan.io/en/1.60/howtos/manage_gcc_abi.html

## How to Build 
The following steps are only required to locally build and test up-cpp, if you are a user of up-cpp, you only need to follow the _How to Use the Library_ section above. 
### Setup SDK local repository, build and test
```
$ git clone https://github.com/eclipse-uprotocol/up-cpp.git
$ git submodule update --init --recursive
```

### Building locally 

#### Using Conan for build

Most will probably be fine building using Conan as follows:
```
$ cd up-cpp
$ conan build . --build=missing -o build_testing=True
```
Places the build artifacts in `up-cpp/build/Release`.

#### Using Conan for dependencies only

If you need to, you can use Conan to only install dependencies
and scaffold out for building using CMake.
```
$ cd up-cpp
$ conan install . --build=missing -o build_testing=True
$ cmake --preset conan-release
$ cd build
$ cmake --build Release --target install -- -j
```

### Creating conan package locally 

If you need to create a release package for conan, please follow the steps below.
```
$ cd up-cpp/conan-recipes
$ conan create .. --build=missing
```
Installs the `up-cpp` package in your local conan cache.
* `~/.conan` if using Conan 1.59
* `~/.conan2` if using Conan 2.X

## Show your support

Give a ⭐️ if this project helped you!
