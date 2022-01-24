# First steps with tensorflow
## How to start

### Set up Python
- Install Python 3.9 (https://www.python.org/downloads/windows/)
- Do not forget to set PATH variable during the installation
(For now, tensorflow does not support python 3.10)

### Install VS Code 
- Install VS Code (https://code.visualstudio.com/docs/setup/windows)
- Install VS Code Extension for Python (https://marketplace.visualstudio.com/items?itemName=ms-python.python oder _Ctrl + Shift + X_ and search for "Python")
- Create Virtual Environment `python -m venv venv` (If the venv is not active by default, run it by executing './venv/Scripts/activate')
- Start it with _Ctrl + Shift + P_, then _Enter_ to create a new Python terminal

### Install tensorflow
- Upgrade pip if necessary: `pip install --upgrade pip`
- `pip install tensorflow`

(https://www.tensorflow.org/install?hl=en)

## Install necessary packages
- `pip install notebook matplotlib pandas`

(_pandas_ and _matplotlib_ are only necessary vor visualization, _notebook_ is for jupyter notebook usage)

### Start jupyter notebook
- `jupyter notebook`

## Resources
This tensorflow tutorial is mainly based on https://www.tensorflow.org/tutorials/keras/classification

### Tutorials
- [Tensorflow Tutorials](https://www.tensorflow.org/tutorials/)

### Theoretical Insights
- [Neural Networks by 3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)

## Known Issues
**P**: You get an error executing pip in the venv
**S**: Try rebooting your computer

**P**: The python command cannot be found.
**S**: Maybe your forgot to set the path environment variable for the python executable. Use `where python` to locate your python executable and add it to the `Path` system variable. Then reboot your computer.