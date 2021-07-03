#! /bin/python

import os
import shutil

DOTS=[
    "~/.config/bspwm",
    "~/.config/dunst",
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
    "~/.local/bin/set-theme",
    "~/.local/bin/work-rdc",
    "~/.local/bin/work-vpn",
    "~/.gtkrc-2.0",
    "~/.xinitrc",
    "~/.zshrc",
]

for dot in DOTS:
    source = dot.replace("~", "/home/rekyuu")
    destination_dir = "/".join(dot.split("/")[1:-1])
    destination = "/".join(dot.split("/")[1:])

    print(f"{source} -> {destination}")

    if len(dot.split("/")[1:-1]) > 0:
        os.makedirs(destination_dir, exist_ok=True)

    if os.path.isdir(source):
        shutil.copytree(source, destination, dirs_exist_ok=True)
    elif os.path.isfile(source):
        shutil.copyfile(source, destination, follow_symlinks=True)
