import cv2
import mediapipe as mp

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Iniciar la captura de video
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    # Convertir a RGB, ya que MediaPipe trabaja en este formato
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)
    
    # Si se detecta una mano
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Lista para almacenar el estado de cada dedo (1: extendido, 0: plegado)
            finger_states = []
            
            # Para los dedos índice, medio, anular y meñique:
            # Usamos los landmarks: 8, 12, 16, 20 para las puntas y 6, 10, 14, 18 para la articulación PIP.
            finger_tips = [8, 12, 16, 20]
            finger_pips = [6, 10, 14, 18]
            
            for tip, pip in zip(finger_tips, finger_pips):
                # En las coordenadas de la imagen, el eje Y aumenta hacia abajo.
                # Por ello, si la coordenada Y de la punta es menor que la del PIP, el dedo está extendido.
                if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
                    finger_states.append(1)
                else:
                    finger_states.append(0)
            
            # Contamos cuántos dedos están extendidos
            open_fingers = sum(finger_states)
            
            # Definición simple:
            # - Si todos los dedos están plegados (open_fingers == 0) => puño cerrado.
            # - Si tres o más están extendidos => mano abierta.
            if open_fingers == 0:
                estado = "Puño Cerrado"
            elif open_fingers >= 3:
                estado = "Mano Abierta"
            else:
                estado = "Parcial"
            
            cv2.putText(frame, estado, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("Deteccion de Apertura/Cierre", frame)
    
    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
