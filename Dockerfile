FROM pytorch/pytorch:latest

RUN apt-get -y update
RUN apt-get -y install openslide-tools
RUN apt-get -y install python3-openslide
RUN apt-get -y install libgl1-mesa-glx
RUN apt-get -y install git
RUN apt-get -y install build-essential 

RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install seaborn
RUN pip install openslide-python
RUN pip install opencv-python
RUN pip install aicspylibczi
RUN pip install albumentations
RUN pip install sklearn
RUN pip install notebook
RUN pip install torchviz

RUN pip install progress
RUN pip install tensorflow
RUN pip install ptitprince

#TODO
RUN pip install pickle5

RUN pip install torchmetrics
RUN pip install mxnet
RUN pip install pytorch-msssim
RUN pip install paquo
RUN pip install shapely

WORKDIR /METHnet_GBM_segmentation


COPY . .


CMD [ "python", "./src/main.py" ]