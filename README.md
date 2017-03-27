# Python Basics

This is a presentation describing the basics needed to become productive with Python.

## Generating the presentation html
The presentation is written in markdown and can be compiled using [landslide](https://github.com/adamzap/landslide).

* Install landslide

`
pip install landslide
`

* Run landslide to generate the presentation html

`
landslide landslide.cfg --copy-theme
`

This should create the presentation in a python\_basics/ folder

## Generating the python files for the presentation examples

`
python3 code_blocks.py python_basics.markdown
`
