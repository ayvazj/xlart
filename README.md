
[![Build Status](https://travis-ci.org/ayvaz/xlart.svg?branch=master)](https://travis-ci.org/ayvazj/xlart)

xlart
=====

Excel art generator

![Sample Screenshots][1]

Installation
------------

Using PIP

    $ pip install xlart

Using setup

    $ python setup.py install


Usage
-----


```bash
    xlart image.png destination.xlsx
```

You can control the downsampling with the --scale argument. 

```bash
    # output 1 cell for every 3 pixels of the image
    xlart image.png destination.xlsx --scale=3
```

Troubleshooting
---------------

If you have problems installing Pillow on macOS try this, then try
installing again.

```bash
    pip install --upgrade pip
    pip install Pillow
```

Links
=====
* ![PyPI][2]


[1]: https://raw.github.com/ayvazj/xlart/master/doc/demo.png
[2]: https://pypi.python.org/pypi/xlart/0.1.0/