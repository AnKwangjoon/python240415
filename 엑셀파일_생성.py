import openpyxl

# 크롤링한 결과 데이터 예시 (임의의 데이터)
crawl_result = [
    {"title": "Article 1", "author": "Author A", "date": "2024-04-18"},
    {"title": "Article 2", "author": "Author B", "date": "2024-04-17"},
    {"title": "Article 3", "author": "Author C", "date": "2024-04-16"}
]

# 엑셀 파일 경로
excel_file_path = "c:\\work\\result.xlsx"

# 새 워크북 생성
workbook = openpyxl.Workbook()

# 활성 시트 선택
sheet = workbook.active
sheet.title = "Crawling Result"

# 헤더 추가
headers = ["Title", "Author", "Date"]
sheet.append(headers)

# 크롤링 결과를 엑셀에 추가
for item in crawl_result:
    row = [item["title"], item["author"], item["date"]]
    sheet.append(row)

# 엑셀 파일 저장
workbook.save(excel_file_path)
print(f"크롤링 결과가 {excel_file_path}에 저장되었습니다.")
