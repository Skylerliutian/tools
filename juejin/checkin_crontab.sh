#!/bin/bash

source /etc/profile
corntabFunc() {
    echo `date "+begin at %Y-%m-%d %H:%M:%S"` >> ~/Desktop/tools/juejin/log &&

    cd ~/Desktop/tools/juejin &&

    /opt/homebrew/bin/python3 index.py >> ~/Desktop/tools/juejin/log

    echo 'finish----------------------------------------' >> ~/Desktop/tools/juejin/log
}


corntabFunc
# date