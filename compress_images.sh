#!/usr/bin/env bash

images=$( find . -name '*.png' )

for png in $images
do
  echo $png
  convert +dither -colors 256 $png ${png%%.png}.small.png
  if [ "$?" -eq 0 ]
  then
    mv ${png%%.png}.small.png $png
  fi
done