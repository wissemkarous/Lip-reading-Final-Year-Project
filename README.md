#   Lip-reading- final year Project :
This deep learning project is about Lip Reading which is a technique of understanding speech by visually interpreting the movements of the lips
so, we implemented this Lip Reading by using deep learning. It can be used for hard-of hearing people or to get some information from video without sound.

This is the keras implementation of Lip2AudSpec: Speech reconstruction from silent lip movements video. 
![image](https://github.com/wissemkarous/Lip-readingPFA/assets/115191512/b1a8a17b-da29-4424-9e5c-b3f51dd07a27)

# Objective :
Lip Reading relies on the kind of the language and, in this project, we chose Hangul as the language to implement the Lip Reading.
# My Model  : 
![3](https://github.com/wissemkarous/Lip-reading-Final-Year-Project/assets/115191512/f5c87939-e3cc-407a-aa82-63bd553b8f4d)
# Loss resulats : After using CTC Layer 
---> For 20 Epochs : <br>
![IMG_20231228_164428.jpg](https://github.com/wissemkarous/Lip-reading-Final-Year-Project/assets/115191512/7f546150-bac9-4ac2-aa03-2a06a7cbc9d3)
---> For 40 Epochs : <br>
![IMG_20231228_164457.jpg](https://github.com/wissemkarous/Lip-reading-Final-Year-Project/assets/115191512/6c5282e6-7276-4a27-8ece-fa31c3c5a576)


# Abstract :
In this study, we propose a deep neural network for reconstructing intelligible speech from silent lip movement videos. We use auditory spectrogram as spectral representation of speech and its corresponding sound generation method resulting in a more natural sounding reconstructed speech. Our proposed network consists of an autoencoder to extract bottleneck features from the auditory spectrogram which is then used as target to our main lip reading network comprising of CNN, LSTM and fully connected layers. Our experiments show that the autoencoder is able to reconstruct the original auditory spectrogram with a 98% correlation and also improves the quality of reconstructed speech from the main lip reading network. Our model, trained jointly on different speakers is able to extract individual speaker characteristics and gives promising results of reconstructing intelligible speech with superior word recognition accuracy.
 
