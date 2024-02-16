# DS525 Data Warehouse and Business Intelligence

## 02-data-modeling-ii
<p>ในตอนนี้ เราจะพูดถึงการนำข้อมูล json files จาก Github เพื่อนำมาสร้างเป็น Cassandra ซึ่งเป็น NoSQL</p>

### ข้อมูล Table
<ul>
  <li>Actors table จัดเก็บข้อมูลผู้ใช้งาน</li>
  <li>Repositories table จัดเก็บข้อมูล Repos ที่มีอยู่ใน Github</li>
  <li>Events table จัดเก็บเหตุการณ์ต่างๆ ที่เกิดกับ Repo โดย Actor</li>
</ul>

### Instruction
<ol>
  <li>ใน Terminal ใช้คำสั่ง docker compose up เพื่อติดตั้ง Cassandra ใน Container</li>
  <li>เปลี่ยน Directory ไปที่ 02-data-modeling-ii โดยใช้คำสั่ง cd ./02-data-modeling-ii </li>
  <li>ติดตั้ง Cassandra Module สำหรับเชื่อมต่อระหว่าง Cassandra และ Python โดยใช้คำสั่ง pip install cassandra-driver</li>
  <li>สั่งอ่านไฟล์ etl.py โดยใช้คำสั่ง python etl.py</li>
</ol>

https://us02web.zoom.us/j/6168217916?pwd=bVZyL2R5SzBNaTNhZTZtYmpUUzdndz09#success
