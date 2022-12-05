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

# Load the replacement picture
replacement_pic = cv2.imread("replacement.png")

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

        # Resize the replacement picture to match the face size
        replacement_pic_resized = cv2.resize(replacement_pic, (w, h))

        # Replace the face in the frame with the replacement picture
        frame[y1:y2, x1:x2] = replacement_pic_resized

    # Write the frame to the output video
    video_writer.write(frame)

# Release the video capture and video writer objects
video_capture.release()
video_writer.release()
