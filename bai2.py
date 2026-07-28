students = [
    {
        "id": "SV01",
        "name": " Nguyen Van An ",
        "email": " an.nguyen@rikkei.edu.vn ",
        "phone": " 0987654321 ",
    },
    {
        "id": "SV02",
        "name": " Tran Thi Bich ",
        "email": " bich_gmail.com ",
        "phone": " 0912345678 ",
    },
    {
        "id": "SV03",
        "name": " Le Hoang Cuong ",
        "email": " cuong@gmail.com ",
        "phone": " 09876abcde ",
    },
    {
        "id": "SV04",
        "name": " Pham Minh Dung ",
        "email": " dung@gmail.com ",
        "phone": " 0355667788 ",
    },
]


def validate_email(email, phone):
    clean_email = email.strip()
    clean_phone = phone.strip()

    is_email = (
        ("@" in clean_email)
        and (clean_email.count("@") == 1)
        and clean_email.endswith((".com", ".edu.vn"))
    )

    is_phone = (
        len(clean_phone) == 10 and clean_phone.startswith("0") and clean_phone.isdigit()
    )

    return clean_email, is_email, clean_phone, is_phone


for student in students:
    name = student["name"].strip()

    email, is_email, phone, is_phone = validate_email(
        student["email"], student["phone"]
    )

    if is_email and is_phone:
        print(
            f"[{student['id']}] {name} | Email: {email} | SDT: {phone} -> HO SO HOP LE"
        )
    elif not is_email:
        print(
            f"[{student['id']}] {name} | Email: {email} | SDT: {phone} -> KHONG HOP LE (Thieu @)"
        )
    elif not is_phone:
        print(
            f"[{student['id']}] {name} | Email: {email} | SDT: {phone} -> KHONG HOP LE (SDT chua chu)"
        )
