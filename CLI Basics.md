## 1. GUI vs CLI
: **Graphical User Interface** is a window where the user can communicate with the computer by clicking given options in the menu. Thus, we can only manipulate what is given in the menu.

: **Command Line Interface** is a window where the user completely types string of commands to communicate with the computer. Unlike the GUI which is limited by the given menu buttons, CLI is more flexible and can automate commands iteratively.

: **Shell** is a type of CLI where it exposes the innermost layer of the OS to the user, such that it lets you do actions within the scope of the OS

## 2. BASH

: In Linux, bash is the most common Shell, and will be the one being used in this module.

: *Note: I will be mentioning the word CLI, Shell, and BASH, but this refers to the current BASH window that we are operating right now*

### 2.1. Shell Basic Syntax (p.s there is a General Syntax later)

1. **`$` prompt**
: This prompt indicates that the CLI is waiting for a command.

: Whenever we copy commands, *DO NOT include the $*

e.g.

```bash
$ echo Hello
Hello
```
`
: we see here that the $ is where we can place prompts (echo just prints the word "Hello")

: in the next line is where the output of the recent command is printed (notice that there is no $, suggesting that this line is an output, and it doesn't await for commands)

2. **Inputting Passwords**

: whenever we input passwords, we see to it that it does not get displayed in the CLI. This is a safety feature of BASH, we can just proceed typing our password and click `Enter` afterwards

### 2.2. Common BASH Commands

##### A. `clear` : basically clears the whole CLI

##### B.  `pwd`: prints the working directory (i.e. prints the current folder you are right now)

##### **Path Familiarization**
: when called, you may see something like `/home/jacob`

: the first `/` is the root directory (i.e. root folder containing everything), followed by the home directory and the jacob directory. The remaining `/` are simply separators of the subsequent directories.

##### C. `ls` : lists down the  files and directories within the current directory.

##### **ls Options**
: by default, `ls` lists objects in alphabetical order
: options changes how the output will be displayed
: several options can be done (even simultaneously)

- `ls --help` : lists down several options we can include to `ls`
- `ls -t` : sorts in data modified
- `ls -s` : sorts in size
- `ls -l` : lists down several properties
- `ls -F` : formats objects depending on its type (objects ending with `/` are directories, `*` are executables, etc.)
- `ls -h` : compresses large numbers (e.g. 3502 becomes 3.5k)
- `ls -r` : sorts in reverse

: *Note that we can include multiple options at the same time (e.g. we can do `ls -t -r` to sort in time in reverse*

##### **Options Conventions**
: use the shorthand keywords in routine typing of commands in CLI, while long keywords for scripts and documentations (to make it more readable)

e.g. use `ls -s` in operating commands, and `ls --size` in making scripts/documentations`

##### 4. `cd` :  Changes directory (i.e. proceeds to another directory)

**cd Arguments (these arguments can be used to other commands)

: arguments is the object the command will operate to

: `cd .` : proceeds to the current directory (when used in `cd`, nothing much happens)

: `cd <subdirectory>` : to proceed to the subdirectory
	( e.g. suppose there is Images directory inside the current directory. Simply type `cd Images/`)
	: one can chain subdirectories 

: `cd ..` : Goes back to the parent directory

: `cd ~` : Proceeds to the home default directory

: `cd -` : Goes back to the previous directory I was in

: `cd /` : Basically proceeds to the root directory

### 2.3. BASH General Syntax

: a line of shell command contains the **prompt, command, option, and argument**, with each part separated by spaces

1. **Prompt** : basically the `$` we talked about
2. **Command** : a certain action to implement
3. **Option/s** : the additional keyword/s to change the behavior of the command
4. **Argument/s** : the object/s where the command will operate on

e.g. Explicit Argument
```bash
$ ls -F /
```

- prompt : `$`
- command : `ls`
- option : `-F`
- argument : `/`

: this means to list the objects (`ls`), with object type displays (`-F`), within the directory (`/`, or the root directory)

e.g. Implicit Argument
```bash
$ ls -F
```

- prompt : `$`
- command : `ls`
- option : `-F`
- argument : None (i.e. it does the command to the current directory)

: this means to list the objects (`ls`), with object type displays (`-F`), within the current directory

## 2.4. More Shell Commands

: we will be focusing on file manipulation (e.g. making, writing, removing, moving files and directories)
##### A. `mkdir <new_dir_name>` : makes a new directory inside the current directory

> : For **B, C, and D**, these are ways to create a file (and even edit existing files)

##### B. `nano <file_name.file_exten>` : makes a new file and opens the nano text editor

: nano is one of the simplest text editor, natively opened in the BASH. Thus, use this if you will only write simple texts.

: you can write something there and below are commands that you can implement (`^O` means ctrl+0 )

: `^S` to save
: `^X` to exit from the text editor

: commanding `nano` to exiting files simply edits it

##### C. `code <file_name.file_exten>` : makes new file and opens  it in vs code

: basically used for common file coding via VS Code

: commanding `code` to exiting files simply edits it

##### D. `touch <file_name.file_exten>` : simply makes a blank new file

: only used for the purpose of making a new file, or updating the metadata (e.g. date opened) for existing files

##### E. `rm <file_name.file_exten>` : removes/deletes the file

##### F. `rm -r -i <file_name.file_exten>` : removes/deletes the folder recursively (-r)
: the `-i` option makes it interactive to avoid accidentally deleting files

> **G and H** are different usages of `mv` command (renames or moves files)

##### G. `mv <file_name.exte> <new_file_name.exte>` : renames a file to a new file name

: simply type the file if it is in the current directory, or you can type the whole path

##### H. `mv <file_name.exte> <directory>` : moves the file to the mentioned directory

: simply type the file if it is in the current directory, or you can type the whole path

: aside from moving a file  to the mentioned directory, you can move a directory to the mentioned directory

> **I, J and K** are different usages of `cp` command (copies files/contents)

##### I. `cp <file_name.exte> <directory>` : copies the file to the mentioned directory

##### J. `cp <file_name.exte> <other_or_new_file.exte>`: copies the content to the 2nd mentioned file

`cp <file1> <file2> <directory>`
: having 3 parameters copies the first two files to the mentioned directory

##### K. `cp -r <directory1> <directory2>` : recursively (-r) copies all of the contents of directory1 to directory2

## 2.5. Wildcard Symbols
: **`*` and `?`** are used to substitute a letter/s to search for multiple common filenames

: suppose we have
```bash
$ ls
methane.pdb
ethane.pdb
propane.pdb
octane.pdb
cubane.pdb
```
##### A. `*` Symbol : represents zero or more other *unmentioned* characters

e.g. 
```bash
$ ls *ane.pdb
cubane.pdb  ethane.pdb  methane.pdb  octane.pdb  pentane.pdb  propane.pdb
```

```bash
$ ls *.pdb
cubane.pdb  ethane.pdb  methane.pdb  octane.pdb  pentane.pdb  propane.pdb
```

```bash
$ ls p*
pentane.pdb  propane.pdb
```

##### B. `?` Symbol : represents EXACTLY ONE unmentioned character

e.g.
```bash
$ ls ?ethane
methane.pdb
```

```bash
$ ls ???ane.pdb
cubane.pdb  ethane.pdb  octane.pdb
```