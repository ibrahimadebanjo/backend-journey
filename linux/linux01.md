Date 28|05|26

 Bash vs exit vs echo $SHLVL
1. Bash
`bash` is basically a command that launches a new instance of bash inside your current shell
Reining bash multiple times nests new one on top

2. exit
`exit` is a built-in command used to close current shell later and returns you to the initial one that started it. 

3. echo $SHLVL
`echo $SHLVL` This is a command that is used to check the level of shell you're in.
![Screenshot_20260528-121125](bash_shell_level.jpg) 


LINUX DIRECTORY TREE NAVIGATION
Filesystem in Linux: it's a structure that organizes data on a volume so that the operating system can read and write files and directories example ext4

How to use Tree
1. Log in to Ubuntu
2. apt update && apt install sudo
3. `usermod -aG sudo username `
Nb: if you want to check username type: `whoami` on Ubuntu
4. Logout using exit and log in again from termux using `proot-distro login ubuntu`
5. `sudo apt update`
6. `sudo apt install tree`
7. `tree`

![Screenshot_20260528-095713](tree.jpg)

INODES AND INODE TABLE
Inode is what Linux use to keep track of files or folders separate from the filename.
Using command like `ls -i`, `ls -li`to see informatios on files.

Ls
List file directories
![Screenshot_20260528-121854](ls.jpg) 

Pwd
 Full path from root to current working directory. Only takes 2 flags
 -L : the default and it shows the symlink to the directory
 -P : shows the original path to the directory.

SYMLINKS AND HARDLINKS
1. SYMLINKS
This is a shortcut or pointer to another file or folder.
Nb: if you delete symlink the original file stays and if you delete the original file the symlink breaks.
To create a symlink use:

`ln -s path-to-the-file/folder symlinname`
Nb: can create the symlink in the root or anywhere it'll be pointing to the path specified.
Use em symlinname to delete symlink


![Screenshot_20260528-110902](cd.jpg) 

2. HARDLINK
This represent another name for the file i.e if file is deleted, hardlink will represent the file but with another name. 
To create a hardlink.
touch the file path you want to give hardlink or Crete a new file using touch.
`touch path(file1)`
`ln path(file1) hardlinkname named "file2"`

Nb: when writing flags there should be space between the command and the flag. 