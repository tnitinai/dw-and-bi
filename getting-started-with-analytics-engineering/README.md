# 06 Analytics Engineering

ในบทนี้ เราจะใช้ dbt ในการทำ data warehouse โดยใช้ข้อมูลจาก greenery store


## 1. ติดตั้ง packages ต่างๆ ของ Docker ในขั้นตอนนี้ จะมีการ dump data ของ greenery ใน Postgresql ซึ่ง run ใน port:5432 และมีหน้า Database manager ชื่อ sqlpad ใน port:3000

```sh
docker compose up
```

## 2. ติดตั้ง packages/ applications ที่กำหนดใน requirements file

```bash
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

## 3. เปิด Terminal ใหม่ แล้ว cd ไปหา ชื่อโปรเจค จากนั้นใช้คำสั่ง dbt init เพื่อเริ่มการใข้งาน dbt (ใส่ชื่อ project ว่า greenery) และระบุข้อมูลที่ dbt ต้องการ (ข้อมูล database connection)

```bash
dbt init
```

## 3. ย้ายหรือคัดลอกไฟล์ profiles.yml ซึ่งเป็นไฟล์ที่ระบุค่า configuration สำหรับการติดต่อกับ database โดยใช้คำสั่ง

    ```bash
    cp ../yaml_files/profiles.yml .
    ```
## 4. เปิดไฟล์ profiles.yml และแก้ไข schema ให้เป็นชื่ออื่นๆ (แนะนำ dbt_<any_name>)

    ```yaml
    greenery:

      outputs:
        dbt_greenery:
          type: postgres
          threads: 1
          host: localhost
          port: 5432
          user: postgres
          pass: "{{ env_var('DBT_ENV_SECRET_PG_PASSWORD') }}"
          dbname: greenery
          schema: dbt_greenery

        prod:
          type: postgres
          threads: 1
          host: localhost
          port: 5432
          user: postgres
          pass: "{{ env_var('DBT_ENV_SECRET_PG_PASSWORD') }}"
          dbname: greenery
          schema: prod

      target: dbt_greenery
    ```

## 5. ไปที่ folder greenery > models สร้าง folder ว่า staging และ marts

## 6. ในขั้นตอนนี้จะทำตัวอย่างเพียง 1 ไฟล์ โดยการสร้าง file ชื่อ mrt__greenery_order_details.sql และระบุข้อมูลดังนี้
  ```sql
    select 
    o.order_id,
    p.name as product_name,
    p.price as unit_price,
    o.quantity
    
    from {{ source('greenery', 'products') }} as p
    right join {{ source('greenery', 'order_items') }} as o

    on p.product_id = o.product_id
  ```

## 7. ใช้คำสั่ง dbt debug เพื่อทดสอบ
  ```bash
    dbt debug
  ```

## 8. หากไม่มีข้อผิดพลาด ให้ใช้คำสั่ง  dbt run และดูผลลัพธ์ได้ที่ sqlpad
  ```bash
    dbt run
  ```