import os
import argparse
import numpy as np
import SimpleITK as sitk


def get_argument():
    parser = argparse.ArgumentParser()

    # Data settings
    parser.add_argument('--tre_file_path', default='~/Datasets/Brain_MR_Angiography/TubeTK/original/Vessel_annotation_file')
    parser.add_argument('--nii_save_path', default='~/Datasets/Brain_MR_Angiography/TubeTK/original/Vessel')
    parser.add_argument('--org_MRA_path', default='~/Datasets/Brain_MR_Angiography/TubeTK/original/MRA')

    parser.add_argument('--img_depth', default=128, help='The original database voxel size')
    parser.add_argument('--img_height', default=448, help='The original database voxel size')
    parser.add_argument('--img_width', default=448, help='The original database voxel size')

    args = parser.parse_args()
    return args


def main():
    args = get_argument()

    # read all vessel annotation file (tre format)
    ann_list = [file for file in os.listdir(args.tre_file_path) if file.lower().endswith('.tre')]
    print('The number of annotation file is: ', len(ann_list))

    # process tre annotation file one-by-one
    for ann in ann_list:
        print('The processing file is: ', ann)

        # create the new array for vessel
        mask_arr = np.zeros((args.img_depth, args.img_height, args.img_width), dtype=np.int16)

        # set the lines information to processing voxel
        line_idx = -1                                                                                              # the read lines index
        group_id = 0
        NPoints_line = 25                                                                                      # the line of first annotation group NPoints
        start_line = -1
        end_line = -1

        # read the tre file
        with open(os.path.join(args.tre_file_path, ann)) as lines:
            for line in lines:
                line_idx = line_idx + 1                                                                        # start from 0

                if line_idx == 5:
                    group_num = int(line.split()[2])
                    print('The number of group in the annotation file is: ', group_num)

                if line_idx == NPoints_line:
                    NPoints = int(line.split()[2])
                    print('The %d-th group points is: %d' % (group_id, NPoints))
                    group_id = group_id + 1

                    if NPoints > 0:
                        start_line = NPoints_line + 2
                        end_line = NPoints_line + 2 + NPoints
                    NPoints_line = NPoints_line + NPoints + 15

                if line_idx >= start_line and line_idx < end_line:
                    point_data = line.split()
                    x, y, z, r = float(point_data[0]), float(point_data[1]), float(point_data[2]), float(point_data[3])

                    if np.floor(z - r) < 0:
                        origin = [0, int(np.floor(y - r)), int(np.floor(x - r))]
                    else:
                        origin = [int(np.floor(z - r)), int(np.floor(y - r)), int(np.floor(x - r))]
                    for k in range(int(np.ceil(2 * r))):
                        for j in range(int(np.ceil(2 * r))):
                            for i in range(int(np.ceil(2 * r))):
                                if np.sqrt(np.square(origin[0] + k - z) + np.square(origin[1] + j - y) + np.square(origin[2] + i - x)) <= r and origin[0] + k < 128:
                                    mask_arr[origin[0] + k, origin[1] + j, origin[2] + i] = 1

        # create NIfTI file for mask_arr
        org_img = sitk.ReadImage(fileName=os.path.join(args.org_MRA_path, ann[:-4] + '-MRA.mha'))
        mask_img = sitk.GetImageFromArray(arr=mask_arr)
        mask_img.SetSpacing(org_img.GetSpacing())
        mask_img.SetOrigin(org_img.GetOrigin())
        mask_img.SetDirection(org_img.GetDirection())
        sitk.WriteImage(image=mask_img, fileName=os.path.join(args.nii_save_path, ann[:-4] + '.nii.gz'))


if __name__ == '__main__':
    main()
