#!/bin/bash
set -x
git pull

git status | grep images | while read -r directory ; do
	git add "$directory"
	git commit -m "Images"
	git push
done
