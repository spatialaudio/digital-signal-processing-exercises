# digital-signal-processing-exercises

**Exercises for a Master's Course on Digital Signal Processing**

These exercises accompany the lecture [Digital Signal Processing](https://github.com/spatialaudio/digital-signal-processing-lecture)

The lecture and the tutorial are designed for International Standard Classification of Education (ISCED) level 7 (Master, 1 SWS).
The project is currently maintained for the winter term 2022/23.

Jupyter notebooks can be accessed via the services

- Online as [static web pages](https://nbviewer.jupyter.org/github/spatialaudio/digital-signal-processing-exercises/blob/main/index.ipynb) hosted with help of https://nbviewer.jupyter.org
- Online as [static web pages](https://github.com/spatialaudio/digital-signal-processing-exercises/blob/main/index.ipynb) directly in the github preview
- Online for [interactive usage](https://mybinder.org/v2/gh/spatialaudio/digital-signal-processing-exercises/dev) hosted with help of https://mybinder.org
- Local for interactive usage on the user's computer by cloning / downloading the repository from
https://github.com/spatialaudio/digital-signal-processing-exercises


## Versions / Tags
- [v0.1](https://github.com/spatialaudio/digital-signal-processing-exercises/releases/tag/v0.1) for winter term 2021/22
- TBD for winter term 2022/23 

## Branch Conventions

- we use the `dev` branch as the developing branch, i.e. all notebook outputs are cleared for convenient diff handling
- we use the `main` branch as presentation branch, i.e. notebook outputs (such as plots, results) are included for students' convenience
- note that we **hard reset** `main` branch from time to time in order to represent an actual desired state of the material
- so please do not rely on `main` related commits, but rather act on the `dev` commits, where git history is not changed

## Anaconda Environment for Local Usage

The [Anaconda distribution](https://www.anaconda.com/distribution/) is a convenient solution to install a required environment, i.e. to have access to the Jupyter Notebook renderer with a Python interpreter on a personal computer. It is very likely that a very recent installation of Anaconda already delivers all required packages just using the `base` environment. It is however good practice to create a dedicated environment for each project. So, for this tutorial we might use a `mydsp` (or whatever name works for us) environment.

- get into the folder where the exercises are located, e.g. `cd my_dsp_folder`
- in the subfolder `.binder` the `environment.yml` can be used to create a dedicated conda `mydsp` environment as
    - `conda env create -f environment.yml --force`
    - we can remove this environment with `conda env remove --name mydsp`
- this should also have installed audio related libraries using pip
    - `pip install soundfile==0.10.3.post1`
    - we might check this with `pip list`
- activate this environment with `conda activate mydsp`
- Jupyter notebook renderer needs to know our dedicated environment:
`python -m ipykernel install --user --name mydsp --display-name "mydsp"`
- we might want to archive the actually installed package versions by
    - `python -m pip list > detailed_packages_list_pip.txt` and
    - `conda env export --no-builds > detailed_packages_list_conda.txt`
- start either a Jupyter notebook or Jupyter lab working environment via a local server instance by either `jupyter notebook` or `jupyter lab`
- start the landing page `index.ipynb` of the tutorial
- make sure that the notebooks we want to work with are using our dedicated kernel `mydsp`


## Authorship

- University of Rostock:
    - [Frank Schultz](https://orcid.org/0000-0002-3010-0294)
    - [Jacob Thönes](https://github.com/JacobTh98)
    - [Robert Hauser](https://github.com/robhau)
    - [Sascha Spors](https://orcid.org/0000-0001-7225-9992)

## Referencing

Please cite this open educational resource (OER) project as
*Frank Schultz, Digital Signal Processing - A Tutorial Featuring Computational Examples* ideally with relevant ``file(s), github URL, commit number and/or version tag, year``.

## License

- Creative Commons Attribution 4.0 International License (CC BY 4.0) for text/graphics
- MIT License for software


## License

The notebooks are provided as [Open Educational Resources](https://en.wikipedia.org/wiki/Open_educational_resources). Feel free to use the notebooks for your own purposes. The text is licensed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), the code of the IPython examples under the [MIT license](https://opensource.org/licenses/MIT). Please attribute the work as follows: *Frank Schultz, Digital Signal Processing - A Tutorial Featuring Computational Examples* with the URL https://github.com/spatialaudio/digital-signal-processing-exercises
