# Sign Language Interpretation and Generation - IS Project II

Sign Language has become an important part in the lives of the hearing impaired. It enables them to communicate with each other. However, it poses a challenge when it comes to communicating with healthy people as they may not necessarily understand sign language themselves. A human interpreter is thus required but they are expensive and not always reliable. This is where deep learning comes in. A convolutional neural network (CNN) and long short-term memory(LSTM) combined sign language interpretation system is designed. Also, a sign language generation system will be used to facilitate two-way communication. The systems will be connected using a PyQt GUI interface. This will enable users to select one of the two systems. By selecting sign language interpretation, the images will be captured by a camera, extraction of features will be using the trained CNN. The model identifies the Kenyan sign language through LSTM and output is generated. As for sign language generation, an end-to-end automatic speech recognition model will be implemented to convert speech to text. It is expected that the proposed systems will bridge the gap between the hearing impaired and healthy people.
