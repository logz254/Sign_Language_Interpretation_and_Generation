import cv2
import numpy as np
import os

# Create the directory structure
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    #os.makedirs("data/train/5")
    #os.makedirs("data/train/6")
    #os.makedirs("data/train/7")
    #os.makedirs("data/train/8")
    #os.makedirs("data/train/9")
    os.makedirs("data/train/N")
    os.makedirs("data/train/O")
    os.makedirs("data/train/P")
    os.makedirs("data/train/Q")
    os.makedirs("data/train/R")
    os.makedirs("data/train/S")
    os.makedirs("data/train/T")
    os.makedirs("data/train/U")
    os.makedirs("data/train/V")
    os.makedirs("data/train/W")
    os.makedirs("data/train/X")
    os.makedirs("data/train/Y")
    os.makedirs("data/train/Z")
    # os.makedirs("data/train/10")
    os.makedirs("data/test/5")
    os.makedirs("data/test/6")
    os.makedirs("data/test/7")
    os.makedirs("data/test/8")
    os.makedirs("data/test/9")
    # os.makedirs("data/test/10")
    

# Train or test 
mode = 'train'
directory = 'data/'+mode+'/'

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    count = {'n': len(os.listdir(directory+"/N")),
             'o': len(os.listdir(directory+"/O")),
             'p': len(os.listdir(directory+"/P")),
             'q': len(os.listdir(directory+"/Q")),
             'r': len(os.listdir(directory+"/R")),
             's': len(os.listdir(directory+"/S")),
             't': len(os.listdir(directory+"/T")),
             'u': len(os.listdir(directory+"/U")),
             'v': len(os.listdir(directory+"/V")),
             'w': len(os.listdir(directory+"/W")),
             'x': len(os.listdir(directory+"/X")),
             'y': len(os.listdir(directory+"/Y")),
             'z': len(os.listdir(directory+"/Z"))}
             # 'ten': len(os.listdir(directory+"/10"))}
    
    # Printing the count in each set to the screen
    #For colors it is (B,G,R)
    cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (51,144,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (51,144,255), 1)
    cv2.putText(frame, "N : "+str(count['n']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (51,144,255), 1)
    cv2.putText(frame, "O : "+str(count['o']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (51,144,255), 1)
    cv2.putText(frame, "P : "+str(count['p']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (51,144,255), 1)
    cv2.putText(frame, "Q : "+str(count['q']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (51,144,255), 1)
    cv2.putText(frame, "R : "+str(count['r']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (51,144,255), 1)
    cv2.putText(frame, "S : " + str(count['s']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (51, 144, 255), 1)
    cv2.putText(frame, "T : " + str(count['t']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (51, 144, 255), 1)
    cv2.putText(frame, "U : " + str(count['u']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (51, 144, 255), 1)
    cv2.putText(frame, "V : " + str(count['v']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (51, 144, 255), 1)
    cv2.putText(frame, "W : " + str(count['w']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (51, 144, 255), 1)
    cv2.putText(frame, "X : " + str(count['x']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (51, 144, 255), 1)
    cv2.putText(frame, "Y : " + str(count['y']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (51, 144, 255), 1)
    cv2.putText(frame, "Z : " + str(count['z']), (10, 360), cv2.FONT_HERSHEY_PLAIN, 1, (51, 144, 255), 1)
    # cv2.putText(frame, "TEN : "+str(count['ten']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (51,144,255), 1)
    
    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (64, 64)) 
 
    cv2.imshow("Frame", frame)
    
    #_, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
    #kernel = np.ones((1, 1), np.uint8)
    #img = cv2.dilate(mask, kernel, iterations=1)
    #img = cv2.erode(mask, kernel, iterations=1)
    # do the processing after capturing the image!
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    if interrupt & 0xFF == ord('N'):
        cv2.imwrite(directory+'N/'+str(count['n'])+'.jpg', roi)
    if interrupt & 0xFF == ord('O'):
        cv2.imwrite(directory+'O/'+str(count['o'])+'.jpg', roi)
    if interrupt & 0xFF == ord('P'):
        cv2.imwrite(directory+'P/'+str(count['p'])+'.jpg', roi)
    if interrupt & 0xFF == ord('Q'):
        cv2.imwrite(directory+'Q/'+str(count['q'])+'.jpg', roi)
    if interrupt & 0xFF == ord('R'):
        cv2.imwrite(directory+'R/'+str(count['r'])+'.jpg', roi)
    if interrupt & 0xFF == ord('S'):
        cv2.imwrite(directory + 'S/' + str(count['s']) + '.jpg', roi)
    if interrupt & 0xFF == ord('T'):
        cv2.imwrite(directory + 'T/' + str(count['t']) + '.jpg', roi)
    if interrupt & 0xFF == ord('U'):
        cv2.imwrite(directory + 'U/' + str(count['u']) + '.jpg', roi)
    if interrupt & 0xFF == ord('V'):
        cv2.imwrite(directory + 'V/' + str(count['v']) + '.jpg', roi)
    if interrupt & 0xFF == ord('W'):
        cv2.imwrite(directory + 'W/' + str(count['w']) + '.jpg', roi)
    if interrupt & 0xFF == ord('X'):
        cv2.imwrite(directory + 'X/' + str(count['x']) + '.jpg', roi)
    if interrupt & 0xFF == ord('Y'):
        cv2.imwrite(directory + 'Y/' + str(count['y']) + '.jpg', roi)
    if interrupt & 0xFF == ord('Z'):
        cv2.imwrite(directory + 'Z/' + str(count['z']) + '.jpg', roi)
    # if interrupt & 0xFF == ord('10'):
    #     cv2.imwrite(directory+'10/'+str(count['ten'])+'.jpg', roi)
    
cap.release()
cv2.destroyAllWindows()
"""
d = "old-data/test/0"
newd = "data/test/0"
for walk in os.walk(d):
    for file in walk[2]:
        roi = cv2.imread(d+"/"+file)
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
        cv2.imwrite(newd+"/"+file, mask)     
"""
