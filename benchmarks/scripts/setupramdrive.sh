#!/bin/bash

mkdir /pgramdisk
mount -t tmpfs -o size=100m tmpfs /pgramdisk
mkdir /pgramdisk/pg_stat_tmp

exit 0
