import cv2
import mediapipe as mp
import pyautogui

# Inicializar MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Tamaño de pantalla
screen_width, screen_height = pyautogui.size()

# Captura de video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Invertir imagen como espejo
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    frame_height, frame_width, _ = frame.shape

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Dibujar puntos
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Índice (landmark 8)
            index_finger_tip = hand_landmarks.landmark[8]

            # Coordenadas del dedo índice en píxeles
            x = int(index_finger_tip.x * frame_width)
            y = int(index_finger_tip.y * frame_height)

            # Mostrar punto en pantalla
            cv2.circle(frame, (x, y), 10, (255, 0, 255), cv2.FILLED)

            # Convertir coordenadas de cámara a pantalla
            screen_x = int(index_finger_tip.x * screen_width)
            screen_y = int(index_finger_tip.y * screen_height)

            # Mover el mouse
            pyautogui.moveTo(screen_x, screen_y)

    cv2.imshow("Control de Mouse con la Mano", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
