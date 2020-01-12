Some of my codes use cython for faster computation. As a result they are C compiled and tested to run perfectly on my system. They may not run properly and the binaries need to be compiled on the host machine. I have tried to include both a Linux and a Windows version of the binaries. But again they aren't guranteed to work. 
Please do the following for compiling the binaries in the host machine that has cython package with it:
There is file named setup.py
The .pyx files need to be compiled. 
setup.py file needs to be edited to include the filename of the relevant .pyx file that needs to be compiled
Then in the terminal please run 
python setup.py build_ext --inplace
