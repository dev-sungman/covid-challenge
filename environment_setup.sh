DIR="$( cd "$( dirname -- $0 )" && pwd -P )"

export nnUNet_raw_data_base=$DIR'/nnUNet_raw_data_base'
export nnUNet_preprocessed=$DIR'/nnUNet_preprocessed'
export RESULTS_FOLDER=$DIR'/nnUNet_trained_models'
export PYTHONPATH='{PYTHONPATH}:'$DIR
