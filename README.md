# execfs

The superior FUSE filesystem for exec on file open.

In the filesystem created by **execfs** for every path the filename is extracted, it's passed to a shell and the output is returned as if it was the content of the file in that path.

```
~$ execfs &
~$ cat /tmp/execfs/"pacman -Q | grep git"
git 2.28.0-1
libgit2 1:1.0.1-1
libgit2-glib 0.99.0.1-2
```

Here we have the `.vimrc` that is generated bash simple command, setting the colors base on the time of day, which could be wrapped into a script for better readabilty. We can achieve this using a symlink from `~/.vimrc` to `~/tmp/execfs/...`. 

```
~$ ln -s '/tmp/execfs/[ $(date +%H) -gt 20 ] && echo set bg=dark || echo set bg=light' .vimrc
~$ cat .vimrc
set bg=dark
```

When the sub directory `cached` is used the shell command is executed once and its stored.

```
~$ gedit '/tmp/execfs/cached/git diff'
```

The cached command are also visible in the filesystem under the `cached` directory

```
~$ gedit "/tmp/execfs/cached/git diff # $(date)" &
~$ gedit "/tmp/execfs/cached/git diff # $(date)" &
~$ gedit "/tmp/execfs/cached/git diff # $(date)" &
~$ tree /tmp/execfs
/tmp/execfs
└── cached
    ├── git diff # Mon Aug 24 02:31:38 AM EEST 2020
    ├── git diff # Mon Aug 24 02:32:51 AM EEST 2020
    └── git diff # Mon Aug 24 02:33:58 AM EEST 2020

~$ rm /tmp/execfs/cached/*
```

## Usage

Running **execfs** will create a pseudo filesystem under the `/tmp/execfs`. Every access of any kind to files uder the directory will cause execfs to parse the filename as a shell command, run it and provide the output.

If a command fails to execute then the filesystem behaves as if the pseudo file does not exist.

The pseudo file under the `/tmp/execfs/cached` behave in the same way with the diference that they will only execute the command first time and the output will be stored for future uses.

To use parameters that contain paths, in order to not be interpreted as part of the main path, any '\\' will be replaced with a `/`.

```
~$ ln -s '/tmp/execfs/grep alias ~\.bashrc' alias_list
```

### Options

- `mountpoit`: The first argument is the empty directory where the filesystem will be mounted, if missing the default value of `/tmp/execfs` will be used.
- `-b`, `--background`: Start in the background.
- `-u`, `--unsafe`: Allow possible indirect command executions (see Unsafe option).
- `-c CWD`, `--cwd CWD`, `--home`: Set the working directory of the shell that will execute the commands.
- `-v`, `--verbose`, `-q`, `--quiet`: Control the level of logging.

#### Unsafe option

Long story short, with `--unsafe`, shell tab-completion can cause some unwanted executions of commands.

TODO expand

## Install

```
git clone https://github.com/MaanooAk/execfs
sudo python setup.py install
```

Arch Linux: [AUR package](https://aur.archlinux.org/packages/execfs/).
