import cv2
import mediapipe as mp
from random import randrange


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        mp_hands = mp.solutions.hands
        with mp_hands.Hands(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
            while self.video.isOpened():
                success, image = self.video.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    continue
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = hands.process(image)

                # Drawing the hand annotations on the image.
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            image,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())

                # Adjusting size of displayed image based on distance between tip of thumb and index finger along y-axis.                         
                try:
                    thumb_tip_y = round(results.multi_hand_landmarks[0].landmark[4].y, 4)
                    index_tip_y = round(results.multi_hand_landmarks[0].landmark[8].y, 4)
                    diff = abs((thumb_tip_y - index_tip_y))*1500
                    print(str(diff))
                    frame_flip = cv2.flip(image, 1)
                    frame_final = cv2.resize(
                    frame_flip, (int(2*diff), int(diff)))
                except Exception as e:
                    print("Couldn't calculate difference between points"+ str(e))
                    frame_final = cv2.flip(image, 1)


                ret, jpeg = cv2.imencode('.jpg', frame_final)
                return jpeg.tobytes()


