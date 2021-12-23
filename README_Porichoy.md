# Text Data Generator for Porichoy

We generate image data in the following steps:

Generate using normal augmentation options built-in the trdg repo (use -na 2 argument for ground truth generation)
* For Bangla names
```
python run.py -c 15000 -i texts/test/bangla_names_mod.txt -l bn -w 5 -r -f 64 -k 3 -rk -bl 1 -rbl -na 2 -id images --output_dir bangla_names -t 4
  ```
  * For Common Bangla words
```
python run.py -c 20000 -i texts/all-words.txt -l bn -w 10 -r -f 64 -k 3 -rk -bl 1 -rbl -na 2 -id images --output_dir bangla_common_words -t 4
 ```
  * For Bangla Numbers
```
python run.py -c 7500 -rs -num -sym -l bn -f 64 -k 3 -rk -bl 1 -rbl -na 2 -id images -t 4 --output_dir bangla_nums
```
  * For Random Sequences
```
python run.py -c 7500 -rs -num -sym -l bn -f 64 -k 3 -rk -bl 1 -rbl -na 2 -id images -t 4 --output_dir random_seq
```
  * For long text lines
```
python run.py -c 1500 -i texts/all-words.txt -l bn -w 10 -f 64 -bl 1 -rbl -na 2 -id images --output_dir long -t 4
```
* Create the following directories
  * **gt_txt** - we move the labels.txt files created for every batch here
  * **bangla_common_words_gt** - ground truth for every image in this batch
  * **bangla_nums_gt** - ground truth for every image in this batch
  * **bangla_names_gt** - ground truth for every image in this batch
  * **random_seq_gt** - ground truth for every image in this batch
* Create separate ground truth txt files for every image from labels.txt file generated (use prepare_ground_truth.ipynb under trdg folder)
* Rename images for that batch (use prepare_ground_truth.ipynb under trdg folder)
* Create the following directories
  * images
  * labels
* Move all images of different batches to images folder and delete previous directories (do in terminal)
```
mv bangla_common_words/* images
mv bangla_names/* images
mv bangla_nums/* images
mv random_seq/* images
rm -r bangla_common_words
rm -r bangla_names
rm -r bangla_nums
rm -r random_seq
```
* Move all ground truths of different batches to labels folder and delete previous directories (do in terminal)
```
mv bangla_common_words_gt/* labels
mv bangla_names_gt/* labels
mv bangla_nums_gt/* labels
mv random_seq_gt/* labels
rm -r bangla_common_words_gt
rm -r bangla_names_gt
rm -r bangla_nums_gt
rm -r random_seq_gt
rm -r gt_txt
```
* Create a folder aug_images to save the augmented images
* Run augmentation pipeline (aug_pipeline.ipynb in trdg folder)