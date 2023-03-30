#Facial recognition using OpenCV
import cv2
import time

# Load the cascade
face_cascade = cv2.CascadeClassifier('ok.xml')

# start a timer
start_time = time.time()
last_time = start_time;

#number of images saved
savedImages = 0

# function that  provides alterning rgb values
def rgb():
    r = 120
    g = 0
    b = 120
    while True:
        yield (r, g, b) # return a tuple of rgb values
        # example of the tuples  returned  by this function
        # (0, 0, 0)

        r = (r + 1) % 256
        g = (g + 1) % 256
        b = (b + 1) % 256

# To capture video from webcam.
cap = cv2.VideoCapture(0)   

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    
    for (x, y, w, h) in faces:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
        
        #save the image to the faces folder
        if(time.time() - last_time > 5):
            savedImages += 1
            #print(f'Image saved: {savedImages}')

            #saving instead of imwrite you can use imencode
            retval, buffer = cv2.imencode('.jpg', img[y:y+h, x:x+w])
            
            with open( 'FacialRecognition/Faces/face_smile_'+ str(int(time.time())) + ".jpg", 'wb') as f:
                f.write(buffer)
            


            #instead of saving the image, you can do something else
            #like send it to a server
            last_time = time.time()
            
        # Draw the rectangle around each face
        r, g, b = next(rgb())
        cv2.rectangle(img, (x, y), (x+w, y+h), (r,g,b), 2)
       # using the rgb function to get rgb values
        


    # Display
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Stop if escape key is pressed

