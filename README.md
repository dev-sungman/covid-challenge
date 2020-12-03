
# COVID-19 Challenge

### Root

|── README.md

|── environment_setup.sh

|── conver_testformat.py

|── nnunet

|── nnUNet_raw_data_base ([download](https://drive.google.com/drive/folders/194hHX5cOFoPi0VvIKNMoAIqHppG1YwWI?usp=sharing))

|── nnUNet_preprocessed ([download](https://drive.google.com/drive/folders/1bcpLwVSd_QFEm_GLR0a2RddIqa4RIC-M?usp=sharing))

|── nnUNet_trained_models (If you train the model, it will be made automatically)



### Setting Environment

```
source ./environment_setup.sh
```



### Training

**New arguments**

* '$save_name': your trained results will be saved here.
* --use_nnblock: if you want to use 3D nnblock, please use this argument
* --use_ws : if you want to use weight standardization, please use this argument
* --use_skip_attention : if you want to use skip attention, please use this argument
* -w $path_to_pretrainedWeight : load pretrained weight by Model genesis


```bash
CUDA_VISIBLE_DEVICES=1 python nnunet/run/run_training.py 3d_fullres nnUNetTrainerV2 Task000_MYTASK all '$save_name' --use_nnblock --use_ws -w genesis_nnunet_luna16_006.model
```

If you run above the script, you can find your training results:

> nnUNet_trained_models/nnUNet/3d_fullres/Task000_MYTASK/nnUNetTrainer....v2.1/$save_name/all



### Inference

* You have to rename your .model, .pkl files. Please change the name of the model and pickle files named 'model_best.model', 'model_best.model.pkl' by following the below conditions.

  > model : model_final_checkpoint.model
  >
  > pickle : model_final_checkpoint.model.pkl

```bash
CUDA_VISIBLE_DEVICES=1 python nnunet/inference/predict_simple.py -i nnUNet_raw_data_base/nnUNet_raw_data/Task000_MYTASK/imagesTs -o '$output_path' -t Task000_MYTASK -m 3d_fullres -f all
```



* If you don't want to rename your model, please add '-chk model_best' argument
* $save_name : if you trained with '$save_name' argument, you have to input --name='$save_name' argument in inference phase.

```bash
CUDA_VISIBLE_DEVICES=1 python nnunet/inference/predict_simple.py -i nnUNet_raw_data_base/nnUNet_raw_data/Task000_MYTASK/imagesTs -o '$output_path' -t Task000_MYTASK -m 3d_fullres -f all -chk model_best --name='$save_name'
```



### Convert Data (for submission)

If you finished the inference, you can check a new folder named $output_path

```bash
python convert_testformat.py --data_path='$output_path'
```



Then, you can find submission folder in your '$output_path'.

please compress it and submit.
