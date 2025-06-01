import cv2
import numpy as np
import argparse

# Argumentos de linha de comando
parser = argparse.ArgumentParser(description="Contador de objetos por cor (vermelho e azul).")
parser.add_argument('--camera', type=str, default='0', help='ID da câmera ou URL RTSP')
parser.add_argument('--video', type=str, default=None, help='Caminho para o arquivo de vídeo MP4')
args = parser.parse_args()

# Define a fonte de vídeo
if args.video is not None:
    camera_source = args.video
else:
    camera_source = int(args.camera) if args.camera.isdigit() else args.camera

# Faixas de cor em HSV
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

line_y = 300
line_thickness = 4

red_count = 0
blue_count = 0

cap = cv2.VideoCapture(camera_source)
if not cap.isOpened():
    print("Erro ao abrir o vídeo/câmera:", camera_source)
    exit(1)

def get_centroid(x, y, w, h):
    return (int(x + w / 2), int(y + h / 2))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Fim do vídeo ou erro ao capturar frame.")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_red = cv2.bitwise_or(
        cv2.inRange(hsv, lower_red1, upper_red1),
        cv2.inRange(hsv, lower_red2, upper_red2)
    )
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    cv2.line(frame, (0, line_y), (frame.shape[1], line_y), (0, 255, 255), line_thickness)

    def count_objects(mask, color):
        global red_count, blue_count
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 600:
                x, y, w, h = cv2.boundingRect(cnt)
                cx, cy = get_centroid(x, y, w, h)
                if color == "red":
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                    cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
                    if (line_y - 5) < cy < (line_y + 5):
                        red_count += 1
                elif color == "blue":
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    cv2.circle(frame, (cx, cy), 4, (255, 0, 0), -1)
                    if (line_y - 5) < cy < (line_y + 5):
                        blue_count += 1

    count_objects(mask_red, "red")
    count_objects(mask_blue, "blue")

    cv2.putText(frame, f"Vermelhos: {red_count}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, f"Azuis: {blue_count}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Contador de Objetos", frame)

    if cv2.waitKey(30 if args.video else 1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
