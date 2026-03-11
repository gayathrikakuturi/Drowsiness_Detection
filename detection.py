import cv2
import mediapipe as mp
import numpy as np
import winsound

# -----------------------------
# Functions
# -----------------------------

def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)


def mouth_aspect_ratio(mouth):
    A = np.linalg.norm(mouth[1] - mouth[5])
    B = np.linalg.norm(mouth[2] - mouth[4])
    C = np.linalg.norm(mouth[0] - mouth[3])
    return (A + B) / (2.0 * C)


# -----------------------------
# Mediapipe Setup
# -----------------------------

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# -----------------------------
# Landmark Indexes
# -----------------------------

LEFT_EYE = [33,160,158,133,153,144]
RIGHT_EYE = [362,385,387,263,373,380]

MOUTH = [78,81,13,311,308,402]

# -----------------------------
# Thresholds
# -----------------------------

EAR_THRESHOLD = 0.25
MAR_THRESHOLD = 0.65

FRAME_THRESHOLD = 20
YAWN_FRAMES = 15

# -----------------------------
# Counters
# -----------------------------

blink_count = 0
yawn_count = 0

eye_counter = 0
yawn_counter = 0

alarm_on = False

# -----------------------------
# Camera
# -----------------------------

cap = cv2.VideoCapture(0)

cv2.namedWindow("Driver Drowsiness Detection", cv2.WINDOW_NORMAL)

# -----------------------------
# Main Loop
# -----------------------------

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame,1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    status = "ALERT"

    if results.multi_face_landmarks:

        mesh_points = np.array([
            np.multiply([p.x, p.y],
            [frame.shape[1], frame.shape[0]]).astype(int)
            for p in results.multi_face_landmarks[0].landmark
        ])

        left_eye = mesh_points[LEFT_EYE]
        right_eye = mesh_points[RIGHT_EYE]
        mouth = mesh_points[MOUTH]

        leftEAR = eye_aspect_ratio(left_eye)
        rightEAR = eye_aspect_ratio(right_eye)

        ear = (leftEAR + rightEAR) / 2

        mar = mouth_aspect_ratio(mouth)

        # -----------------------------
        # Blink Detection
        # -----------------------------

        if ear < EAR_THRESHOLD:

            eye_counter += 1

            if eye_counter >= FRAME_THRESHOLD:

                status = "SLEEPY"

                if not alarm_on:
                    winsound.PlaySound("music.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    alarm_on = True

        else:

            if eye_counter > 2:
                blink_count += 1

            eye_counter = 0
            alarm_on = False
            winsound.PlaySound(None, winsound.SND_PURGE)

        # -----------------------------
        # Yawn Detection
        # -----------------------------

        if mar > MAR_THRESHOLD:

            yawn_counter += 1

            if yawn_counter >= YAWN_FRAMES:
                yawn_count += 1
                yawn_counter = 0

        else:
            yawn_counter = 0

        # -----------------------------
        # Driver Status
        # -----------------------------

        if ear < 0.21:
            status = "SLEEPY"
        elif ear < 0.25:
            status = "DROWSY"
        else:
            status = "ALERT"

        # -----------------------------
        # Draw Landmarks
        # -----------------------------

        for point in left_eye:
            cv2.circle(frame, tuple(point), 2, (0,255,0), -1)

        for point in right_eye:
            cv2.circle(frame, tuple(point), 2, (0,255,0), -1)

        for point in mouth:
            cv2.circle(frame, tuple(point), 2, (255,0,0), -1)

        # -----------------------------
        # Display Information
        # -----------------------------

        cv2.putText(frame, f"EAR: {ear:.2f}", (30,40),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

        cv2.putText(frame, f"Blinks: {blink_count}", (30,80),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)

        cv2.putText(frame, f"Yawns: {yawn_count}", (30,120),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)

        cv2.putText(frame, f"STATUS: {status}", (30,160),
                    cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,0,255),3)

    cv2.imshow("Driver Drowsiness Detection", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()