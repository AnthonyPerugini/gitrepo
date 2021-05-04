#! /bin/bash

echo "python3 $(pwd)/gitrepo.py \$1" >> gitrepo

pip install -r requirements.txt

sudo chmod +x gitrepo
sudo mv gitrepo /usr/bin/gitrepo
