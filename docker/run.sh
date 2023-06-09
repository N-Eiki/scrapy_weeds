#!/bin/bash
xhost +
# /opt/X11/bin/xhost +

docker run -it --rm --privileged\
    --env="DISPLAY=host.docker.internal:0" \
    -v $HOME/.Xauthority:/root/.Xauthority \
    -v ${PWD}/../script:/workdir/scrayping/script\
    --name scrapying poetry_scrapy bash 

#   poetry run python scripts/amg.py --checkpoint /mnt/ckpt/sam_vit_h_4b8939.pth --model-type default --input /mnt/imgs/ノビル.jpg --output /mnt/output/

# import matplotlib.pyplot as plt;plt.plot([0, 1, 2]);plt.show()