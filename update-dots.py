#! /bin/python

import filecmp
import os
import shutil
import sys

DOTS=[
    "~/.config/bspwm",
    "~/.config/dunst",
    "~/.config/fish",
    "~/.config/flavours",
    "~/.config/gtk-3.0",
    "~/.config/kitty",
    "~/.config/mpd",
    "~/.config/ncmpcpp",
    "~/.config/picom",
    "~/.config/polybar",
    "~/.config/rofi",
    "~/.config/sxhkd",
    "~/.config/systemd/user/work-vpn.service",
    "~/.local/bin/bootstrap",
    "~/.local/bin/bspc-left-monitor",
    "~/.local/bin/bspc-right-monitor",
    "~/.local/bin/pacman-remove-orphans",
    "~/.local/bin/screenshot-scrot",
    "~/.local/bin/set-flavour",
    "~/.local/bin/set-theme",
    "~/.local/bin/work",
    "~/.local/bin/work-rdc",
    "~/.local/bin/work-vpn",
    "~/.local/share/flavours/base16/templates/vscode-custom",
    "~/.gtkrc-2.0",
    "~/.Xresources",
    "~/.xinitrc",
]


def replicate(source, dest):
    if os.path.isdir(source):
        replicate_dir(source, dest)
    elif os.path.isfile(source):
        replicate_file(source, dest)


def replicate_dir(source, dest):
    comp = filecmp.dircmp(source, dest)

    if not os.path.isdir(dest):
        shutil.copytree(source, dest)
        print(f"{source} -> {dest}")
        return
    
    if len(comp.diff_files) > 0:
        for f in comp.diff_files:
            replicate_file(f"{source}/{f}", f"{dest}/{f}")

    if len(comp.subdirs) > 0:
        for subdir in comp.subdirs:
            replicate_dir(f"{source}/{subdir}", f"{dest}/{subdir}")


def replicate_file(source, dest):
    both_are_the_same = os.path.isfile(dest) and filecmp.cmp(source, dest)
    source_is_newer = os.path.getctime(source) > os.path.getctime(dest) if os.path.isfile(dest) else True

    if not both_are_the_same and source_is_newer:
        destination_dir = "/".join(dest.split("/")[:-1])
        if destination_dir != "" and len(destination_dir.split("/")) > 0:
            os.makedirs(destination_dir, exist_ok=True)
                
        shutil.copyfile(source, dest, follow_symlinks=True)

        print(f"{source} -> {dest}")


for dot in DOTS:
    home = dot.replace("~", "/home/rekyuu")
    repo = "/".join(dot.split("/")[1:])

    if len(sys.argv) >= 2:
        if sys.argv[1] == "export":
            replicate(repo, home)
    else:
        replicate(home, repo)
