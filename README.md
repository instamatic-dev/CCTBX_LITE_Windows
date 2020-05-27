![LICENSE](https://img.shields.io/github/license/Taimin/CCTBX_LITE_Windows)

# CCTBX-LITE-Windows

`CCTBX` is a toolbox for crystallography computation. The Computational Crystallography Toolbox (CCTBX) is being developed as the open source component of the `PHENIX` system. The `CCTBX` also provides some of the key component of the `Olex 2` software. `Olex 2` is dedicated to the workflow of small molecule crystallographic studies. It features a powerful and flexible refinement engine, `olex2.refine`, which is developed as part of the cctbx, in the smtbx top-module.

For researchers and students, `CCTBX` can be a quite handy tool for crystallography research. However, the [Downloaded Package](http://cci.lbl.gov/cctbx_build/) is quite large after installation with all the features included, which is quite intimidating for me at least. That is the main reason for me to make this mini version of cctbx. In addition, it is poorly documented. Only limited features and very basic features are documented in [HERE](https://cci.lbl.gov/cctbx_docs/index.html). When faced with such a huge software package, one will easily get lost and confused.

Another issue for cctbx is if you want to incooperate cctbx into your own project. It will be a headache to include all the `1.5G` files. If your programming project is quite small (<1MB), you will start to wonder why you must include such a large project into your tiny project with all the unnecessary files and features.

This minimized cctbx is just around `110MB`. It does not include the base packages. It removed features such as xfel, GUI system, phenix, hdf5 and cbf. Kept all the compile boost python modules and cctbx_project. All the test files, GUI related files and example files were removed. It's built from the [Bootstrap Script](https://raw.githubusercontent.com/cctbx/cctbx_project/master/libtbx/auto_build/bootstrap.py) using this cmd line:

    python bootstrap.py --builder=cctbxlite --with-python=C:\Users\yang\AppData\Local\Programs\Python\Python37\python.exe --nproc=2 hot update build

Another feature for this package is it's built on `python 3.7` while the official packages are still using python 2. Considering python 2 will no longer be updated from 2020. Hope the official CCTBX package transition from 2 to 3 will come soon.

In sum, the available toolboxes in this package is `boost.python`, `cctbx main package`, `libtbx`, `iotbx`, `mmtbx`, `scitbx` and `smtbx`. It definitely can be even smaller. If you want to try, that can be very interesting to see how far can it go. In my opionion, `boost.python`, `cctbx main package`, `iotbx`, `libtbx` and `scitbx` must be kept. Otherwise, no code will work.

# Installation and Requirements

To install this package, download to the package to the destination directory and install python 3.7. Support for other python 3 versions will be added. Then run the `install.bat` file, then set:

    LIBTBX_BUILD = YOUR DESTINATION DIRECTORY/build
	PYTHONPATH = %LIBTBX_BUILD%\..\modules\cctbx_project;%LIBTBX_BUILD%\..\modules;%LIBTBX_BUILD%\lib