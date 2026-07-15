class ChassisController:
    """
    คลาสสำหรับควบคุมล้อ Mecanum (เดินหน้า, ถอยหลัง, สไลด์ข้าง)
    """
    def __init__(self, ep_robot):
        self.chassis = ep_robot.chassis

    def move_forward(self, distance, speed):
        """
        เดินหน้าตามระยะทาง (เมตร) และความเร็วที่กำหนด
        """
        print(f"[Chassis] Moving forward: distance={distance}m, speed={speed}m/s")
        self.chassis.move(x=distance, y=0, z=0, v=speed).wait_for_completed()

    def move_backward(self, distance, speed):
        """
        ถอยหลังตามระยะทาง (เมตร) และความเร็วที่กำหนด
        """
        print(f"[Chassis] Moving backward: distance={distance}m, speed={speed}m/s")
        self.chassis.move(x=-distance, y=0, z=0, v=speed).wait_for_completed()

    def slide_left(self, distance, speed):
        """
        สไลด์ซ้ายตามระยะทาง (เมตร) และความเร็วที่กำหนด
        """
        print(f"[Chassis] Sliding left: distance={distance}m, speed={speed}m/s")
        self.chassis.move(x=0, y=-distance, z=0, v=speed).wait_for_completed()

    def slide_right(self, distance, speed):
        """
        สไลด์ขวาตามระยะทาง (เมตร) และความเร็วที่กำหนด
        """
        print(f"[Chassis] Sliding right: distance={distance}m, speed={speed}m/s")
        self.chassis.move(x=0, y=distance, z=0, v=speed).wait_for_completed()

    def rotate_left(self, angle, speed):
        """
        หมุนตัวไปทางซ้ายตามมุมที่กำหนด (องศา)
        """
        print(f"[Chassis] Rotating left: angle={angle}deg")
        self.chassis.move(x=0, y=0, z=angle, v=speed).wait_for_completed()

    def rotate_right(self, angle, speed):
        """
        หมุนตัวไปทางขวาตามมุมที่กำหนด (องศา)
        """
        print(f"[Chassis] Rotating right: angle={-angle}deg")
        self.chassis.move(x=0, y=0, z=-angle, v=speed).wait_for_completed()
