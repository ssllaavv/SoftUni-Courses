import re

html_code = input()

title_raw_pattern = r'<title>(.*)(?=</title>)'
body_raw_pattern = r'<body>(.*)(?=</body>)'
pattern_to_remove = r'(<[^>]*>)|(\\n)'

title_raw = re.findall(title_raw_pattern, html_code)
body_raw = re.findall(body_raw_pattern, html_code)

title = re.sub(pattern_to_remove, "", title_raw[0])
body = re.sub(pattern_to_remove, "", body_raw[0])

print(f"Title: {title}")
print(f"Content: {body}")