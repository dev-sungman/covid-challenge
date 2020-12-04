import os
import sys
import tqdm
import shutil
import argparse
import pathlib
import numpy as np
import SimpleITK as sitk
from scipy.ndimage.morphology import binary_fill_holes
from skimage.measure import label


def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, default=None)
    parser.add_argument('--save_path', type=str, default=None)
    return parser.parse_args()


def apply_boundary(mask_path, img_path='./nnUNet_raw_data_base/nnUNet_raw_data/Task000_MYTASK/imagesTs'):
    mask_sample = mask_path.split('/')[-1]
    img_meta = sitk.ReadImage(os.path.join(img_path, mask_sample.replace('.nii', '_0000.nii')))
    img = sitk.GetArrayFromImage(img_meta)

    mask_meta = sitk.ReadImage(mask_path)
    mask = sitk.GetArrayFromImage(mask_meta)

    img_mask = (img > -500).astype(int)
    img_mask = np.stack([binary_fill_holes(im) for im in img_mask])
    img_mask_cc = label(img_mask)
    img_mask_cc_label = sorted([(l, len(np.where(img_mask_cc == l)[0])) 
                                for l in np.unique(img_mask_cc)], key=lambda x: x[1], reverse=True)
    
    result_mask = mask * (img_mask_cc == img_mask_cc_label[1][0])
    result_mask_meta = sitk.GetImageFromArray(result_mask)
    for k in img_meta.GetMetaDataKeys():
        result_mask_meta.SetMetaData(k, img_meta.GetMetaData(k))
    sitk.WriteImage(result_mask_meta, mask_path)
    

def main(args):
    test_path = args.data_path
    submission_path = os.path.join(test_path, args.save_path)

    e_list = [180, 189, 287, 318] # specially, must add _0

    pathlib.Path(submission_path).mkdir(parents=True, exist_ok=True)
    for _file in os.listdir(test_path):
        file_ext = _file.split('.')[-1]

        if file_ext == 'gz':
            file_path = os.path.join(test_path, _file)
            apply_boundary(file_path)

            idx = _file.split('.')[0][-3:]

            if int(idx) in e_list:
                idx = idx + '_0'

            new_file = '{}.nii.gz'.format(idx)
            new_file_path = os.path.join(submission_path, new_file)

            shutil.move(file_path, new_file_path)
            print('{} --> {}'.format(_file, new_file))

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
