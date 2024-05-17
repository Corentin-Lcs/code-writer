<h1 align="center">Code Writer</h1>

The "Code Writer" GitHub project is a tool designed especially for video programming tutorials. It automatically generates code writing from a source file, allowing programming tutorial creators to simply record the video showing the code being written step by step.

<p align="center">
  <img src="https://github.com/Corentin-Lcs/code-writer/blob/main/Code.jpg" alt="Code.jpg"/>
</p>

## Usage

The user has the possibility to create dynamic tutorials without having to manually write every line of code and can use the tool for all existing programming languages. The `script.py` file is modular and offers several parameters :

```py
typing_speed = 0.05 # Typing speed (in characters per second)
line_pause = 0.001 # Pause time between each line (in seconds)
file_name = 'file.extension' # Name of file to write
```

> Don't forget to replace "file.extension" with the desired source file.

To use the program from the command prompt, run the following command :

```
python script.py
```

## Project's Structure

```
code-writer/
├─ README.md
├─ LICENSE
├─ Code.jpg
└─ src/
   ├─ script.py
   └─ file.extension
```

## Meta

Created by [@Corentin-Lcs](https://github.com/Corentin-Lcs). Feel free to contact me !

Distributed under the GNU GPLv3 license. See [LICENSE](https://github.com/Corentin-Lcs/code-writer/blob/main/LICENSE) for more information.
