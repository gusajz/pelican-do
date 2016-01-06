#!/bin/bash
VERSION=v"$(python setup.py --version)"

echo Deploying \"${VERSION}\"


if [ -n "$(git status --porcelain)" ]
then
  echo "Everything should be commited before deploying"
  exit
fi

echo 'Tagging'
git tag -a $VERSION

echo 'Uploading'
python setup.py register -r pypi
