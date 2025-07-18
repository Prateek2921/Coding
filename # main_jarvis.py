# main_jarvis.py

from camera_module import detect_faces  # You build this
from brain import jarvis_response       # You build this

while True:
    command = input("You: ")

    if command == "camera":
        detect_faces()
    else:
        print("Jarvis:", jarvis_response(command))
