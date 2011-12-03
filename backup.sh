#!/bin/bash

GIT_PATH=`dirname $(readlink -f $0)`

echo "GIT path is $GIT_PATH"

# remove potential edits
git reset --hard

# get latest version
git pull origin master

# generate backup
$GIT_PATH/backup.py > $GIT_PATH/.encrypt.sh && chmod +x $GIT_PATH/.encrypt.sh && $GIT_PATH/.encrypt.sh

# generate commit
git add .
git commit -m "Updated backup from `date -s +F`"

git push origin master
