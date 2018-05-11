#!/usr/bin/env bash

OUTPUT=train.vec
INFO_FILE=info.dat
BG_FILE=bg.txt
NUM=400
WEIGHT=92
HIGHT=112

opencv_createsamples \
    -vec $OUTPUT \
    -info $INFO_FILE \
    -bg $BG_FILE \
    -num $NUM \
    -show \
    -w $WEIGHT \
    -h $HIGHT