#!/bin/bash

grep "[[:digit:]]" /sys/class/power_supply/BAT0/capacity | xargs echo -n
