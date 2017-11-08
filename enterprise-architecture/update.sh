#!/bin/bash

set -e
set -x

BRANCH=itsp-update-$(date "+%Y-%m-%d")
REPO=$(git remote -v | grep "^origin.\+\(push\)" | awk '{print $2}' | perl -e 's/^(https:\/\/|git@)github.com[:\/](.+?)(\.git)?$/$2/' -pi)

git fetch origin
git checkout origin/master
git checkout -b $BRANCH

mv ~/Downloads/tableExport.csv it-standards.csv

read -p "You may want to 'diff' the list in another terminal window. Press enter to continue"

git commit -am "update IT Standards List"
git push -u origin $BRANCH

open "https://github.com/$REPO/compare/$BRANCH?expand=1"
