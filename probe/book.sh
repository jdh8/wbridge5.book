#!/bin/sh
# Probe every auction in probe/book.txt, one Wine prefix copy per job slot:
#   for i in $(seq 1 14); do cp -a --reflink=always wbridge5/prefix wbridge5/prefix$i; done
#   setsid probe/book.sh > probe/data/book.log 2>&1 &
cd "$(dirname "$0")/.." || exit
grep -v '^#' probe/book.txt | parallel -j14 --line-buffer --tag \
    'WINEPREFIX=wbridge5/prefix{%} python3 probe/tm.py -n 300 --seed 1 {=uq()=}'
