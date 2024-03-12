# Building a Data Warehouse
ในบทนี้เราจะเรียนรู้เรื่องการนำข้อมูลจาก csv file ปรับแต่งเป็นข้อมูลในรูปแบบตารางที่ Google BigQuery รองรับ โดยใช้ภาษา python 

## ขั้นตอน
1. สร้าง Google Account เพื่อเปิดใช้งาน BigQuery

>BigQuery เป็นบริการฐานข้อมูลคลาวด์ขนาดใหญ่ (cloud-based) ที่ให้บริการการวิเคราะห์ข้อมูลแบบ Real-time และ Batch Processing โดยใช้ SQL ในการสอบถามข้อมูล ซึ่งถูกพัฒนาโดย Google Cloud Platform บริการนี้ช่วยให้ผู้ใช้สามารถประมวลผลข้อมูลขนาดใหญ่ได้อย่างมีประสิทธิภาพ โดยไม่จำเป็นต้องกังวลเรื่องการจัดการโครงสร้างฐานข้อมูลหรือการทำ Scale ของระบบเอง นอกจากนี้ยังมีความสามารถในการแบ่งปันข้อมูลและการทำงานร่วมกับเครื่องมืออื่น ๆ ใน Google Cloud Platform อีกด้วย

2. สร้าง Service Account เพื่อให้ เครื่อง client ของเราติดต่อกับ BigQuery service ของ google ได้
  1. ในหน้า Google Console ค้นหา Service ที่ชื่อว่า **IAM & Admin** เปิด left navigation เลือก Service Accounts เลือก CREATE SERVICE ACCOUNT ที่อยู่ตรง navigation bar  
  2. ระบุชื่อ โดยให้ระบุอย่างเฉพาะเจาะจงว่า account นี้ ใช้เพื่อทำอะไร (เพื่อจะได้รู้ในอนาคตว่า account ทำอะไรนั่นเอง) เช่น elt-to-bigquery
  3. กำหนด role ให้กับ service account นี้ (ในบทนี้จะกำหนดให้เป็น owner)
  4 กด DONE
  5. เมื่อสร้าง service account สำเร็จ ให้เลือก KEYS tab แล้วเลือก ADD KEY > Create new key > เลือก JSON format แล้วจึงกด OK
  6. ระบบจะดาวน์โหลดไฟล์ไว้ให้ **เก็บรักษา file นี้ให้ดี ไม่เก็บใน GitHub โดยเด็ดขาด**

>Service Account เป็นบัญชีที่ใช้สำหรับการรับรองตัวตน (authentication) และการให้สิทธิ์ (authorization) ให้แอปพลิเคชันหรือบริการทำงานกับแหล่งข้อมูลหรือบริการอื่น ๆ ในระบบ Cloud โดยไม่ต้องใช้บัญชีผู้ใช้ในการยืนยันตัวตนในบริการ Google Cloud Platform (GCP) เช่น BigQuery, Cloud Storage, Compute Engine และ Google Cloud APIs อื่น ๆ Service Account จะถูกใช้เพื่อให้บริการนั้น ๆ สามารถเข้าถึงและใช้งานแหล่งข้อมูลหรือบริการได้อย่างปลอดภัยและมีความยืดหยุ่น

**Service Account มักจะมีไฟล์ JSON ที่เก็บข้อมูลการรับรองตัวตน (credentials) ซึ่งสามารถใช้ในการตั้งค่าและใช้งาน Service Account ในแอปพลิเคชันหรือระบบของคุณได้**

3. ใน CodeSpace ให้สร้าง folder ชื่อ credentials ไว้ที่ root และเพื่อป้องกันการ commit credentials ไปยัง GitHub ให้เปิด file ขื่อว่า .gitignore และระบุ 
