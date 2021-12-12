# Text Data Generator for Porichoy

We generate image data in the following steps:

* Generate using normal augmentation options built-in the trdg repo (use -na 2 argument for ground truth generation)
* Create separate ground truth txt files for every image from labels.txt file generated (use prepare_ground_truth.ipynb under trdg folder)
* Rename images for that batch (use prepare_ground_truth.ipynb under trdg folder)
* Run augmentation pipeline (aug_pipeline.ipynb in trdg folder)