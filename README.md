digital-signal-processing-exercises

The project is currently under heavy development while adding new material for
the winter term 2020/21.

# Exercises for a Master Course on Digital Signal Processing

These exercises accompany the lecture

https://github.com/spatialaudio/digital-signal-processing-lecture


## Getting Started

The Jupyter notebooks are accessible in various ways

- Online as [static web pages](https://nbviewer.jupyter.org/github/spatialaudio/digital-signal-processing-exercises/blob/outputs/index.ipynb) hosted with help of https://nbviewer.jupyter.org
- Online as [static web pages](https://github.com/spatialaudio/digital-signal-processing-exercises/blob/outputs/index.ipynb) directly in the github preview
- Online for [interactive usage](https://mybinder.org/v2/gh/spatialaudio/digital-signal-processing-exercises/outputs) hosted with help of https://mybinder.org
- Local for interactive usage on your computer by cloning / downloading the repository from
https://github.com/spatialaudio/digital-signal-processing-exercises

Note: We use the [output branch](https://github.com/spatialaudio/digital-signal-processing-exercises/tree/outputs) merely to have convenient way of rendered results and
plots for static web pages, whereas the master branch contains no outputs
for convenient diff debugging. Thus, output branch is derived from a current
appropriate master version and will be changed hard from time to time.

## Python / Jupyter Environment

The [Anaconda Python distribution](https://www.anaconda.com/products/individual)
is a very convenient out of the box solution to install the required software
to use Jupyter Notebook with Python.

It is very likely that the root environment already delivers all required packages.

If not, creating and activating a dedicated environment `my_dsp` might be useful:

- get at least python 3.7x, numpy, scipy, matplotlib, notebook, ipykernel, the
other packages are very useful tools

`conda create -n my_dsp python=3.7 pip numpy scipy matplotlib notebook jupyterlab pydocstyle pycodestyle autopep8 ipykernel nb_conda jupyter_nbextensions_configurator jupyter_contrib_nbextensions`

- activate this environment

`conda activate my_dsp`

- Jupyter notebook needs to know that we want to use the new environment

`python -m ipykernel install --user --name my_dsp --display-name "my_dsp"`

- get into the folder where the DSP exercises are located

`cd my_digital-signal-processing-exercises_folder`

- start a Jupyter notebook local server instance

`jupyter notebook`

- Change Kernel in the Jupyter Notebook GUI to my_dsp.

- Have fun with the playgrounds

## License

The notebooks are provided as [Open Educational Resources](https://en.wikipedia.org/wiki/Open_educational_resources). Feel free to use the notebooks for your own purposes. The text is licensed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), the code of the IPython examples under the [MIT license](https://opensource.org/licenses/MIT). Please attribute the work as follows: *Frank Schultz, Digital Signal Processing - A Tutorial Featuring Computational Examples* with the URL https://github.com/spatialaudio/digital-signal-processing-exercises
