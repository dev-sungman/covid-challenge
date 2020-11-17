
# COVID-19 Challenge

### Root

|── README.md

|── environment_setup.sh

|── conver_testformat.py

|── nnunet

|── data (please download the data via download link)



### Setting Environment

1. Setup environment path.

   ```
   # ./environment_setup.sh
   ```

2. Download the data [[link](https://drive.google.com/drive/folders/194hHX5cOFoPi0VvIKNMoAIqHppG1YwWI?usp=sharing)] and locate it in root directory. 
   

### Training

```bash
CUDA_VISIBLE_DEVICES=1 python nnunet/run/run_training.py 3d_fullres nnUNetTrainerV2 Task000_MYTASK -f 0
```



### Inference

```bash
CUDA_VISIBLE_DEVICES=1 python nnunet/inference/predict_simple.py -i /workspace/datasets/COVID-19-20_v2/imagesTs -o /workspace/scripts/nnUNet/tests -t Task000_MYTASK -m 3d_fullres -f 0
```



### Convert Data (for submission)

```bash
python convert_testformat.py --data_path='tests_bests'
```

