import os
import yaml

def load_settings(config_path="config/settings.yaml"):
    """
    โหลดการตั้งค่าจากไฟล์ settings.yaml และแปลงเป็น Dictionary
    """
    # คำนวณหา absolute path จากตำแหน่งของไฟล์นี้ ไปหาโฟลเดอร์ root ของโปรเจกต์
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, config_path)
    
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Config file not found at {full_path}")
        
    with open(full_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
        
    return config
