from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout ,CMakeToolchain ,CMakeDeps

class ProGeoAcous00Conan(ConanFile):
    name = "Pro"
    version = "0.1"
    license = "MIT"
    author = "Votre Nom <[email protected]>"
    url = "http://votre-url-de-repo.git"
    description = "Projet Pro en C++20"
    topics = ("c++20", "opengl", "glfw", "amp", "eigen", "cdt", "ldr")
    settings = "os", "compiler", "build_type", "arch"
    
    # Dépendance

    def requirements(self):
        self.requires("eigen/3.4.0")
        self.requires("embree/4.3.3")


    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()


    def layout(self):
        cmake_layout(self)  # Obligatoire avec Conan 2.x

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
