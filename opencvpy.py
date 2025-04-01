import cv2
import mediapipe as mp

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Puntas de los dedos: pulgar, índice, medio, anular, meñique
finger_tips_ids = [4, 8, 12, 16, 20]

# Captura de video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Efecto espejo
    frame = cv2.flip(frame, 1)

    # Convertir a RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    fingers_up = 0
    porcentaje_abierto = 0

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark

            # Dedos (excepto pulgar)
            print(finger_tips_ids)
            for tip_id in finger_tips_ids[1:]:
                if landmarks[tip_id].y < landmarks[tip_id - 2].y:
                    fingers_up += 1

            # Pulgar
            if landmarks[finger_tips_ids[0]].x > landmarks[finger_tips_ids[0] - 1].x:
                fingers_up += 1

            # Calcular porcentaje
            porcentaje_abierto = int((fingers_up / 5) * 100)

    # Mostrar texto en pantalla
    cv2.putText(frame, f'Dedos abiertos: {fingers_up}', (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f'Mano abierta: {porcentaje_abierto}%', (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 255), 2)

    cv2.imshow('Contador de Dedos y Porcentaje', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
