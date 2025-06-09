# Cell_Interpolation_With_Diffusion

# Latent Diffusion Models for Video Frame Interpolation (LDMVFI)

This repository is adapted from [LDMVFI](https://github.com/danier97/LDMVFI), which leverages latent diffusion models (LDMs) for high-fidelity video frame interpolation (VFI). Existing VFI models primarily minimize L1/L2/VGG loss between their outputs and ground-truth frames. However, these metrics often fail to correlate with perceptual quality. LDMs have demonstrated exceptional results in generating visual content with high perceptual quality. This work harnesses their generative capabilities for VFI.

---

## **Paper**

For detailed insights into the methodology and results, please look at the (https://github.com/danier97/LDMVFI). Additionally, this repository incorporates custom modifications for specific test sets, detailed below.

---



## Installation Guide

Follow these steps to set up the environment and run the model.

# LDMVFI: Latent Diffusion Model for Video Frame Interpolation

A PyTorch-based implementation of Latent Diffusion Models for Video Frame Interpolation. This repository provides pretrained models and tools for high-quality frame generation in video sequences.

---

## 🔧 Installation Guide

Follow the steps below to set up the environment and run the model.

---

### ✅ Prerequisites

Ensure the following are installed on your system:

- [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- [Git](https://git-scm.com/)

---

### 📥 1. Clone the Repository

```bash
git clone https://github.com/danier97/LDMVFI.git
cd LDMVFI



## **Custom Test Set Implementation For the Odds and Evens Frames**

This repository includes a modified test set handler in the file `testset_custome.py`. This file dynamically generates sequences and handles input and ground truth frames for evaluation. Below are the key highlights of its functionality:

- **Dynamic Sequence Handling**: The file automatically generates sequence names for multiple sequences, making it adaptable to datasets with varying numbers of sequences.
- **Input Frame Processing**: For each sequence, it loads and transforms two input frames (`1.png` and `3.png`) from the `input` folder. Missing frames trigger a warning.
- **Ground Truth Frame Handling**: The corresponding ground truth frame (`2.png`) is loaded and transformed. If the ground truth frame is missing, a warning is logged.
- **Debugging Information**: The script prints the total number of successfully loaded input and ground truth frames, helping users verify the dataset's integrity.

The results will be saved in the directory `LDMVFI/eval_results/CustomData/`, and subfolders will be created for each sequence. For example, for `sequence1`, the results will be stored in `LDMVFI/eval_results/CustomData/sequence1/`.

---

### **Custom Dataset Structure the Odds and Evens Frames**
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
### Custom Dataset Evaluation Results
For the custom dataset, the evaluation results are saved in:
```
LDMVFI/eval_results/CustomData/
```
Within this directory, each sequence will have its own subfolder. For example:
```
LDMVFI/eval_results/CustomData/
├── sequence1/
│   ├── interpolated_frames/
│   ├── metrics.txt
│   └── ...
├── sequence2/
│   ├── interpolated_frames/
│   ├── metrics.txt
│   └── ...
├── sequence3/
│   ├── interpolated_frames/
│   ├── metrics.txt
│   └── ...
└── ...
```
This structure ensures that results for each sequence are organized and easily accessible.





## **Custom Test Set Implementation for Generating Intermediate Frames**

This repository includes a second modified test set handler, which can generate 16 intermediate frames between each pair of input frames. Below are the key highlights of its functionality:

- **Input Frame Requirements**: The input frames are named `frame_001.png` and `frame_019.png`, located in the `input` folder for each sequence. 
- **Intermediate Frame Generation**: Starting from `frame_001` and `frame_019`, the implementation dynamically generates frames `frame_002` to `frame_018` following a hierarchical approach.
- **No Ground Truth Required**: Unlike the previous test set, this setup does not rely on ground truth frames (`gt`) for evaluation.
- **Output Directory**: All generated frames for each sequence are saved in the same directory structure as the input frames. For example, results for `sequence1` will be saved in:

```
LDMVFI/eval_results/CustomData/
├── sequence1/
│   ├── frame_001.png
│   ├── frame_002.png
│   ├── frame_003.png
│   ├── ...
│   ├── frame_018.png
│   └── frame_019.png
├── sequence2/
│   ├── frame_001.png
│   ├── frame_002.png
│   ├── ...
│   └── frame_019.png
└── ...
```
- **Efficient Frame Hierarchy**: Frames are generated in a structured manner, ensuring consistency across multiple levels of interpolation.

---

### **Custom Dataset Structure for Intermediate Frame Generation**
The custom dataset used in this implementation follows this folder structure:
```
<data_directory>/
├── customedata/
│   ├── input/
│   │   ├── sequence1/
│   │   │   ├── frame_001.png
│   │   │   └── frame_019.png
│   │   ├── sequence2/
│   │   │   ├── frame_001.png
│   │   │   └── frame_019.png
│   │   ├── sequence3/
│   │   │   ├── frame_001.png
│   │   │   └── frame_019.png
│   │   └── ...
```
Each sequence is stored in its own folder under `input`. The `input` folder contains the starting and ending frames (`frame_001.png` and `frame_019.png`).

---

### Custom Dataset Evaluation Results for Intermediate Frames
For this dataset, the evaluation results are saved in:
```
LDMVFI/eval_results/CustomData/
```
Within this directory, each sequence will have its own subfolder containing all the generated frames. For example:
```
LDMVFI/eval_results/CustomData/
├── sequence1/
│   ├── frame_001.png
│   ├── frame_002.png
│   ├── frame_003.png
│   ├── ...
│   ├── frame_018.png
│   └── frame_019.png
├── sequence2/
│   ├── frame_001.png
│   ├── frame_002.png
│   ├── ...
│   └── frame_019.png
└── ...
```
This structure ensures that results for each sequence are organized and accessible for further analysis.

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
