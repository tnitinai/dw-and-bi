# 04 Building a Data Lake

สำหรับโปรเจคในครั้งนี้ จะเป็นการใช้ PySpark ใน Jupyter Notebook ที้รันผ่าน CodeSpace อีกที ซึ่งมีเป้าหมายเพื่อการนำ github_events file จำนวน 5 files แล้วผ่านกระบวนการ ETL เพื่ออัพโหลดไฟล์กลับไปที่ Google Cloud Storage
ขั้นตอนโดยสรุป
<ol>
  <li>เปิด Codespace</li>
  <li>ใช้คำสั่ง docker compose up เพื่อติดตั้ง pyspark-notebook</li>
  <li>เปิด Browser Pyspark</li>
  <li>สร้าง Service Account ใน Google Cloud Storage</li>
  <li>รัน etl_local_with_gStorage.ipynb</li> 
</ol>
```sh
sudo chmod 777 .
```

แล้วค่อยรัน

```sh
docker-compose up
```
