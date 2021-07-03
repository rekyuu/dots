#! /bin/sh

numlockx &
DISPLAY=":0" picom -b &

eval $(/usr/bin/gnome-keyring-daemon --start) &
export SSH_AUTH_SOCK &

exec bspwm