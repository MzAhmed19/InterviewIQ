import cv2
import os

# Load video
video_path = 'testinterview1.mp4'
video = cv2.VideoCapture(video_path)

# Create directory for frames
if not os.path.exists('frames'):
    os.makedirs('frames')

frame_count = 0

while True:
    ret, frame = video.read()
    if not ret:
        break
    # Save every nth frame (to reduce data size if needed)
    if frame_count % 10 == 0:
        frame_filename = f'frames/frame_{frame_count}.jpg'
        cv2.imwrite(frame_filename, frame)
    frame_count += 1

video.release()
cv2.destroyAllWindows()

print("✅ Frames extracted.")