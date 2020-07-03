#!/bin/bash

# background iamge
feh --bg-fill $HOME/.config/i3/wp.png --bg-fill ~/.config/i3/wp.png

# turns of caps lock
setxkbmap -option ctrl:nocaps

# adjust tablet to main primar screen
xinput set-prop "HUION Huion Tablet Pen Pen (0)" --type=float "Coordinate Transformation Matrix" 0.6 0 0.4 0 1 0 0 0 1
