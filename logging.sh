#!/bin/bash

if [[ $(git log --format='%h' -n 1 $1) ]] ; then
    gitHash=$(git log --format='%h' -n 1 $1)
    echo $gitHash
else
    echo Fail
fi