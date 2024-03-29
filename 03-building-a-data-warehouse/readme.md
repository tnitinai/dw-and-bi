# Building a Data Warehouse
ในบทนี้เราจะเรียนรู้เรื่องการนำข้อมูลจาก csv file ปรับแต่งเป็นข้อมูลในรูปแบบตารางที่ Google BigQuery รองรับ โดยใช้ภาษา python 

## ขั้นตอน
1. สร้าง Google Account เพื่อเปิดใช้งาน BigQuery จากนั้นสร้าง dataset ชื่อว่า GitHub โดยเลือกเป็น single region

>BigQuery เป็นบริการฐานข้อมูลคลาวด์ขนาดใหญ่ (cloud-based) ที่ให้บริการการวิเคราะห์ข้อมูลแบบ Real-time และ Batch Processing โดยใช้ SQL ในการสอบถามข้อมูล ซึ่งถูกพัฒนาโดย Google Cloud Platform บริการนี้ช่วยให้ผู้ใช้สามารถประมวลผลข้อมูลขนาดใหญ่ได้อย่างมีประสิทธิภาพ โดยไม่จำเป็นต้องกังวลเรื่องการจัดการโครงสร้างฐานข้อมูลหรือการทำ Scale ของระบบเอง นอกจากนี้ยังมีความสามารถในการแบ่งปันข้อมูลและการทำงานร่วมกับเครื่องมืออื่น ๆ ใน Google Cloud Platform อีกด้วย

2. สร้าง Service Account เพื่อให้ เครื่อง client ของเราติดต่อกับ BigQuery service ของ google ได้
3. ในหน้า Google Console ค้นหา Service ที่ชื่อว่า **IAM & Admin** เปิด left navigation เลือก Service Accounts เลือก CREATE SERVICE ACCOUNT ที่อยู่ตรง navigation bar
4. ระบุชื่อ โดยให้ระบุอย่างเฉพาะเจาะจงว่า account นี้ ใช้เพื่อทำอะไร (เพื่อจะได้รู้ในอนาคตว่า account ทำอะไรนั่นเอง) เช่น elt-to-bigquery
5. กำหนด role ให้กับ service account นี้ (ในบทนี้จะกำหนดให้เป็น owner) และ กด DONE
6. เมื่อสร้าง service account สำเร็จ ให้เลือก KEYS tab แล้วเลือก ADD KEY > Create new key > เลือก JSON format แล้วจึงกด OK
7. ระบบจะดาวน์โหลดไฟล์ไว้ให้ **เก็บรักษา file นี้ให้ดี ไม่เก็บใน GitHub โดยเด็ดขาด**

>Service Account เป็นบัญชีที่ใช้สำหรับการรับรองตัวตน (authentication) และการให้สิทธิ์ (authorization) ให้แอปพลิเคชันหรือบริการทำงานกับแหล่งข้อมูลหรือบริการอื่น ๆ ในระบบ Cloud โดยไม่ต้องใช้บัญชีผู้ใช้ในการยืนยันตัวตนในบริการ Google Cloud Platform (GCP) เช่น BigQuery, Cloud Storage, Compute Engine และ Google Cloud APIs อื่น ๆ Service Account จะถูกใช้เพื่อให้บริการนั้น ๆ สามารถเข้าถึงและใช้งานแหล่งข้อมูลหรือบริการได้อย่างปลอดภัยและมีความยืดหยุ่น

**Service Account มักจะมีไฟล์ JSON ที่เก็บข้อมูลการรับรองตัวตน (credentials) ซึ่งสามารถใช้ในการตั้งค่าและใช้งาน Service Account ในแอปพลิเคชันหรือระบบของคุณได้**

8. ใน CodeSpace ให้สร้าง folder ชื่อ credentials ไว้ที่ root และเพื่อป้องกันการ commit credentials ไปยัง GitHub ให้เปิด file ขื่อว่า .gitignore และระบุ credentials เพื่อบอก Git ว่า ไม่ track file เหล่านี้
9. ให้ cd ไปหา working directory โดยใช้คำสั่ง
   ```python
   cd 03-building-a-data-warehouse
   ```
10. ใช้คำสั่งเหล่านี้เพื่อสร้าง environment และ install packages ต่างๆ
```python
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```
11. ให้ระบุข้อมูลต่อไปนี้
  ```python
keyfile = "YOUR_KEYFILE_PATH"
    service_account_info = json.load(open(keyfile))
    credentials = service_account.Credentials.from_service_account_info(service_account_info)

    # โค้ดส่วนนี้จะเป็นการสร้าง Client เชื่อมต่อไปยังโปรเจค GCP ของเรา โดยใช้ Credentials ที่
    # สร้างจากโค้ดข้างต้น
    project_id = "YOUR_GCP_PROJECT"
```
12. สั่ง run file etl.py
   ```python
   python ety.py
   ```
13. กลับไปดู Google BigQuery จะพบว่า มีข้อมูลเพิ่มเข้ามาตามไฟล์ที่เรา run etl.py
