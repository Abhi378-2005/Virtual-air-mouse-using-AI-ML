import cv2
import pyautogui
import numpy as np
import time
from hand_detector import HandDetector

# --- TUNING PARAMETERS (Play with these!) ---
width_cam, height_cam = 640, 480
frame_reduction = 80    # Higher = Less arm movement needed (Higher Sensitivity)
smoothening = 10          # Higher = Smoother but slower (Try 5 to 10)
jitter_threshold = 5     # Higher = Ignores more shaking (Try 2 to 5)
# --------------------------------------------

pyautogui.FAILSAFE = False 

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, width_cam)
    cap.set(4, height_cam)

    detector = HandDetector(max_hands=1)
    screen_width, screen_height = pyautogui.size()
    
    # Variables for smoothing
    prev_x, prev_y = 0, 0
    curr_x, curr_y = 0, 0
    
    # Variables for clicking
    click_time = 0

    print(">>> Virtual Mouse Starting...")
    
    while True:
        success, frame = cap.read()
        if not success: break

        # 1. Detect Hand
        frame = detector.find_hands(frame)
        lm_list = detector.find_positions(frame)

        # Draw the "Active Zone" Box (Purple)
        # You must keep your hand inside this box to reach all corners of screen
        cv2.rectangle(frame, (frame_reduction, frame_reduction), 
                     (width_cam - frame_reduction, height_cam - frame_reduction), 
                     (255, 0, 255), 2)

        if len(lm_list) != 0:
            # Tip of Index Finger (Movement)
            x1, y1 = lm_list[8][1], lm_list[8][2]
            # Tip of Thumb (Clicking)
            x2, y2 = lm_list[4][1], lm_list[4][2]

            # 2. Map Coordinates (Camera -> Screen)
            x3 = np.interp(x1, (frame_reduction, width_cam - frame_reduction), (0, screen_width))
            y3 = np.interp(y1, (frame_reduction, height_cam - frame_reduction), (0, screen_height))

            # 3. Jitter Reduction (Dead Zone)
            # If we haven't moved much, keep the target same as previous (don't update)
            if abs(x3 - prev_x) < jitter_threshold and abs(y3 - prev_y) < jitter_threshold:
                x3 = prev_x
                y3 = prev_y

            # 4. Smoothing (Interpolation)
            curr_x = prev_x + (x3 - prev_x) / smoothening
            curr_y = prev_y + (y3 - prev_y) / smoothening

            # 5. Move Mouse
            # Flip 'x' because camera is mirrored
            final_x = screen_width - curr_x
            final_y = curr_y
            
            try:
                pyautogui.moveTo(final_x, final_y)
            except: pass

            prev_x, prev_y = curr_x, curr_y

            # 6. Click Logic (with cooldown to prevent double-clicks)
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if distance < 40:
                # Draw green circle to show "Click Ready"
                cv2.circle(frame, (x1, y1), 15, (0, 255, 0), cv2.FILLED)
                
                # Simple debouncing (wait 0.3s before next click)
                if time.time() - click_time > 0.3:
                    pyautogui.click()
                    click_time = time.time()

        # Show Frame
        cv2.imshow("Virtual Mouse", cv2.flip(frame, 1))
        if cv2.waitKey(1) == 27: # ESC
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()