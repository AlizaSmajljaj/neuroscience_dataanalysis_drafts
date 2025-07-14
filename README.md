# MESC to TIFF Converter

Converts neuroscience microscopy data (.mesc) to TIFF stacks for Suite2P analysis.

## Usage

1. Install requirements:
```bash
conda create -n mesc_convert python=3.9
conda activate mesc_convert
pip install h5py tifffile numpy
