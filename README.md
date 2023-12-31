# Assignment-4-Project-English-Thai-Dictionary
## โปรแกรมนี้เป็น "พจนานุกรม อังกฤษ - ไทย" ที่อนุญาตให้ผู้ใช้ดำเนินการกับคำศัพท์ภาษาอังกฤษและไทย โดยมีฟังก์ชันหลักๆ ดังนี้:

1. **การเก็บข้อมูลด้วยคลาส `DictionaryEntry`:**
   - คลาสนี้ใช้สำหรับเก็บข้อมูลของแต่ละคำศัพท์ที่ประกอบไปด้วย ภาษาอังกฤษ (`english_word`)、ภาษาไทย (`thai_translation`) และประเภทของคำ (`word_type`) ที่ผู้ใช้เลือก.

2. **การโหลดและบันทึกข้อมูลด้วยฟังก์ชัน `load_data` และ `save_data`:**
   - `load_data`: ใช้เพื่อโหลดข้อมูลจากไฟล์ 'dictionary.pkl' โดยใช้ `pickle`. หากไม่พบไฟล์, ฟังก์ชันจะส่งค่าเป็นรายการว่าง.
   - `save_data`: ใช้เพื่อบันทึกข้อมูลลงในไฟล์ 'dictionary.pkl' โดยใช้ `pickle`.

3. **การแปลงประเภทของคำด้วยฟังก์ชัน `translate_word_type`:**
   - ฟังก์ชันนี้ใช้เพื่อแปลงเลขที่ผู้ใช้เลือกในการเลือกประเภทของคำเป็นข้อความประเภทคำที่เซ็ตไว้ล่วงหน้า.

4. **การแสดงข้อมูลด้วยฟังก์ชัน `display_dictionary`:**
   - แสดงรายการคำศัพท์ทั้งหมดที่อยู่ในพจนานุกรม จัดเรียงตามตัวอักษรของภาษาอังกฤษ.

5. **การเพิ่มข้อมูลด้วยฟังก์ชัน `create_entry`:**
   - ให้ผู้ใช้ป้อนข้อมูลใหม่เพื่อเพิ่มคำศัพท์ในพจนานุกรม.

6. **การแก้ไขข้อมูลด้วยฟังก์ชัน `update_entry`:**
   - ให้ผู้ใช้ป้อนคำศัพท์ที่ต้องการแก้ไข และเปลี่ยนแปลงข้อมูลเดิม.

7. **การค้นหาข้อมูลด้วยฟังก์ชัน `read_entry`:**
   - ให้ผู้ใช้ป้อนคำศัพท์ที่ต้องการค้นหา และแสดงข้อมูลหากพบ.

8. **การลบข้อมูลด้วยฟังก์ชัน `delete_entry`:**
   - ให้ผู้ใช้ป้อนคำศัพท์ที่ต้องการลบ และลบข้อมูลนั้นออกจากพจนานุกรม.

9. **การแสดงเมนูด้วยฟังก์ชัน `print_menu`:**
   - แสดงเมนูทางเลือกสำหรับผู้ใช้.

10. **การวนลูปหลักด้วย `while True`:**
    - ให้ผู้ใช้ทำรายการต่างๆ จนกว่าจะเลือกทำรายการที่มีค่าเป็น '6' เพื่อออกจากโปรแกรม.

11. **การใช้ `enumerate` และ `lambda` ในการจัดเรียงข้อมูล:**
    - ในฟังก์ชัน `display_dictionary`, ใช้ `enumerate` เพื่อระบุลำดับของคำศัพท์และ `lambda` เพื่อให้การจัดเรียงเป็นตามตัวอักษรของภาษาอังกฤษ.

โดยทั้งหมดนี้เขียนขึ้นมาเพื่อให้ผู้ใช้สามารถจัดการคำศัพท์ภาษาอังกฤษและไทยได้ง่ายและสะดวก เพื่อสร้างและบรรยายความหมายของคำศัพท์ต่างๆ ที่สนใจ.
