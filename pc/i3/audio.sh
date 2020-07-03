#!/bin/bash

# pulseaudio initialisation
pkill pulseaudio 
sleep 1

pulseaudio --start -D
sleep 1

id=$(pactl list short sinks | grep Arctis | cut -c 1)

pactl set-default-sink $id

