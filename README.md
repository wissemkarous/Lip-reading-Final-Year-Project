# Lip-readingPFA
This deep learning project is about Lip Reading which is a technique of understanding speech by visually interpreting the movements of the lips
so, we implemented this Lip Reading by using deep learning. It can be used for hard-of hearing people or to get some information from video without sound.

# Objective
Lip Reading relies on the kind of the language and, in this project, we chose Hangul as the language to implement the Lip Reading.

# Abstract
In this study, we propose a deep neural network for reconstructing intelligible speech from silent lip movement videos. We use auditory spectrogram as spectral representation of speech and its corresponding sound generation method resulting in a more natural sounding reconstructed speech. Our proposed network consists of an autoencoder to extract bottleneck features from the auditory spectrogram which is then used as target to our main lip reading network comprising of CNN, LSTM and fully connected layers. Our experiments show that the autoencoder is able to reconstruct the original auditory spectrogram with a 98% correlation and also improves the quality of reconstructed speech from the main lip reading network. Our model, trained jointly on different speakers is able to extract individual speaker characteristics and gives promising results of reconstructing intelligible speech with superior word recognition accuracy.
