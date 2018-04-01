# Text_Recognizer

A Machine Learning project which recognizes text from image using OpenCV framework.
It passes the image through various object recognition steps like Normalization, Thresholding, Line Segmentation,
Character Segmentation etc., and then uses Support Vector Classifier to classify the image as on of the character. 

## Getting Started
This Project can be used via two files called main.py and Classify.py.
Where main.py takes two command line args --image_path and --output_file contains name of output_file, 
where the output is going to stored. The main.py file recognizes and separates all characters and pass
them to Classify.py to classify the character, whereas Classify.py takes a single character image with 
--image_path command line argument and classify the character in it.

## Usage
Using main.py: 

```python main.py --image_path img.jpg --output_file out.txt```

Using Classify.py: 

```python Classify.py --image_path img.jpg```






## Built With

* [Scikit-learn](http://scikit-learn.org/stable/documentation.html) - The framework containing implementation for
various Machine Learning Algorithms
* [OpenCV](https://docs.opencv.org/2.4/doc/tutorials/tutorials.html) - The framework containing various methods for 
manipulating image.





