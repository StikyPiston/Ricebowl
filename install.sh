#!/bin/bash

echo "Welcome to the Ricebowl installer"
sudo cp -r ./* /usr/bin/
sudo mv /usr/bin/ricebowl-cli /usr/bin/ricebowl
sudo chmod +x /usr/bin/ricebowl

echo "Done! Happy ricing!"
