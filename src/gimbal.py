class GimbalController:
    """
    คลาสสำหรับควบคุมป้อมปืน (Gimbal) และมุมกล้องก้มเงย
    """
    def __init__(self, ep_robot):
        self.gimbal = ep_robot.gimbal

    def rotate_to(self, pitch=0, yaw=0, pitch_speed=50, yaw_speed=50):
        """
        หมุน Gimbal ไปยังมุมที่กำหนดในลักษณะ absolute (เทียบกับกึ่งกลางตัวหุ่น)
        """
        print(f"[Gimbal] Rotating to: pitch={pitch}deg, yaw={yaw}deg")
        self.gimbal.moveto(pitch=pitch, yaw=yaw, pitch_speed=pitch_speed, yaw_speed=yaw_speed).wait_for_completed()

    def rotate_by(self, pitch=0, yaw=0, pitch_speed=50, yaw_speed=50):
        """
        หมุน Gimbal เพิ่มขึ้น/ลดลงจากมุมเดิม (relative)
        """
        print(f"[Gimbal] Rotating by: pitch={pitch}deg, yaw={yaw}deg")
        # หมุนแกนระนาบและแกนตั้งตามค่าความต่าง
        # หมายเหตุ: ใน SDK ของ RoboMaster gimbal.move ใช้ควบคุมความเร็ว ส่วนการกำหนดมุมแบบ relative ใช้ moveto ร่วมกับ offset หรือเรียกทีละแกน
        # วิธีการหนึ่งคือใช้ moveto โหมด relative ถ้ามี หรือคำนวณตำแหน่งใหม่
        pass

    def center(self):
        """
        คืนค่าหัวของหุ่นยนต์มาที่ตรงกลาง
        """
        print("[Gimbal] Centering...")
        self.gimbal.recenter().wait_for_completed()
