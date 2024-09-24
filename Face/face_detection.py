import cv2


class VideoCapture:
    # starting the camera
    start = cv2.VideoCapture(0)

    # checking if the camera input is working
    if not start.isOpened():
        print("Camera feed is not available. Exiting...")
        exit()

    while True:
        # get frames-by-frames
        ret, frame = start.read()

        if not ret:
            print("Software has not received frames to process. Exiting...")
            break

        face_cascade = cv2.CascadeClassifier(
            "C:/Users/Trina/PycharmProjects/22-23_CE301_roy_trina/Face"
            "/face_detector_haar_features.xml")  # add the xml file for the face

        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

        eye_cascade = cv2.CascadeClassifier(
            "C:/Users/Trina/PycharmProjects/22-23_CE301_roy_trina/Face/eye_detector_haar_features.xml")
        # add the xml file for the eyes

        eyes = eye_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=2)

        for (x, y, w, h) in faces:
            print("__", x, y, x + w, y + h)
            reg = frame[y:y + h, x:x + w]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # show the result
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    # End
    start.release()
    cv2.destroyAllWindows()
