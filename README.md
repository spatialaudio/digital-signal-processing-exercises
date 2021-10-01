digital-signal-processing-exercises

The project is currently maintained for the winter term 2021/22.

# Exercises for a Master's Course on Digital Signal Processing

These exercises accompany the lecture

https://github.com/spatialaudio/digital-signal-processing-lecture


## Getting Started

The Jupyter notebooks are accessible in various ways

- Online as [static web pages](https://nbviewer.jupyter.org/github/spatialaudio/digital-signal-processing-exercises/blob/outputs/index.ipynb) hosted with help of https://nbviewer.jupyter.org
- Online as [static web pages](https://github.com/spatialaudio/digital-signal-processing-exercises/blob/outputs/index.ipynb) directly in the github preview
- Online for [interactive usage](https://mybinder.org/v2/gh/spatialaudio/digital-signal-processing-exercises/master) hosted with help of https://mybinder.org
- Local for interactive usage on the user's computer by cloning / downloading the repository from
https://github.com/spatialaudio/digital-signal-processing-exercises

Note: We use the [output branch](https://github.com/spatialaudio/digital-signal-processing-exercises/tree/outputs) merely for convenience showing rendered results and plots on static web pages, whereas the [master branch](https://github.com/spatialaudio/digital-signal-processing-exercises) contains no outputs for convenient diff debugging. Thus, the **output branch** is derived from a current appropriate master version and will be **changed hard** from time to time.

## Python / Jupyter Environment

The [Anaconda Python distribution](https://www.anaconda.com/products/individual)
is a very convenient out of the box solution to install the required software on
all major operating systems.

It is very likely that Anaconda's root environment already delivers all
required packages.
If not, creating and activating a dedicated environment `mydsp` might be useful:

- get at least `python` version 3.8x, `numpy`, `scipy`, `matplotlib`, `notebook`, `ipykernel`

- the other packages in the command below (that is to create the environment `mydsp` from terminal) are very useful tools

- `conda create -n mydsp python=3.8 pip numpy sympy scipy matplotlib notebook ipykernel jupyterlab pydocstyle pycodestyle autopep8 flake8 nb_conda jupyter_nbextensions_configurator jupyter_contrib_nbextensions`

- activate this environment by `conda activate mydsp`

- Jupyter notebooks need to know that we want to use this new environment

`python -m ipykernel install --user --name mydsp --display-name "mydsp"`

- get into the folder where the DSP exercises are located `cd my_digital-signal-processing-exercises_folder`

- start a Jupyter notebook local server instance `jupyter notebook` or `jupyter lab`

- change kernel in the Jupyter Notebook GUI to `mydsp`

- have fun with the playgrounds and start programming stuff by yourself

If the above steps lead to problems, the currently used exact environment to maintain the notebooks was created under `conda 4.10.3` and `conda-build 3.21.4` by the commands
- `conda create -n mydsp python=3.8.12 pip=21.2.4 numpy=1.21.2 sympy=1.8 scipy=1.7.1 matplotlib=3.4.3 notebook=6.4.4 ipykernel=6.4.1 jupyterlab=3.1.14 pydocstyle=6.1.1 pycodestyle=2.7.0 autopep8=1.5.7 flake8=3.9.2 nb_conda=2.2.1 jupyter_nbextensions_configurator=0.4.1 jupyter_contrib_nbextensions=0.5.1`
- `pip install soundfile`

## License

The notebooks are provided as [Open Educational Resources](https://en.wikipedia.org/wiki/Open_educational_resources). Feel free to use the notebooks for your own purposes. The text is licensed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), the code of the IPython examples under the [MIT license](https://opensource.org/licenses/MIT). Please attribute the work as follows: *Frank Schultz, Digital Signal Processing - A Tutorial Featuring Computational Examples* with the URL https://github.com/spatialaudio/digital-signal-processing-exercises
