#!/usr/bin/env bash

xwallpaper --stretch $HOME/Pictures/arch.png &
kbdd &
pamixer -set-volume 0
picom &
nm-applet &
cbatticon &
blueman-applet &
#sleep 0.5
mpv /usr/share/mathjax2/extensions/a11y/invalid_keypress.mp3
volumeicon &
