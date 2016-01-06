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

if [ $? -eq 0 ]
then
  echo "Cannot tag"
  exit
fi

echo 'Uploading'
python setup.py sdist upload -r pypi
