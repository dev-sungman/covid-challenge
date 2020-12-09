import os
import sys
import shutil
import argparse
import pathlib

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--sample_path', type=str, default=None)
    parser.add_argument('--data_path', type=str, default=None)

    return parser.parse_args()

def main(args):

    test_path = args.data_path
    submission_path = os.path.join(test_path, 'submission')
    #pathlib.Path(submission_path).mkdir(parents=True, exist_ok=True)
    
    post_number_dict = {}
    sample_path_list = os.listdir(args.sample_path)

    for _file in sample_path_list:
        file_ext = _file.split('.')[-1]
        
        if file_ext == 'gz':
            file_path = os.path.join(args.sample_path, _file)
            
            file_flag = 0 if len(_file.split('-')) > 1 else 1

            if file_flag == 0:
                idx = _file.split('_')[0]
                post_number = _file.split('_')[-1].split('.')[0]
                post_number_dict[idx] = post_number 
            
            else:
                if len(_file.split('_')) > 1:
                    idx = _file.split('_')[0].split('.')[0]
                    post_number = _file.split('_')[-1].split('.')[0]
                    post_number_dict[idx] = post_number
    
    print(post_number_dict)

    for _file in os.listdir(test_path):
        file_ext = _file.split('.')[-1]

        if file_ext == 'gz':
            file_path = os.path.join(test_path, _file)
            
            file_flag = 0 if len(_file.split('-')) > 1 else 1

            if file_flag == 0:
                base_name = '-'.join(_file.split('-')[3:])
                idx = base_name.split('_')[0]

                post_number = post_number_dict[idx]
                new_file = '{}_{}.nii.gz'.format(base_name.split('.')[0], post_number)
            else:
                base_name = _file.split('.')[0]
                if base_name in post_number_dict.keys():
                    post_number = post_number_dict[base_name]
                    new_file = '{}_{}.nii.gz'.format(base_name, post_number)
                else:
                    new_file = _file

            new_file_path = os.path.join(submission_path, new_file)

            #shutil.move(file_path, new_file_path)
            print('{} --> {}'.format(_file, new_file))

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
