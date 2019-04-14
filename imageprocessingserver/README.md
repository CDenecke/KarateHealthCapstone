# Image Processing Server
## Description
This imageprocessingserver is used to subtract the background of images leaving only the object of interest in the frame. This will drastically reduce the noise in an image for other programs that process these images.

## Getting Started

These instructions will help get you up and running with this project on running on your local machine.

### Prerequisites
You must be using python 3.5, and pip3. It is also recommended you install conda to install tensorflow, as there have been issues installing.

This server was tested and run on an Amazon Web Server p2.xlarge using the ubuntu OS.

I would also recommend you run this on the Amazon Web Server or a system with a single NVIDIA K80 GPU.


### Installing
First clone this repository. In the imageprocessingserver folder run the commands
```
pip3 install -r  requirements.txt
```
```
python setup.py install
```

## Running the server

See the read me file in the prject folder.

## Testing the Servre
See project/remoteSegmentationTest file's README.md

## Traning the Network.
To train the network with your own custom data you will need to navigate to the README.md file located in
```
project/hands
```

## Contributing

Please see the original mask-rcnn we forked at https://github.com/matterport/Mask_RCNN

Please see the original vgg image anotator at http://www.robots.ox.ac.uk/~vgg/software/via/
