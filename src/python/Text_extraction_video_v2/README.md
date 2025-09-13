# Video to Text Extractor

This project extracts text from a video file by first converting the video into frames and then running Optical Character Recognition (OCR) on those frames.

## Prerequisites

Before running this project, you need to install system dependencies.

### For Debian/Ubuntu-based systems:
```bash
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
sudo apt install imagemagick