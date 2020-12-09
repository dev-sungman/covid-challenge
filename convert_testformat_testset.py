import os
import sys
import shutil
import argparse
import pathlib
import json

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('data_path', type=str, default=None)

    return parser.parse_args()

def main(args):

    test_path = args.data_path
    submission_path = os.path.join(test_path, 'submission')
    pathlib.Path(submission_path).mkdir(parents=True, exist_ok=True)

    test_table = json.load(open('testset_table.json', 'r'))
    for _file in os.listdir(test_path):
        file_ext = _file.split('.')[-1]

        if file_ext == 'gz':
            file_path = os.path.join(test_path, _file)
            
            matching_file = test_table[str(_file.split('.')[0])+'_0000.nii.gz']
            
            if matching_file[0] == 'C' : #COVID**
                new_file = '-'.join(matching_file.split('-')[3:])[:-10] +'.nii.gz'
                new_file = os.path.join(submission_path, new_file)
            
            else: #019
                new_file = '-'.join(matching_file.split('-')[3:])[:-10] +'.nii.gz'
                new_file = os.path.join(submission_path, new_file[1:])

            
            shutil.move(file_path, new_file)
            print('{} \n---> {}\n'.format(file_path, new_file))

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
