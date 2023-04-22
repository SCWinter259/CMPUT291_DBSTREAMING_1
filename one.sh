#!/usr/bin/bash

echo "Bash script started"

git add .

read -p "Enter your commit message: " MES

while ["$MES" = ""]; do
    read -p "Your message is empty! Enter a proper message: " MES
done

git commit -m "$MES"

echo $MES

echo "Bash script executed successfully"