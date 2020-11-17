import os
import sys
import shutil
import argparse
import pathlib

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, default=None)

    return parser.parse_args()

def main(args):

    test_path = args.data_path
    submission_path = os.path.join(test_path, 'submission')

    e_list = [180, 189, 287, 318] # specially, must add _0

    pathlib.Path(submission_path).mkdir(parents=True, exist_ok=True)

    for _file in os.listdir(test_path):
        file_ext = _file.split('.')[-1]

        if file_ext == 'gz':
            file_path = os.path.join(test_path, _file)

            idx = _file.split('.')[0][-3:]

            if int(idx) in e_list:
                idx = idx + '_0'

            new_file = '{}.nii.gz'.format(idx)
            new_file_path = os.path.join(submission_path, new_file)

            shutil.move(file_path, new_file_path)
            print('{} --> {}'.format(_file, new_file))

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
