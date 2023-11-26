import pickle

class DictionaryEntry:
    def __init__(self, english_word, thai_translation, word_type):
        self.english_word = english_word
        self.thai_translation = thai_translation
        self.word_type = word_type

def load_data():
    try:
        with open('dictionary.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def save_data():
    with open('dictionary.pkl', 'wb') as f:
        pickle.dump(dictionary, f)

dictionary = load_data()

def translate_word_type(choice):
    word_types = {
        1: "คำนาม (Noun)",
        2: "คำวิเศษณ์ (Adjective)",
        3: "คำกริยา (Verb)",
        4: "คำกริยาช่วย (Auxiliary Verb)",
        5: "คำสรรพนาม (Pronoun)",
        6: "คำบุพบท (Adverb)",
        7: "คำสันธาน (Preposition)",
        8: "คำเชื่อม (Conjunction)",
        9: "คำบรรยาย (Exclamation)",
        10: "คำสั่ง (Interjection)"
    }
    return word_types.get(choice)

word_types = [
    "คำนาม (Noun)",
    "คำวิเศษณ์ (Adjective)",
    "คำกริยา (Verb)",
    "คำกริยาช่วย (Auxiliary Verb)",
    "คำสรรพนาม (Pronoun)",
    "คำบุพบท (Adverb)",
    "คำสันธาน (Preposition)",
    "คำเชื่อม (Conjunction)",
    "คำบรรยาย (Exclamation)",
    "คำสั่ง (Interjection)"
]

def display_dictionary():
    if not dictionary:
        print("คลังคำศัพท์ว่างเปล่า.")
        return

    sorted_dictionary = sorted(dictionary, key=lambda entry: entry.english_word.lower())

    print("\nคลังคำศัพท์:")
    for i, entry in enumerate(sorted_dictionary, 1):
        print(f"{i}. ภาษาอังกฤษ: {entry.english_word} - ภาษาไทย: {entry.thai_translation} ({entry.word_type})")

def create_entry():
    print("=== เพิ่มคำศัพท์ ===")
    english_word = input("Enter English word: ")
    thai_translation = input("Enter Thai translation: ")

    print("เลือกประเภทของคำ:")
    for i, word_type in enumerate(word_types, 1):
        print(f"{i}. {word_type}")

    while True:
        try:
            word_type_choice = int(input("เลือกเลขที่ต้องการ (1-{}) (Choose the number you want (1-{})): ".format(len(word_types), len(word_types))))
            if 1 <= word_type_choice <= len(word_types):
                break
            else:
                print("กรุณาเลือกเลขที่ต้องการให้ถูกต้อง (1-{}).".format(len(word_types)))
        except ValueError:
            print("กรุณากรอกเลขที่เป็นตัวเลขเท่านั้น.")

    word_type = translate_word_type(word_type_choice)

    new_entry = DictionaryEntry(english_word, thai_translation, word_type)
    dictionary.append(new_entry)

    print(f"\nเพิ่มคำศัพท์ '{english_word}' เรียบร้อยแล้ว!\n")
    save_data()

def update_entry():
    english_word = input("ป้อนคำศัพท์ภาษาอังกฤษที่ต้องการแก้ไข: ")
    entry = next((e for e in dictionary if e.english_word.lower() == english_word.lower()), None)

    if entry:
        print(f"ภาษาอังกฤษ: {entry.english_word}")
        new_thai_translation = input("ป้อนคำแปลภาษาไทยใหม่: ")

        print("ประเภทของคำทั้งหมด:")
        for i, word_type in enumerate(word_types, 1):
            print(f"{i}. {word_type}")

        while True:
            try:
                choice = int(input("เลือกเลขที่ต้องการ (1-{}): ".format(len(word_types))))
                if 1 <= choice <= len(word_types):
                    break
                else:
                    print("กรุณาเลือกเลขที่ต้องการให้ถูกต้อง (1-{}).".format(len(word_types)))
            except ValueError:
                print("กรุณากรอกเลขที่เป็นตัวเลขเท่านั้น.")

        selected_word_type = translate_word_type(choice)

        entry.thai_translation = new_thai_translation
        entry.word_type = selected_word_type

        print(f"แก้ไขคำศัพท์ '{english_word}' เรียบร้อย.")
        save_data()
    else:
        print(f"ไม่พบคำศัพท์ '{english_word}'.")

def read_entry():
    english_word = input("ป้อนคำศัพท์ภาษาอังกฤษเพื่อค้นหา: ")
    entry = next((e for e in dictionary if e.english_word.lower() == english_word.lower()), None)

    if entry:
        print(f"ภาษาอังกฤษ: {entry.english_word} - ภาษาไทย: {entry.thai_translation} ({entry.word_type})")
    else:
        print(f"ไม่พบคำศัพท์ '{english_word}'.")
        print(f"คำศัพท์ภาษาไทย: ไม่พบคำศัพท์")

def delete_entry():
    english_word = input("ป้อนคำศัพท์ภาษาอังกฤษที่ต้องการลบ: ")
    entry = next((e for e in dictionary if e.english_word.lower() == english_word.lower()), None)

    if entry:
        dictionary.remove(entry)
        print(f"ลบคำศัพท์ '{english_word}' เรียบร้อย.")
        save_data()
    else:
        print(f"ไม่พบคำศัพท์ '{english_word}'.")

def print_menu():
    print("\nDictionary English - Thai พจนานุกรม อังกฤษ - ไทย")
    print("เมนู:")
    print("1. ค้นหาคำศัพท์ (Read Entry)")
    print("2. เพิ่มคำศัพท์ (Create Entry)")
    print("3. แก้ไขคำศัพท์ (Update Entry)")
    print("4. ลบคำศัพท์ (Delete Entry)")
    print("5. คลังคำศัพท์ (Display Dictionary)")
    print("6. ออกจากโปรแกรม (Exit)")

while True:
    print_menu()
    choice = input("เลือกทำรายการ (1-6): ")

    if choice == '1':
        read_entry()
    elif choice == '2':
        create_entry()
    elif choice == '3':
        update_entry()
    elif choice == '4':
        delete_entry()
    elif choice == '5':
        display_dictionary()
    elif choice == '6':
        break
    else:
        print("ทางเลือกไม่ถูกต้อง กรุณากรอกตัวเลข 1-6 เท่านั้น.")