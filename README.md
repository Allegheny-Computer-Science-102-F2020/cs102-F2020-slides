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
- Run the program that performs string multiple types of concatenation: `python string-concatenation.py`
- Run the program that performs sums and products of lists: `python number-sums-products.py`
- Run the program that demonstrates the map function: `python map-function.py`
- Run the program that demonstrates the filter function: `python filter-function.py`
- Run the program that demonstrates the reduce function: `python reduce-function.py`

Please note that these are what I would call "Python program segments" in that
they do not leverage a framework, like Poetry, for building Python applications.
While these programs will execute and produce output in your terminal window,
they do not provide either a command-line or a web-based interface. Unless
stated otherwise, these programs also do not assume that you have any additional
Python packages installed on your laptop. Finally, these programs contain
debugging output not listed on the slides, thereby better ensuring that you can
understand how the program accepts input and produces output. Here is an example
from running the command `python mean-compute.py` program:

```
Called compute_mean with numbers = [5, 10, 5, 10, 5]
Sum of numbers = 35
Length of numbers = 5
Calculated mean = 7.0
7.0
Called compute_mean with numbers = [5, 1, 7, 99, 4]
Sum of numbers = 116
Length of numbers = 5
Calculated mean = 23.2
23.2
5.0
```

The version of the Python function that contains the debugging output statements
that produced this output is as follows:

```
def compute_mean(numbers):
    print(f"Called compute_mean with numbers = {numbers}")
    s = sum(numbers)
    print(f"Sum of numbers = {s}")
    N = len(numbers)
    print(f"Length of numbers = {N}")
    mean = s / N
    print(f"Calculated mean = {mean}")
    return mean
```

## Problems or Praise

If you have any problems with compiling the slides, then please create an
issue in this repository using the "Issues" link at the top of this site. Please
note that this slides has been developed and tested on an Arch Linux
workstation running TexLive 2020. It is also worth noting that you can also
compile the slides using LaTeX development tools such as `latexmk`. If you are
unable to compile the slides with your development tools and your execution
environment, then please open a new issue and I will attempt to resolve your
concerns.
