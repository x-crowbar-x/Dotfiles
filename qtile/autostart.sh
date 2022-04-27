#!/usr/bin/env bash

#kbdd &
pamixer --set-volume 0
picom --experimental-backend &
nm-applet &
# cbatticon &
blueman-applet &
mpv /usr/share/mathjax2/extensions/a11y/invalid_keypress.mp3
volumeicon &
