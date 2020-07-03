#!/bin/env sh

pkill polybar

sleep 1;

polybar primaryBar &
polybar secondaryBar &
