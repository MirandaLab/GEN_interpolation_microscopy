
import glob
from typing import List
from PIL import Image
import torch
from torchvision import transforms
from torchvision.utils import save_image as imwrite
import os
from os.path import join, exists
import numpy as np
import time
from ldm.models.autoencoder import *

class TripletTestSet:
    def __init__(self):
        self.transform = transforms.Compose([
            transforms.ToTensor(),  # Converts the image to a tensor and scales values to [0, 1]
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # Normalizes the tensor to [-1, 1]
        ])

    def eval(self, model, sample_func, metrics=['PSNR', 'SSIM'], output_dir=None, resume=False):
        results_dict = {k: [] for k in metrics if k not in ['PSNR', 'SSIM', 'LPIPS']}  # Exclude metrics needing ground truth

        # Ensure output directory exists
        if not exists(output_dir):
            os.makedirs(output_dir)

        logfile = open(join(output_dir, 'results.txt'), 'a')

        # Iterate through all sequences
        for sequence in self.im_list:
            sequence_output_dir = join(output_dir, sequence)
            if not exists(sequence_output_dir):
                os.makedirs(sequence_output_dir)

            # Load initial frames for the current sequence
            frame_001 = self.input0_list[sequence][0]  # Frame 001
            frame_019 = self.input1_list[sequence][0]  # Frame 019

            # Generate frames according to the specified order
            # Step 1: Generate Frame 010 from Frame 001 and Frame 019
            xc_010 = {'prev_frame': frame_001, 'next_frame': frame_019}
            frame_010 = self.generate_frame(model, sample_func, xc_010, sequence_output_dir, 'frame_010.png')

            # Step 2: Generate Frame 005 from Frame 001 and Frame 010
            xc_005 = {'prev_frame': frame_001, 'next_frame': frame_010}
            frame_005 = self.generate_frame(model, sample_func, xc_005, sequence_output_dir, 'frame_005.png')

            # Step 3: Generate Frame 003 from Frame 001 and Frame 005
            xc_003 = {'prev_frame': frame_001, 'next_frame': frame_005}
            frame_003 = self.generate_frame(model, sample_func, xc_003, sequence_output_dir, 'frame_003.png')

            # Step 4: Generate Frame 002 from Frame 001 and Frame 003
            xc_002 = {'prev_frame': frame_001, 'next_frame': frame_003}
            frame_002 = self.generate_frame(model, sample_func, xc_002, sequence_output_dir, 'frame_002.png')

            # Step 5: Generate Frame 004 from Frame 005 and Frame 003
            xc_004 = {'prev_frame': frame_005, 'next_frame': frame_003}
            frame_004 = self.generate_frame(model, sample_func, xc_004, sequence_output_dir, 'frame_004.png')

            # Step 6: Generate Frame 007 from Frame 010 and Frame 005
            xc_007 = {'prev_frame': frame_010, 'next_frame': frame_005}
            frame_007 = self.generate_frame(model, sample_func, xc_007, sequence_output_dir, 'frame_007.png')

            # Step 7: Generate Frame 006 from Frame 007 and Frame 005
            xc_006 = {'prev_frame': frame_007, 'next_frame': frame_005}
            frame_006 = self.generate_frame(model, sample_func, xc_006, sequence_output_dir, 'frame_006.png')

            # Step 8: Generate Frame 008 from Frame 010 and Frame 007
            xc_008 = {'prev_frame': frame_010, 'next_frame': frame_007}
            frame_008 = self.generate_frame(model, sample_func, xc_008, sequence_output_dir, 'frame_008.png')

            # Step 9: Generate Frame 009 from Frame 010 and Frame 008
            xc_009 = {'prev_frame': frame_010, 'next_frame': frame_008}
            frame_009 = self.generate_frame(model, sample_func, xc_009, sequence_output_dir, 'frame_009.png')

            # Step 10: Generate Frame 015 from Frame 010 and Frame 019
            xc_015 = {'prev_frame': frame_010, 'next_frame': frame_019}
            frame_015 = self.generate_frame(model, sample_func, xc_015, sequence_output_dir, 'frame_015.png')

            # Step 11: Generate Frame 017 from Frame 019 and Frame 015
            xc_017 = {'prev_frame': frame_019, 'next_frame': frame_015}
            frame_017 = self.generate_frame(model, sample_func, xc_017, sequence_output_dir, 'frame_017.png')

            # Step 12: Generate Frame 016 from Frame 017 and Frame 015
            xc_016 = {'prev_frame': frame_017, 'next_frame': frame_015}
            frame_016 = self.generate_frame(model, sample_func, xc_016, sequence_output_dir, 'frame_016.png')

            # Step 13: Generate Frame 018 from Frame 017 and Frame 019
            xc_018 = {'prev_frame': frame_017, 'next_frame': frame_019}
            frame_018 = self.generate_frame(model, sample_func, xc_018, sequence_output_dir, 'frame_018.png')

            # Step 14: Generate Frame 013 from Frame 010 and Frame 015
            xc_013 = {'prev_frame': frame_010, 'next_frame': frame_015}
            frame_013 = self.generate_frame(model, sample_func, xc_013, sequence_output_dir, 'frame_013.png')

            # Step 15: Generate Frame 014 from Frame 013 and Frame 015
            xc_014 = {'prev_frame': frame_013, 'next_frame': frame_015}
            frame_014 = self.generate_frame(model, sample_func, xc_014, sequence_output_dir, 'frame_014.png')

            # Step 16: Generate Frame 012 from Frame 010 and Frame 013
            xc_012 = {'prev_frame': frame_010, 'next_frame': frame_013}
            frame_012 = self.generate_frame(model, sample_func, xc_012, sequence_output_dir, 'frame_012.png')

            # Step 17: Generate Frame 011 from Frame 010 and Frame 012
            xc_011 = {'prev_frame': frame_010, 'next_frame': frame_012}
            frame_011 = self.generate_frame(model, sample_func, xc_011, sequence_output_dir, 'frame_011.png')

        logfile.close()

    def generate_frame(self, model, sample_func, xc, output_dir, frame_name):
        """Generate a single frame based on the provided conditioning."""
        with torch.no_grad():
            with model.ema_scope():
                c, phi_prev_list, phi_next_list = model.get_learned_conditioning(xc)
                shape = (model.channels, c.shape[2], c.shape[3])
                out = sample_func(conditioning=c, batch_size=c.shape[0], shape=shape, x_T=None)
                if isinstance(out, tuple):
                    out = out[0]
                frame = model.decode_first_stage(out, xc, phi_prev_list, phi_next_list)
                frame = torch.clamp(frame, min=-1., max=1.)
        
        # Save the generated frame
        imwrite(frame, join(output_dir, frame_name), value_range=(-1, 1), normalize=True)
        return frame

class CustomData(TripletTestSet):
    def __init__(self, db_dir):
        super(CustomData, self).__init__()
        self.im_list = [f'sequence{i+1}' for i in range(186)]  # List of sequences
        
        self.input0_list = {}
        self.input1_list = {}
        
        # Load frames for each sequence
        for sequence in self.im_list:
            self.input0_list[sequence] = []
            self.input1_list[sequence] = []
            
            frame0_path = join(db_dir, 'input', sequence, 'frame_001.png')
            frame1_path = join(db_dir, 'input', sequence, 'frame_019.png')
            
            # Check if the frame files exist before loading
            if exists(frame0_path):
                self.input0_list[sequence].append(self.transform(Image.open(frame0_path).convert('RGB')).cuda().unsqueeze(0))
            else:
                print(f"Warning: {frame0_path} not found.")

            if exists(frame1_path):
                self.input1_list[sequence].append(self.transform(Image.open(frame1_path).convert('RGB')).cuda().unsqueeze(0))
            else:
                print(f"Warning: {frame1_path} not found.")
