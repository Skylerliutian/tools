#!/bin/bash

# source /etc/profile
# corntabFunc() {
#     echo `date "+begin at %Y-%m-%d %H:%M:%S"` >> ~/Desktop/code/tools/juejin/log &&

#     cd ~/Desktop/code/tools/juejin &&

#     /opt/homebrew/bin/python3 index.py >> ~/Desktop/code/tools/juejin/log

#     echo 'finish----------------------------------------' >> ~/Desktop/code/tools/juejin/log
# }


# corntabFunc
PATH=$PATH:/usr/local/bin

echo `date "+begin at %Y-%m-%d %H:%M:%S"` >> log
python3 index.py >> log
echo 'finish----------------------------------------' >> log