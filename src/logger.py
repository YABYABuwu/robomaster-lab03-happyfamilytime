class Logger:
    def __init__(self, ep_robot, base_data_dir="data/raw"):
        """
        จัดการสร้างโฟลเดอร์สำหรับ Run ปัจจุบัน และเตรียมไฟล์ CSV สำหรับบันทึกข้อมูล
        """
        self.base_data_dir = base_data_dir
        self.run_dir = self._create_run_directory()
        self.file_handles = {}
        self.csv_writers = {}
        self.chassis = ep_robot.chassis

    def _create_run_directory(self):
        """
        สร้างโฟลเดอร์สำหรับรอบการรันใหม่ (เช่น data/raw/run1, data/raw/run2)
        """
        if not os.path.exists(self.base_data_dir):
            os.makedirs(self.base_data_dir)
        
        # ค้นหาว่ามี run ล่าสุดถึงเลขอะไรแล้ว เพื่อสร้างโฟลเดอร์ถัดไป
        existing_runs = [d for d in os.listdir(self.base_data_dir) if d.startswith('run')]
        run_numbers = [int(d.replace('run', '')) for d in existing_runs if d.replace('run', '').isdigit()]
        
        next_run_num = max(run_numbers) + 1 if run_numbers else 1
        current_run_dir = os.path.join(self.base_data_dir, f"run{next_run_num}")
        
        os.makedirs(current_run_dir, exist_ok=True)
        return current_run_dir
    def sub_attitude_info_handler(self, sub_info):
    # print("sub info: {0}".format(sub_info))
    # print(type(sub_info))
        log_dir = self.run_dir + 'log_attitude.csv'
        if not os.path.exists(log_dir):
            with open(log_dir , mode='w', newline='') as file:
              writer = csv.writer(file)
              writer.writerow(['time unit' ,'yaw', 'pitch', 'roll'])
        with open(log_dir, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([int(time.time()), sub_info[0], sub_info[1], sub_info[2]])

    def sub_position_info_handler(self, sub_info):
        # print("sub info: {0}".format(sub_info))
        # print(type(sub_info))
        log_dir = self.run_dir + 'log_position.csv'
        if not os.path.exists(log_dir):
            with open(log_dir, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['time unit', 'x', 'y', 'z'])
        with open(log_dir, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([int(time.time()), sub_info[0], sub_info[1], sub_info[2]])

    def sub_imu_info_handler(self, sub_info):
        # print("sub info: {0}".format(sub_info))
        # print(type(sub_info))
        log_dir = self.run_dir + 'log_imu.csv'
        if not os.path.exists(log_dir):
            with open(log_dir, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['time unit', 'acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z'])
        with open(log_dir, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([int(time.time()), sub_info[0], sub_info[1], sub_info[2], sub_info[3], sub_info[4], sub_info[5]])

    def sub_esc_info_handler(self, sub_info):
        # print("sub info: {0}".format(sub_info))
        # print(type(sub_info))
        log_dir = self.run_dir + 'log_esc.csv'
        if not os.path.exists(log_dir):
            with open(log_dir, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['time unit', 'speed', 'angle', 'timestamp', 'stable'])
        with open(log_dir, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([int(time.time()), sub_info[0], sub_info[1], sub_info[2], sub_info[3]])

    def start_attitude_log(self, feq=5):
        self.chassis.sub_attitude(freq=feq, callback= self.sub_attitude_info_handler)

    def start_position_log(self, feq=5):
        self.chassis.sub_positin(freq=feq, callback= self.sub_position_info_handler)

    def start_imu_log(self, feq=5):
        self.chassis.sub_imu(freq=feq, callback= self.sub_imu_info_handler)

    def start_esc_log(self, feq=5):
        self.chassis.sub_esc(freq=feq, callback= self.sub_esc_info_handler)

    def start_all(self, feq_att=5, feq_pos=5, feq_imu=5, feq_esc=5):
        self.chassis.sub_attitude(freq=feq_att, callback= self.sub_attitude_info_handler)
        self.chassis.sub_positin(freq=feq_pos, callback= self.sub_position_info_handler)
        self.chassis.sub_imu(freq=feq_imu, callback= self.sub_imu_info_handler)
        self.chassis.sub_esc(freq=feq_esc, callback= self.sub_esc_info_handler)

    def stop_attitude_log(self):
        self.chassis.unsub_attitude()

    def stop_position_log(self):
        self.chassis.unsub_positin()

    def stop_imu_log(self):
        self.chassis.unsub_imu()

    def stop_esc_log(self):
        self.chassis.unsub_esc()

    def stop_all(self):
        self.chassis.unsub_attitude()
        self.chassis.unsub_positin()
        self.chassis.unsub_imu()
        self.chassis.unsub_esc()
        
