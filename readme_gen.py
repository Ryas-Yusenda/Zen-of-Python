import os
a = """<p align="center">
<a href="" rel="noopener">
<img width = 200px height = 200px src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt="Python"> </a>
</p>
<h3 align="center"> Python Project </h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Status](https://img.shields.io/github/commit-activity/m/Ryas-Yusenda/Zen-of-Python)](https://github.com/Ryas-Yusenda/Zen-of-Python/commits/main)
[![GitHub Issues](https://img.shields.io/github/repo-size/Ryas-Yusenda/Zen-of-Python)](https://github.com/Ryas-Yusenda/Zen-of-Python)
[![GitHub Issues](https://img.shields.io/github/languages/top/Ryas-Yusenda/Zen-of-Python?color=red)](https://github.com/Ryas-Yusenda/Zen-of-Python)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

</div>

---

<p align="center"> Just For Fun & Learning.
<br> 
</p>

## 📝 Table of Content

"""

b = """## 🏁 Getting Started <a name="getting_started"></a>

Run the project on your local machine for development and testing purposes.

### Prerequisites

You have to install some prerequisites.

```
pip install "example"
```

or

```
pip install -r requirements.txt
```

### Installing

Clone the repository.

```
git clone https://github.com/Ryas-Yusenda/Zen-of-Python.git
```

## 🎈 Usage <a name="usage"></a>

This project aims to learn and develop the python programming language. Keep learning. keep goinng. Keep practice :)

## ⛏️ Built With <a name="tech_stack"></a>

- [Anaconda](https://www.anaconda.com/)
- [Google Colab](https://colab.research.google.com/)
- [Jupyter](https://jupyter.org/)
- [Python](https://www.python.org/)

## ✍️ Authors <a name="authors"></a>

- [@Ryas-Yusenda](https://github.com/Ryas-Yusenda) - Idea & Initial work

See also the list of [contributors](https://github.com/Ryas-Yusenda/Zen-of-Python/contributors)
who participated in this project."""


# get all files' and folders' names in the current directory
filenames = os.listdir(".")

result = []
for filename in filenames:  # loop through all the files and folders
    # check whether the current object is a folder or not
    if os.path.isdir(os.path.join(os.path.abspath("."), filename)):
        if ".git" in filename or ".idea" in filename or ".ipynb_checkpoints" in filename or ".mrx-link-logs" in filename:
            continue
        result.append(filename)


result.sort()
print(result)

# To save Foldes names to a file.
f = open("README.md", 'w', encoding='utf-8')
f.write(a)
for index, filename in enumerate(result):
    f.write("- [%s](https://github.com/Ryas-Yusenda/Zen-of-Python/tree/main/%s)\n" %
            (filename, filename.replace(" ", "%20")))

f.write(b)
f.close()
