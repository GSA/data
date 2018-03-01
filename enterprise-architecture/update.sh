#!/bin/bash

set -e
set -o pipefail
set -x

BRANCH=itsp-update-$(date "+%Y-%m-%d")
REPO=$(git remote -v | grep "^origin.\+\(push\)" | awk '{print $2}' | perl -e 's/^(https:\/\/|git@)github.com[:\/](.+?)(\.git)?$/$2/' -pi)

git fetch origin
git checkout origin/master
git checkout -b $BRANCH

curl https://ea.gsa.gov/api/v0/itstandards | python3 json_to_csv.py > it-standards.csv

echo "it-standards.csv updated."

read -p "You may want to 'diff' the list in another terminal window. Press enter to continue"

git commit -am "update IT Standards List"
git push -u origin $BRANCH

open "https://github.com/$REPO/compare/$BRANCH?expand=1"
