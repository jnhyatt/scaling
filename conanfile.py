from conans import ConanFile, CMake, tools

class ScalingConan(ConanFile):
    name = "scaling"
    version = "0.1"
    license = "MIT License"
    author = "Joshua Hyatt joshua.n.hyatt@gmail.com"
    url = "github.com/jnhyatt/scaling"
    description = "Scales GLM vectors"
    topics = ("Math", "OpenGL")
    settings = "os", "compiler", "build_type", "arch"
    requires = "glm/0.9.9.8"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run("git clone https://github.com/jnhyatt/scaling")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="scaling")
        cmake.build()

    def package(self):
        slef.copy("include/", dst="include", src="scaling")
        self.copy("*scaling.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["scaling"]

