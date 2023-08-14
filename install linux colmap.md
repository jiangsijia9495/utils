COLMAP is a Structure-from-Motion and Multiple-View Stereo software that reconstructs 3D representation of objects from a series of 2D images. The building steps here basically follow the official documents, with a little bit modification for the target platform.

An NVIDIA GPU of the Turing architecture is used on the tested machine.

Install CUDA
COLMAP depends on CUDA. The latest version is CUDA 11, which also supports the Turing architecture. Follow the steps to install (source):

Install an NVIDIA driver
Open “Software & Updates”.
At the “Additional Drivers” tab, check the first option, “Using NVIDIA driver metapackage from nvidia-driver-455 (proprietary, tested)”.
Click “Apply Changes” to install the driver.
Install an NVIDIA CUDA Toolkit
Run sudo apt install nvidia-cuda-toolkit to install the CUDA Toolkit, which is version 11 on Ubuntu 20.10 and supports the Turing architecture.
Open ~/.bashrc in a text editor, and add a new line export CUDA_PATH=/usr at the end of the file.
Run source ~/.bashrc to make the change take effect.
Build CUDA samples (optional)
Build the official CUDA samples to test if CUDA has been successfully installed.

sudo apt install git build-essential
git clone https://github.com/NVIDIA/cuda-samples.git
cd cuda-samples
make -j3 SMS="75"
Use the number “75” because it represents the Turing architecture. Use the number that matches your GPU (find out here).

The samples are output to ./bin/x86_64/linux/release directory. Pick up some and run them to check if CUDA is successfully installed.

Install dependencies
Install other dependencies that COLMAP requires. These are the same as what is described in the official document.

sudo apt install \
    cmake \
    libboost-program-options-dev \
    libboost-filesystem-dev \
    libboost-graph-dev \
    libboost-regex-dev \
    libboost-system-dev \
    libboost-test-dev \
    libeigen3-dev \
    libsuitesparse-dev \
    libfreeimage-dev \
    libgoogle-glog-dev \
    libgflags-dev \
    libglew-dev \
    qtbase5-dev \
    libqt5opengl5-dev \
    libcgal-dev
Build Ceres Solver
Now build the last dependency, the Ceres Solver, which needs to be built from source.

# Install dependencies of the Ceres Solver
# that are not installed yet.
sudo apt install libatlas-base-dev libsuitesparse-dev
# Move up out of any previously cloned repository.
cd ..
# Then clone and build the Ceres Solver.
git clone https://ceres-solver.googlesource.com/ceres-solver
cd ceres-solver
git checkout 2.0.0   # Check out the latest release.
mkdir build-2.0.0
cd build-2.0.0
cmake .. -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF
make -j3
sudo make install
The COLMAP document uses make -j to build Ceres, which could use up all available CPU threads and consume over 20 GB of memory, which is undesired in an ordinary PC. Use make -j3 instead to reduce resource usage, though it takes longer to build.

Build COLMAP
Finally, build COLMAP.

cd ..
git clone https://github.com/colmap/colmap.git
cd colmap
git checkout dev
mkdir build
cd build
# Use gcc-9 and g++-9 to compile.
CC=/usr/bin/gcc-9 CXX=/usr/bin/g++-9 cmake ..
make -j3
sudo make install
If not specified, CMake uses gcc-10 and g++-10 to compile (on Ubuntu 20.10), which makes a COLMAP source file PoissonRecon.cpp throws a compiler error, stating that gcc/g++ version later than 9 is not supported. As a result, manually specify version 9 here when configuring the CMake project.

If you are not sure what compilers are installed on your platform, use the command (source): dpkg --list | grep compiler , which prints all installed packages with the word “compiler” contained.

After installation, run colmap gui to run the COLMAP GUI, or colmap -h to find out how to use COLMAP in the terminal.
