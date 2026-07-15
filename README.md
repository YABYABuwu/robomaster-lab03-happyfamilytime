# RoboMaster Lab 03 - Happy Family Time

โปรเจกต์สำหรับการทำ Lab 03 ของวิชา RoboMaster

## สมาชิกในกลุ่ม
1. [ชื่อ-นามสกุล] - [รหัสนักศึกษา]
2. [ชื่อ-นามสกุล] - [รหัสนักศึกษา]
3. [ชื่อ-นามสกุล] - [รหัสนักศึกษา]

## โครงสร้างโปรเจกต์ (Project Structure)
```
robomaster-lab3-happyfamilytime/
├── .gitignore                  # ระบุไฟล์ที่ไม่ต้องการอัปโหลดขึ้น Git (.venv, data/*.csv)
├── requirements.txt            # Third-party Libraries (robomaster, pyyaml, pandas, matplotlib)
├── README.md                   # เอกสารสมาชิกในกลุ่มและข้อมูลโปรเจกต์
├── main.py                     # Entry point หลักในการเชื่อมต่อและสั่งรันหุ่นยนต์
│
├── config/
│   └── settings.yaml           # เก็บพารามิเตอร์การตั้งค่า เช่น ความเร็ว และ IP connection
│
├── src/                        # ส่วนควบคุม Hardware และฟังก์ชันการทำงานหลัก
│   ├── __init__.py
│   ├── config_loader.py        # โหลดไฟล์การตั้งค่า yaml
│   ├── chassis.py              # ควบคุมการเคลื่อนที่ของล้อ Mecanum
│   ├── gimbal.py               # ควบคุมป้อมปืนและทิศทางกล้อง
│   ├── vision.py               # จัดการกล้องและ OpenCV
│   └── logger.py               # บันทึกข้อมูล Sensor ลงในไฟล์ CSV
│
├── data/
│   ├── raw/                    # โฟลเดอร์เก็บข้อมูลดิบ (เช่น log IMU)
│   └── processed/              # โฟลเดอร์เก็บข้อมูลที่ผ่านการประมวลผลแล้ว
│
└── analysis/
    ├── analyze_logs.ipynb      # โน้ตบุ๊กวิเคราะห์ผลการวิ่งและประมวลผลข้อมูล
    └── plots/                  # เก็บรูปกราฟผลลัพธ์ที่สร้างขึ้น
```

## วิธีการใช้งานเบื้องต้น (Getting Started)
1. **สร้าง Virtual Environment และติดตั้ง Dependencies:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # สำหรับ Windows
   pip install -r requirements.txt
   ```
2. **ปรับแต่งพารามิเตอร์คงที่:**
   แก้ไขไฟล์ `config/settings.yaml` เช่น ปรับความเร็ว ความเร็วป้อมปืน หรือทิศทางการบันทึกข้อมูล
3. **รันสคริปต์หลัก:**
   ```bash
   python main.py
   ```
