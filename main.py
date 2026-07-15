from src.chassis import ChassisController as Chassis
import time
import robomaster
from robomaster import robot
import csv
import os



def main():

    print("[Main] Connecting to RoboMaster via Wi-Fi Direct...")
    ep_robot = robot.Robot()
    
    try :
        ep_robot.initialize(conn_type = "ap")
        print("[Main] Connected! SN:", ep_robot.get_sn())

        chassis = Chassis(ep_robot)

        v = 0.7
        degree = 91
        
        chassis.move_forward(0.6, v)
        time.sleep(2)
        chassis.move_turnRight(degree, 1)
        time.sleep(1)

        chassis.move_forward(0.6, v)
        time.sleep(2)
        chassis.move_turnRight(degree, 1)
        time.sleep(1)

        chassis.move_forward(0.6, v)
        time.sleep(2)
        chassis.move_turnRight(degree, 1)
        time.sleep(1)

        chassis.move_forward(0.6, v)
        time.sleep(2)
        chassis.move_turnRight(degree, 1)

        ep_robot.close()

    except KeyboardInterrupt:
        print("\n[Main] Program stopped by user.")
    
    except Exception as e:
        print(f"[Main] Error occurred: {e}")

    finally:
        # 3. บล็อกนี้จะทำงานเสมอเมื่อออกจากบล็อก try เพื่อคืน Resource ให้หุ่นยนต์
        print("[Main] Releasing robot resources...")
        
        try:
            ep_robot.camera.stop_video_stream() # ปิดกล้องถ้ามีการเปิดใช้
        
        except:
            pass
        
        ep_robot.uninitialize()
        print("[Main] Disconnected cleanly.")


if __name__ == "__main__":
    main()








