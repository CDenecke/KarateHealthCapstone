# Project Title

Image Processing Server

## Description
This imageprocessingserver is used to subtract the background of images leaving only the object of interest in the frame. This will drastically reduce the noise in an image for other programs that process these images.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
You must be using python 3.5, and pip3. It is also recommended you install conda to install tensorflow, as there have been issues installing.

This server was tested and run on an Amazon Web Server p2.xlarge using the ubuntu OS.

I would also recommend you run this on the Amazon Web Server or a system with a single NVIDIA K80 GPU.


### Installing
First clone this repository. In the imageprocessingserver folder run the command

```
pip3 install -r  requirements.txt
```

## Running the serer

Once  you have all the requirements properly installed you can run the server with the command
```
python3 segmentation_image_server.py
```

## Testing the Servre
See remoteSegmentationTest file's README.md

## Contributing

Please see the original mask-rcnn we forked at https://github.com/multimodallearning/pytorch-mask-rcnn by lasseha
