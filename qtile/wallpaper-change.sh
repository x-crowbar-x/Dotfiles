#!/bin/bash

set_pic1=$HOME"/.config/qtile/Wallpapers/jinx-lol-artwork-4k-5s.jpg"
set_pic2=$HOME"/.config/qtile/Wallpapers/LLS2022_3.6_Patchnotes_Skin-Jinx1-Pulsefire_PCruz_V001.jpg"
set_pic3=$HOME"/.config/qtile/Wallpapers/LS2022_3.6_Patchnotes_Skin-Jinx2_Pulsefire_PCruz_V001.jpg"

if [[ $(date "+%H") -ge 18 ]]; then
	xwallpaper --zoom $set_pic3;
elif [[ $(date "+%H") -ge 13 ]] && [[ $(date "+%H") -le 17 ]]; then
	xwallpaper --zoom $set_pic1;
elif [[ $(date "+%H") -ge 0 ]] && [[ $(date "+%H") -le 12 ]]; then
	xwallpaper --zoom $set_pic2;
fi
