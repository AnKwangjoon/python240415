import re

def check_email(email):
    # 이메일 주소 유효성을 검사하는 정규표현식
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # 주어진 이메일 주소가 유효한지 검사
    if re.match(pattern, email):
        return True
    else:
        return False

# 테스트
emails = ["john@example.com", "invalid_email", "alice@company.co.uk", "bob@gmail"]
for email in emails:
    if check_email(email):
        print(f"{email}은(는) 유효한 이메일 주소입니다.")
    else:
        print(f"{email}은(는) 유효하지 않은 이메일 주소입니다.")

# 테스트
emails = ["john@example.com", "invalid_email", "alice@company.co.uk", "bob@gmail",
          "user123@yahoo.com", "invalid@address", "test.email@example.com", "example@domain", 
          "email@server.com", "12345@example.com"]
for email in emails:
    if check_email(email):
        print(f"{email}은(는) 유효한 이메일 주소입니다.")
    else:
        print(f"{email}은(는) 유효하지 않은 이메일 주소입니다.")