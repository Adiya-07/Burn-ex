import cv2
import mediapipe as mp
import csv
import math


# Function to calculate angle
def calculate_angle(a, b, c):
    """
    Calculates the angle between three points.
    b is the joint (vertex).
    """
    ba = (a[0] - b[0], a[1] - b[1])
    bc = (c[0] - b[0], c[1] - b[1])

    dot = ba[0] * bc[0] + ba[1] * bc[1]

    mag_ba = math.sqrt(ba[0]**2 + ba[1]**2)
    mag_bc = math.sqrt(bc[0]**2 + bc[1]**2)

    if mag_ba == 0 or mag_bc == 0:
        return 0

    angle = math.degrees(math.acos(dot / (mag_ba * mag_bc)))
    return round(angle, 2)


# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils


# Create CSV file
csv_file = open("exercise_data.csv", "w", newline="")
writer = csv.writer(csv_file)

# CSV Header
writer.writerow([
    "frame",

    "left_shoulder_x", "left_shoulder_y",
    "right_shoulder_x", "right_shoulder_y",

    "left_hip_x", "left_hip_y",
    "right_hip_x", "right_hip_y",

    "left_knee_x", "left_knee_y",
    "right_knee_x", "right_knee_y",

    "left_ankle_x", "left_ankle_y",
    "right_ankle_x", "right_ankle_y",

    "left_knee_angle",
    "right_knee_angle"
])


# Path to video
video_path = "dataset/squats/squat_normal_1.mp4"

# Open video
cap = cv2.VideoCapture(video_path)

frame_number = 0


with mp_pose.Pose(
    static_image_mode=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as pose:

    while cap.isOpened():

        success, frame = cap.read()

        if not success:
            break

        # Convert BGR to RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect pose
        results = pose.process(rgb)

        if results.pose_landmarks:

            # Draw pose skeleton
            mp_draw.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

            landmarks = results.pose_landmarks.landmark

            # Required joints
            ls = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
            rs = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]

            lh = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
            rh = landmarks[mp_pose.PoseLandmark.RIGHT_HIP]

            lk = landmarks[mp_pose.PoseLandmark.LEFT_KNEE]
            rk = landmarks[mp_pose.PoseLandmark.RIGHT_KNEE]

            la = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE]
            ra = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE]

            # Calculate knee angles
            left_knee_angle = calculate_angle(
                (lh.x, lh.y),
                (lk.x, lk.y),
                (la.x, la.y)
            )

            right_knee_angle = calculate_angle(
                (rh.x, rh.y),
                (rk.x, rk.y),
                (ra.x, ra.y)
            )

            # Save data
            writer.writerow([
                frame_number,

                ls.x, ls.y,
                rs.x, rs.y,

                lh.x, lh.y,
                rh.x, rh.y,

                lk.x, lk.y,
                rk.x, rk.y,

                la.x, la.y,
                ra.x, ra.y,

                left_knee_angle,
                right_knee_angle
            ])

            frame_number += 1

        # Show video
        cv2.imshow("Pose Detection", frame)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


# Cleanup
cap.release()
cv2.destroyAllWindows()
csv_file.close()