
Termux + Ubuntu Setup

Goal
Run a full Ubuntu environment inside Termux, with access to my Termux files.

The Problem
`proot-distro` runs Ubuntu in a fake root `/root`. By default it doesn’t start in my Termux home, so my files looked “missing”.

How It Works
- Termux home path: `/data/data/com.termux/files/home`  
- `proot-distro` already bind-mounts `/data/data/com.termux` into Ubuntu, so the files are at that long path inside Ubuntu.
- To make it easier, I bind my Termux home to a short path inside Ubuntu: `/root/termux`

Command to Login
```bash
proot-distro login ubuntu -b /data/data/com.termux/files/home:/root/termux
- `-b` = bind mount. Syntax: `-b [host path]:[guest path]`
- This makes my Termux files appear at `/root/termux` inside Ubuntu.

Permanent Shortcut
Added an alias to `~/.bashrc` so I don’t retype the bind every time:
echo "alias ub='proot-distro login ubuntu -b /data/data/com.termux/files/home:/root/termux'" >> ~/.bashrc
source ~/.bashrc
Now I just type `ub` in Termux to launch Ubuntu with my files ready.

Workflow Now
1. Open Termux
2. Type `ub` → drops into Ubuntu
3. `cd termux` → inside `/root/termux` which is my real Termux home
4. Use Ubuntu tools: `apt`, `python`, `git`, etc.

Key Concepts
- *proot-distro*: Runs Linux distros inside Termux without root
- *Bind mount `-b`*: Shares a folder from Termux into Ubuntu at a new path
- *Alias*: Saves a long command under a short name in `~/.bashrc`

That gives you the problem, the fix, and the why, all in one place. You can tag it `#termux #ubuntu #android` for easy search later.```
```

![Screenshot_20260529-113224](..images/setup.jpg)
