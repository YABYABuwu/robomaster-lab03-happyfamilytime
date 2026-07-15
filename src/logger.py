import os
import csv
import datetime

class SensorLogger:
    """
    คลาสจัดการเขียนค่าจากเซนเซอร์ลงไฟล์ CSV แบบเรียลไทม์
    """
    def __init__(self, output_dir="data/raw/run1", file_prefix="log_imu"):
        self.output_dir = output_dir
        self.file_prefix = file_prefix
        self.file_path = None
        self.csv_file = None
        self.writer = None
        
        # ตรวจสอบและสร้างโฟลเดอร์สำหรับเก็บข้อมูลดิบ
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)

    def start_logging(self, headers):
        """
        สร้างไฟล์ CSV ใหม่และเขียนหัวตาราง (Headers)
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.file_path = os.path.join(self.output_dir, f"{self.file_prefix}_{timestamp}.csv")
        
        print(f"[Logger] Creating log file: {self.file_path}")
        self.csv_file = open(self.file_path, mode='w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.csv_file)
        self.writer.writerow(headers) # เขียนหัวข้อคอลัมน์

    def log_row(self, row_data):
        """
        บันทึกข้อมูล 1 แถวลงไฟล์ CSV
        """
        if self.writer:
            self.writer.writerow(row_data)
            self.csv_file.flush() # บังคับให้เขียนลงดิสก์ทันที ป้องกันข้อมูลสูญหายเมื่อหยุดกระทันหัน

    def stop_logging(self):
        """
        ปิดการทำงานของ Logger และบันทึกไฟล์ให้สมบูรณ์
        """
        if self.csv_file:
            self.csv_file.close()
            print(f"[Logger] Log saved successfully: {self.file_path}")
            self.csv_file = None
            self.writer = None
