import cv2

class VisionSystem:
    """
    คลาสสำหรับจัดการสตรีมภาพและประมวลผลวิดีโอจากกล้องหุ่นยนต์ (OpenCV)
    """
    def __init__(self, ep_robot):
        self.camera = ep_robot.camera

    def start_stream(self):
        """
        เริ่มการส่งสัญญาณภาพวิดีโอจากหุ่นยนต์
        """
        print("[Vision] Starting video stream...")
        self.camera.start_video_stream(display=False)

    def stop_stream(self):
        """
        หยุดการส่งสัญญาณภาพวิดีโอ
        """
        print("[Vision] Stopping video stream...")
        self.camera.stop_video_stream()

    def get_latest_frame(self):
        """
        ดึงเฟรมรูปภาพล่าสุดเพื่อนำมาประมวลผลต่อด้วย OpenCV
        """
        # ดึงภาพล่าสุด
        # img = self.camera.read_cv2_image(strategy="newest")
        # return img
        pass

    def show_video_feed(self, process_callback=None):
        """
        แสดงหน้าต่างวิดีโอสตรีมสด และสามารถเรียก callback ฟังก์ชันสำหรับตรวจจับวัตถุได้
        """
        print("[Vision] Opening video window (Press 'q' to quit)...")
        self.start_stream()
        try:
            while True:
                img = self.camera.read_cv2_image(strategy="newest")
                
                # หากมีฟังก์ชัน callback สำหรับประมวลผล เช่น การตรวจจับเส้น หรือสี
                if process_callback is not None and img is not None:
                    img = process_callback(img)
                
                if img is not None:
                    cv2.imshow("RoboMaster Video Feed", img)
                
                # กด 'q' เพื่อออกจากลูป
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            cv2.destroyAllWindows()
            self.stop_stream()
