#!/bin/bash

git checkout -b $1

if [[ $? -eq 0 ]]; then
	echo Success
else
	echo Fail
fi
