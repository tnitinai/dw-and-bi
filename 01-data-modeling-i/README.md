# DS525 Data Warehouse and Business Intelligence

## 01-data-modeling-1
<p>ในตอนนี้ เราจะพูดถึงการนำข้อมูล json files จาก Github เพื่อนำมาสร้างเป็น Postgres SQL</p>

### Schema Information
<table>
  <thead>
    <th>Table Name</th>
    <th>Description</th>
  </thead>
  <tbody>
    <tr>
      <td>repos</td>
      <td>เก็บข้อมูล repository จากตัวอย่าง</td>
    </tr>
    <tr>
      <td>events</td>
      <td>เก็บข้อมูลเหตุการณ์ต่างๆที่เกิดขึ้นกับ repos (repo_id) จาก actors (actor_id)</td>
    </tr>
    <tr>
      <td>actors</td>
      <td>เก็บข้อมูล users ที่ใช้งานใน Github</td>
    </tr>
    <tr>
      <td>comments</td>
      <td>ข้อมูล comments ที่เกิดใน repos (repo_id) จาก users (actor_id) พร้อมทั้งเก็บข้อมูล reactions ของ comments</td>
    </tr>
    <tr>
      <td>commits</td>
      <td>ข้อมูลการ commits ที่เกิดใน repos (repo_id) และแสดงจำนวน commits ในแต่ละครั้ง</td>
    </tr>
    <tr>
      <td>pull_requests</td>
      <td>ข้อมูลการ pull request ของ repos (repo_id) จาก users (actor_id)</td>
    </tr>
    <tr>
      <td>pull_request_reviews</td>
      <td>ข้อมูลการ review pull request ของแต่ละ pull requests</td>
    </tr>
  </tbody>
</table>

### heading 3
