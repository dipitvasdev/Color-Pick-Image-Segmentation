# Color Pallete Generator and Image Segmentation

This is a an web app which extract color pallete from an image provided using K Means algorithm. A color pallete is useful to organizations to maintain consistent look across Operating Systems and pages.  The code then uses these picked colors to recreate a image with the picked colors. A segmented image  a reconstruction of the image using only the colors that were segmented giving user an idea about where the colors were picked in the image. 


The followin Google Colab notebook and the one in the repository are the baseline code that power the demo website. 
Have a look here:- 

**GOOGLE COLAB:- https://colab.research.google.com/drive/1s9aSE83Us0JEHeCTpnaNo7bWYV5jEkqs**


This project has 2 parts :- 

   1) **COLOR PICKING** :- It picks a certain number of dominant colors from the given image, by the use of clustering from Kmeans Algorithm, this can then
   be used to create a color pallete out of an image. A color pallete is useful to organizations to maintain consistent look across Operating Systems and pages. 
  
  2) **SEGMENTATION** :- The code then uses these picked colors to recreate a image with the picked colors. This is a reconstruction of the image using only the colors that were segmented giving user an idea about where the colors were picked in the image. 
  

MODEL - K Means Clustering (Unsupervised)

GITHUB:- https://github.com/dipitvasdev
