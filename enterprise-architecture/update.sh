#!/bin/bash

set -e
set -o pipefail

BRANCH=itsp-update-$(date "+%Y-%m-%d")
REPO=$(git remote -v | grep "^origin.\+\(push\)" | awk '{print $2}' | perl -e 's/^(https:\/\/|git@)github.com[:\/](.+?)(\.git)?$/$2/' -pi)

git fetch origin
git checkout origin/master
git checkout -b $BRANCH

python3 fetch.py > it-standards.csv

echo "it-standards.csv updated."

read -p "Next, you will be shown a diff of what's changed in CSV. Once you quit the reader, the changes will be committed. Press enter to continue.> "

# https://stackoverflow.com/a/37181160/358804
git diff --word-diff-regex="[^[:space:],]+"

git commit -am "update IT Standards List"
git push -u origin $BRANCH

open "https://github.com/$REPO/compare/$BRANCH?expand=1"
