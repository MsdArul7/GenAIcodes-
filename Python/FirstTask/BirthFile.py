import cv2
if __name__ == "__main__":
    video_path = "birthday_video.mp4"
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise Exception("Could not open Video file.")
    while True:
        success, frame = cap.read()
        if not success:
            break
        cv2.imshow("Birthday Video", frame)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
