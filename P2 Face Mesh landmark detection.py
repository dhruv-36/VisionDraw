import cv2
import mediapipe as mp
import time

ptime = 0
cap = cv2.VideoCapture(0)

mpDraw = mp.solutions.drawing_utils
mpMesh = mp.solutions.face_mesh
facemesh = mpMesh.FaceMesh(max_num_faces=1)
drawSpecs = mpDraw.DrawingSpec(thickness=2,circle_radius=1)


# def __init__(self,
#              static_image_mode=False,
#              max_num_faces=1, #increase if multiple faces to detect
#              refine_landmarks=False,
#              min_detection_confidence=0.5,
#              min_tracking_confidence=0.5):

while True:
    suc, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = facemesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpMesh.FACEMESH_CONTOURS,
                                  drawSpecs,drawSpecs)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(img, str(int(fps)), (10, 60), cv2.FONT_HERSHEY_PLAIN, 3, (102, 123, 155), 3)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
