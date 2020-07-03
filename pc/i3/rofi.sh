#!/bin/bash
if [ "$1" = "run" ]; then
	a="run"
elif [ "$1" = "ssh" ]; then
	a="ssh"
fi

rofi -show $a -columns 1 -lines 3
