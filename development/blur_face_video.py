import cv2
import dlib

# Set the input and output file paths
input_file = "input.mp4"
output_file = "output.mp4"

# Load the input video
video_capture = cv2.VideoCapture(input_file)

# Set the video codec and create the output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(output_file, fourcc, 30, (int(video_capture.get(3)), int(video_capture.get(4))))

# Load the face detector
face_detector = dlib.get_frontal_face_detector()

# Loop over each frame in the video
while video_capture.isOpened():
    # Read the next frame from the video
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert the frame to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_detector(frame_gray, 0)

    # Loop over each face
    for face in faces:
        # Get the face coordinates
        x1, y1, x2, y2, w, h = face.left(), face.top(), face.right() + 1, face.bottom() + 1, face.width(), face.height()

        # Extract the face from the frame
        face_frame = frame[y1:y2, x1:x2]

        # Resize the face to a fixed size
        face_frame = cv2.resize(face_frame, (w // 10, h // 10), interpolation=cv2.INTER_NEAREST)

        # Resize the face back to its original size
        face_frame = cv2.resize(face_frame, (w, h), interpolation=cv2.INTER_NEAREST)

        # Blur the face
        face_frame = cv2.GaussianBlur(face_frame, (23, 23), 30)

        # Replace the original face with the blurred face
        frame[y1:y2, x1:x2] = face_frame

    # Write the frame to the output video
    video_writer.write(frame)

# Release the video capture and video writer objects
video_capture.release()
video_writer.release()
