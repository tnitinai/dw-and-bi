# Creating and Scheduling Data Pipelines
ในขั้นตอนนี้จะเป็นการสร้าง Workflow Orchestration หรือเรียกง่ายๆ ว่าเป็นการทำกระบวนการต่างๆ เป็นขั้นตอน โดยใช้ Airflow

1. ไปที่ Directory 05-creating-and-scheduling-data
2. ติดตั้ง Packages ต่างๆ ตามไฟล์ docker-compose.yaml ด้วยคำสั่ง docker compose up
3. ไปที่หน้า Web Interface ของ Airflow (Port 8080) แล้ว login ด้วย username and password
4. ในขั้นตอนนี้ จะเป็นการสร้าง DAG (Directed Acyclic Graph) ซึ่งเป็นการกำหนดกระบวนการในการทำงานของไฟล์
5. กลับไปหน้า Web Interface จะพบว่ามี DAG ชื่อ etl เพิ่มเข้ามา (อาจใช้เวลาสักพักเพื่อให้ระบบอัพเดท)
6. เนื่องจากใน DAG เป็นการนำข้อมูลจากไฟล์ .csv (Github_events) เข้า Postgres Database จึงต้องมีการกำหนด Connection โดยไปที่ Admin > Connections กด + เพื่อเพิ่ม Connection ใหม่ เลือก Connection Type เป็น Postgres แล้วระบุข้อมูลต่างๆ
7. จากนั้นจึงกลับมาหน้า DAG แล้วสั่ง Run 
8. หากดำเนินการสำเร็จจะมีสีเขียวที่ step ต่างๆ

ถ้าใช้งานระบบที่เป็น Linux ให้เรารันคำสั่งด้านล่างนี้ก่อน

```sh
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

หลังจากนั้นให้รัน

```sh
docker-compose up
```

เราจะสามารถเข้าไปที่หน้า Airflow UI ได้ที่ port 8080

เสร็จแล้วให้คัดลอกโฟลเดอร์ `data` ที่เตรียมไว้ข้างนอกสุด เข้ามาใส่ในโฟลเดอร์ `dags` เพื่อที่ Airflow จะได้เห็นไฟล์ข้อมูลเหล่านี้ แล้วจึงค่อยทำโปรเจคต่อ

**หมายเหตุ:** จริง ๆ แล้วเราสามารถเอาโฟลเดอร์ `data` ไว้ที่ไหนก็ได้ที่ Airflow ที่เรารันเข้าถึงได้ แต่เพื่อความง่ายสำหรับโปรเจคนี้ เราจะนำเอาโฟลเดอร์ `data` ไว้ในโฟลเดอร์ `dags` เลย