#!/usr/bin/env bash

START_LINE=`head -n1 .git/COMMIT_EDITMSG`
PATTERN="\w+\-\d+\:\s.+"

if ! [[ "$START_LINE" =~ $PATTERN ]]; then
  echo "Bad commit message, see example: IMQA-123: commit message"
  exit 1
fi