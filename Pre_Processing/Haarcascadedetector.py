import cv2

# Function used to resize an image
def resize_image(img, dim=(650, 650)):
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized

# Function used to extract frames from a video
def get_video_frames(video_path):
    """Function to return a video's frames in a list.
    
    Args:
        video_path (str): Path to the video file.
    
    Returns:
        list: List of frames.
        bool: True if the video was successfully opened, False otherwise.
    """
    vidcap = cv2.VideoCapture(video_path)
    
    if not vidcap.isOpened():
        return [], False
    
    success, image = vidcap.read()
    all_frames = []
    
    while success:
        all_frames.append(image)
        success, image = vidcap.read()
    
    vidcap.release()  # Release the VideoCapture object
    return all_frames, True

# Function to extract lips from a frame using Haar cascade detector
def extract_lips_haar_cascade(haar_detector, frame):
    """Function to extract lips from a frame using Haar cascade detector.

    Args:
        haar_detector (cv2.CascadeClassifier): Haar cascade detector object.
        frame (numpy.ndarray): Input frame.

    Returns:
        tuple: A tuple containing the extracted lips ROI (Region of Interest)
               as a grayscale image and a boolean status indicating success.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    roi_gray = 0
    status = False

    # Detect faces in the frame
    faces = haar_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # If no faces are detected, return a resized version of the entire frame
    if len(faces) == 0:
        roi_gray = cv2.resize(gray, (150, 100))
        return roi_gray, status

    # Extract lips from the first detected face
    for (x, y, w, h) in faces:
        roi_gray = gray[y + (2 * h // 3):y + h, x:x + w]

    # Resize the extracted lips ROI
    roi_gray = cv2.resize(roi_gray, (150, 100))
    status = True
    return roi_gray, status

if __name__ == "__main__":
    face_cascade = cv2.CascadeClassifier("C:/Users/acer/Desktop/Wissem karous/pfa wissemkarous2023/Pre_Processing/haarcascade_frontalface_default.xml")
    video_path = "C:/Users/acer/Desktop/Wissem karous/pfa wissemkarous2023/bbaf2n.mp4"
    frames, status = get_video_frames(video_path)
    
    if status:
        detected = []
        for i, frame in enumerate(frames):
            img, status = extract_lips_haar_cascade(face_cascade, frame)
            detected.append(img)
            cv2.imshow(str(i), detected[-1])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error in getting video.")
