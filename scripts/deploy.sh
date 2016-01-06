#!/bin/bash
VERSION=v"$(python setup.py --version)"

echo Deploying \"${VERSION}\"


if [ -n "$(git status --porcelain)" ]
then
  echo "Everything should be commited before deploying"
  exit
fi

git tag -a $VERSION
