#!/bin/bash
i
zscroll --before-text "  " --delay 0.25 --length 35 \
	--match-command "playerctl status" \
	--match-text "Playing" "--before-text '  '" \
	--match-text "Paused" "--before-text '  ' --scroll 0" \
	--update-check true "playerctl metadata --format \"{{artist}} - {{title}}\"" &
wait
