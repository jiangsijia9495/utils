This gist contains instructions about cuda v11.1 and cudnn 8.0.4 installation in Ubuntu 18.04 for Tensorflow 2.4.1

- If you have previous installation remove it first.
```
!/bin/bash
sudo apt-get purge *nvidia*
sudo apt remove --autoremove nvidia-*
sudo rm /etc/apt/sources.list.d/cuda*
sudo apt remove --autoremove nvidia-cuda-toolkit
sudo apt-get autoremove && sudo apt-get autoclean
sudo rm -rf /usr/local/cuda*
```

- Verify your gpu cuda
```
lspci | grep -i nvidia
```
- gcc compiler is required for development using the cuda toolkit. to verify the version of gcc install enter
```
gcc --version
```
- System update
```
sudo apt-get update
sudo apt-get upgrade
```

- Install other import packages
```
sudo apt-get install g++ freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev
```

- First get the PPA repository driver
```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64 /" | sudo tee /etc/apt/sources.list.d/cuda.list
sudo apt-get update
```
- Installing CUDA-11.1
```
sudo apt-get -o Dpkg::Options::="--force-overwrite" install cuda-11-1 cuda-drivers
```

- Setup your paths
```
echo 'export PATH=/usr/local/cuda-11.1/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.1/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
sudo ldconfig
```
- Install cuDNN v8.0.4
```
CUDNN_TAR_FILE="cudnn-11.1-linux-x64-v8.0.4.30.tgz"
wget https://developer.nvidia.com/compute/machine-learning/cudnn/secure/8.0.4/11.1_20200923/cudnn-11.1-linux-x64-v8.0.4.30.tgz
tar -xzvf ${CUDNN_TAR_FILE}
```

- Copy the following files into the cuda toolkit directory.
```
sudo cp -P cuda/include/cudnn*.h /usr/local/cuda-11.1/include
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda-11.1/lib64/
sudo chmod a+r /usr/local/cuda-11.1/lib64/libcudnn*
```
- Finally, to verify the installation, check (maybe the Cuda version in nvidia-smi and nvcc is different)
```
sudo apt install nvidia-cuda-toolkit
nvidia-smi
nvcc -V
```
- Install Tensorflow 2.4.1 (tf-nightly-gpu if needed) because it is stable and compatible with CUDA 11.1 Toolkit and cuDNN 8.0.4
```
pip3 install --user tf-nightly-gpu
pip3 install --user tensorflow==2.4.1
conda install -c anaconda cudnn
conda install -c anaconda cudatoolkit
```
