import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
import streamlit as st
from sklearn.cluster import KMeans

 

class App:
# Code From Notebook
    def __init__(self):
        self.image = None
        self.k = None
        self.placeholder = st.empty()
    def runOnPress(self):
        with st.spinner("Please Wait..."):
            pc = st.empty() 
        
            with pc.container():
                st.session_state.page = 1
                st.title("Color Picker and Image Segmentation Tool ")

                st.text("This tool will generate a downloadable color pallete for your image, and also a segmented image using K Means") 
                bytes = self.image.read()
                file_bytes = np.asarray(bytearray(bytes))
                img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            
                img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                img_flat = img.reshape((-1,3))

                km = KMeans(n_clusters = self.k)

                km.fit(img_flat)

                centers = np.array(km.cluster_centers_,dtype='uint8')

                i=0
                fig,ax = plt.subplots(1,self.k)
                colors=[]
                for color in centers:
                    colors.append(color)
                    a=np.zeros((100,100,3),dtype='uint8')
                    a[:,:,:]=color
                    ax[i].imshow(a)
                    ax[i].axis("off")
                    i+=1                                              
                fig.savefig("Color_Pallete.png")

                a = cv2.imread("Color_Pallete.png")
                a = cv2.cvtColor(a,cv2.COLOR_BGR2RGB)

                
                st.image(a, width = 300)
                st.download_button("Down Color Pallter",open("Color_Pallete.png","rb"), "Color_Pallete.png", use_container_width= True)


                seg_img=np.zeros((img_flat.shape[0],3),dtype='uint8')
                for ix in range(seg_img.shape[0]):
                    seg_img[ix]=colors[km.labels_[ix]]
                seg_img=seg_img.reshape((img.shape))
                
                cv2.imwrite("Segmented Image.png",seg_img)

                st.image(seg_img, width = 500)
                st.download_button("Download Segmented Image",open("Segmented Image.png","rb"), "Segmented Image.png", use_container_width= True)



    def run(self):
        with self.placeholder.container():

            st.session_state.page = 0 
            ## Set Up the screen
            st.title("Color Picker and Image Segmentation Tool ")

            st.caption("This tool will generate a downloadable color pallete for your image, and also a segmented image using K Means") 

            st.subheader("Upload a Image or Take a Picture")
            radio = st.radio("Provide Image", ("Upload an Image", "Take a Picture"))
            if(radio == "Upload an Image"):
                  self.image = st.file_uploader("Upload an Image",type = ['png','jpeg','jpg'] , accept_multiple_files= False)
            elif(radio == "Take a Picture"):
                 self.image = st.camera_input("Take a Picture")
            self.k = st.slider("Pick how many colors to pick(k value in k means, default is 5)",1,10,5)

    
            btn = st.button("PICK COLOR AND SEGMENT IMAGE", on_click= self.runOnPress, type='primary', use_container_width= True)

            if btn:
                self.placeholder.empty()
app = App()
app.run() 