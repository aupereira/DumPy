# DumPy
DumPy is a basic math library written in pure Python. It's not fast, it's not well rounded, and it's certainly not good for production use — if you want that, please use something like NumPy or SciPy instead. Now, if DumPy isn't good for any of those things, then what *is* it good for? Mostly, just education — that is to say my education in that I learned how to write Python libraries at a basic level — and because it's quite basic it might help you understand how some common algorithms work.


### Installation
Installing DumPy can be done either by (1) downloading a bundled release from the releases section or (2) building it yourself.

##### 1. Installing a pre-packaged release
1. Go to the [Releases](https://github.com/aupereira/DumPy/releases) page.
2. Download the latest release.
3. Run the following command: `pip install <Path to File>`

##### 2. Building DumPy yourself
Make sure to have the build module installed. If you don't have it, you can get it with `pip install build`
1. Clone the DumPy repo: `git clone "https://github.com/aupereira/DumPy.git"`
2. From the root directory run: `python -m build`
3. Use pip to install the generated build in the /dist directory with: `pip install <Path to File>`


### Building Documentation
DumPy uses Sphinx with the Read the Docs theme for documentation. To build the documentation, navigate to the docs folder in your terminal and run the following commands:
1. Install prerequisites: `pip install -r requirements.txt`
2. Run the relevant MAKE command. If you don't have make because you're on Windows, open an Admin Command Prompt and run `winget install GnuWin32.Make`. The project is configured for the following doc formats:
    * **HTML** - Run `MAKE html` to generate a Read the Docs style website. It will be located in ./build/html.
    * **PDF** - Requires latexmk. Run `MAKE latex` to generate a LaTeX version of the docs, then navigate to ./build/latex and run `MAKE`.


### Basic Usage
DumPy is very simple to use. Currently, everything you need is available just by importing it. The typical syntax is:
```
import dumpy as dp
```
Then, you're all set! You're ready to call DumPy functions!
```
mat = dp.identity(5)
dp.printmat(mat)
```
