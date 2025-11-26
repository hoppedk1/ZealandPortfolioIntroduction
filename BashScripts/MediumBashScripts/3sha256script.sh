#!/bin/bash

read -p "path and name of the file: " file;
echo "sha256sum: "
sha256sum $file;


