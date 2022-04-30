#!/bin/bash

find ~/.config/qtile/Wallpapers/  -type f | shuf -n 1 | xargs xwallpaper --zoom
