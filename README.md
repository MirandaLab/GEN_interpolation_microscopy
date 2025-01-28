# abc

# Latent Diffusion Models for Video Frame Interpolation (LDMVFI)

This repository is adapted from [LDMVFI](https://github.com/danier97/LDMVFI), which leverages latent diffusion models (LDMs) for high-fidelity video frame interpolation (VFI). Existing VFI models primarily minimize L1/L2/VGG loss between their outputs and ground-truth frames. However, these metrics often fail to correlate with perceptual quality. LDMs have demonstrated exceptional results in generating visual content with high perceptual quality. This work harnesses their generative capabilities for VFI.

---

## **Paper**

For detailed insights into the methodology and results, refer to the [original paper](https://github.com/danier97/LDMVFI). Additionally, this repository incorporates custom modifications for specific test sets, detailed below.

---

## **Dependencies and Installation**

### Prerequisites
1. Install Conda if not already installed.
2. Create the environment and install dependencies:
   ```bash
   conda env create -f environment.yaml
   conda activate <environment_name>
   ```

---

## **Pre-trained Model**

Download the pre-trained model and configuration file:

- [Pre-trained Model](https://drive.google.com/file/d/1LdmfF0Tk8d1-sample-link)
- [Config File](https://github.com/danier97/LDMVFI/blob/main/configs/ldm/ldmvfi-vqflow-f32-c256-concat_max.yaml)

Place these files in your working directory.

---

## **Custom Test Set Implementation**

This repository includes a modified test set handler in the file `testset_custome.py`. This file dynamically generates sequences and handles input and ground truth frames for evaluation. Below are the key highlights of its functionality:

- **Dynamic Sequence Handling**: The file automatically generates sequence names for multiple sequences, making it adaptable to datasets with varying numbers of sequences.
- **Input Frame Processing**: For each sequence, it loads and transforms two input frames (`1.png` and `3.png`) from the `input` folder. Missing frames trigger a warning.
- **Ground Truth Frame Handling**: The corresponding ground truth frame (`2.png`) is loaded and transformed. If the ground truth frame is missing, a warning is logged.
- **Debugging Information**: The script prints the total number of successfully loaded input and ground truth frames, helping users verify the dataset's integrity.

The results will be saved in the directory `LDMVFI/eval_results/CustomData/`, and subfolders will be created for each sequence. For example, for `sequence1`, the results will be stored in `LDMVFI/eval_results/CustomData/sequence1/`.

---

## **Preparing Datasets**

### **Training Sets**
- [Vimeo-90K](http://toflow.csail.mit.edu/)
- [BVI-DVC Quintuplets](https://github.com/BVI-DVC)

### **Test Sets**
- [Middlebury](https://vision.middlebury.edu/)
- [UCF101](https://www.crcv.ucf.edu/research/data-sets/ucf101/)
- [DAVIS](https://davischallenge.org/)
- [SNU-FILM](https://github.com/JihyongOh/SNU-FILM)

### **Custom Dataset Structure**
The custom dataset used in this implementation follows this folder structure:
```
<data_directory>/
├── customedata/
│   ├── input/
│   │   ├── sequence1/
│   │   │   ├── 1.png
│   │   │   └── 3.png
│   │   ├── sequence2/
│   │   │   ├── 1.png
│   │   │   └── 3.png
│   │   ├── sequence3/
│   │   │   ├── 1.png
│   │   │   └── 3.png
│   │   └── ...
│   └── gt/
│       ├── sequence1/
│       │   └── 2.png
│       ├── sequence2/
│       │   └── 2.png
│       ├── sequence3/
│       │   └── 2.png
│       └── ...
```
Each sequence is stored in its own folder under `input` and `gt`. The `input` folder contains the input frames (`1.png` and `3.png`), while the `gt` folder contains the corresponding ground truth frame (`2.png`).

---

## **Evaluation**

### Evaluate using PSNR/SSIM/LPIPS metrics
For example, on the Middlebury dataset:
```bash
python evaluate.py \
--config configs/ldm/ldmvfi-vqflow-f32-c256-concat_max.yaml \
--ckpt <path/to/ldmvfi-vqflow-f32-c256-concat_max.ckpt> \
--dataset Middlebury_others \
--metrics PSNR SSIM LPIPS \
--data_dir <path/to/data/dir> \
--out_dir eval_results/ldmvfi-vqflow-f32-c256-concat_max/ \
--use_ddim
```

### Evaluate using FloLPIPS
To evaluate perceptual video metrics like FloLPIPS:
```bash
python evaluate_vqm.py \
--exp ldmvfi-vqflow-f32-c256-concat_max \
--dataset Middlebury_others \
--metrics FloLPIPS \
--data_dir <path/to/data/dir> \
--out_dir eval_results/ldmvfi-vqflow-f32-c256-concat_max/
```

---

## **Video Interpolation**

To interpolate a video in `.yuv` format:
```bash
python interpolate_yuv.py \
--net LDMVFI \
--config configs/ldm/ldmvfi-vqflow-f32-c256-concat_max.yaml \
--ckpt <path/to/ldmvfi-vqflow-f32-c256-concat_max.ckpt> \
--input_yuv <path/to/input/yuv> \
--size <spatial res of video, e.g. 1920x1080> \
--out_fps <output fps, should be 2 x original fps> \
--out_dir <desired/output/dir> \
--use_ddim
```

---

## **Citing**

If you use this repository or the adapted methods, please cite the original repository:

```
@misc{ldmvfi,
  author = {Danier97},
  title = {LDMVFI: Latent Diffusion Models for Video Frame Interpolation},
  year = {2023},
  url = {https://github.com/danier97/LDMVFI},
}
```

---

```

---
