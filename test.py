import keyboard
import cv2
import threading

def count_q_key():
    count = 0
    
    while True:
        try:
            keyboard.wait('q')
            count += 1
            print(f"Number of times 'q' key pressed: {count}")
            
            if count == 1:
                object_detection_thread = threading.Thread(target=detect_object)
                object_detection_thread.start()
                
        except KeyboardInterrupt:
            break

def detect_object():
    # Perform object detection here
    # Replace this code with your actual object detection logic
    # For example, using OpenCV's Haar cascaqdes:
    face_cascade = cv2.CascadeClassifier('C:/Yolo/multi-pose-landmark-mediapipe-main/cascade3.xml')  # Replace with appropriate cascade file
    video_capture = cv2.VideoCapture(0)  # Replace with appropriate video capture source
    
    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        if len(faces) > 0:
            print("Object detected!")
        
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    video_capture.release()
    cv2.destroyAllWindows()

# Start counting and detection in separate threads
counting_thread = threading.Thread(target=count_q_key)
counting_thread.start()
