![build](../../workflows/build/badge.svg) ![release](../../workflows/release/badge.svg)

# cs102-F2020-slides

This repository contains the slides for Computer Science 102 Fall 2020. To
learn more about the course for which these slides were created, please visit
the [Computer Science 102 Fall 2020 GitHub
Organization](https://github.com/Allegheny-Computer-Science-102-F2020).

## Accessing the Slides

Since this repository primarily contains LaTeX source code, the GitHub Actions
configuration for it will compile the source code and automatically release a
PDF of the source code whenever the last commit is associated with a [Git
Tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging). As such, this will
cause PDF files to become available in the listing of the
[Releases](https://github.com/Allegheny-Computer-Science-102-F2020/cs102-F2020-slides/releases)
for this repository. All release numbers in this repository adhere to the
[Semantic Versioning](http://semver.org/) standard.

## Running Python Programs from the Slides

The slides contain the source code of segments of Python programs that a student
can run in order to learn more about the connection between discrete structures
and Python programming. Here is an outline of the commands that you can type if
you want to change into the directory that contains these Python programs and
then run them on your own laptop. Importantly, these commands assume that you
have already cloned this repository to your laptop.

- Change into the directory that contains the Python source code: `cd src`
- Run the program that computes the absolute value: `python abs-compute.py`
- Run the program that computes the factorial sequence: `python factorial-function.py`
- Run the program that computes the mean of a list of numbers: `python mean-compute.py`
- Run the program that uses a Newton's method function to compute a square root: `python newtons-method-function.py`
- Run the program that uses a Newton's method segment to compute a square root: `python newtons-method.py`
- Run the program that displays a range of integer numbers: `python range-display.py`
- Run the program that uses higher-order functions to compute a number's square: `python square-function.py`


## Problems or Praise

If you have any problems with compiling the slides, then please create an
issue in this repository using the "Issues" link at the top of this site. Please
note that this slides has been developed and tested on an Arch Linux
workstation running TexLive 2020. It is also worth noting that you can also
compile the slides using LaTeX development tools such as `latexmk`. If you are
unable to compile the slides with your development tools and your execution
environment, then please open a new issue and I will attempt to resolve your
concerns.
