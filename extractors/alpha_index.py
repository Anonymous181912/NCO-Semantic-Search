import pdfplumber
import json

mapping = []
all_tables = []


with pdfplumber.open("sources/alphabetical_index.pdf") as pdf:
    for page_num, page in enumerate(pdf.pages, 1):
        try:
            tables = page.extract_tables()
            if not tables or len(tables) < 2:
                print(f"Page {page_num}: Less than 2 tables found.")
                continue

            
            table1 = tables[0][1:] if len(tables[0]) > 1 else []
            table2 = tables[1][1:] if len(tables[1]) > 1 else []

            all_tables.extend([table1, table2])

        except Exception as e:
            print(f"Error processing page {page_num}: {e}")


previous_table = []

for table_index, table in enumerate(all_tables):
    if not table:
        continue

    first_row = table[0]
    if first_row and len(first_row) >= 2 and first_row[1] == '':
        if previous_table:
            
            previous_table[-1][0] = f"{previous_table[-1][0]} {first_row[0]}"
            table.pop(0)

    
    for row in table:
        if not row or len(row) < 3:
            print(f"Skipping invalid row: {row}")
            continue
        mapping.append({
            "occupation": row[0].strip() if row[0] else "",
            "2015_code": row[1].strip() if row[1] else "",
            "2004_code": row[2].strip() if row[2] else ""
        })

    previous_table = table 


print(f"Extracted {len(mapping)} occupations")

try:
    with open("data/alpha_index.json", "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=4, ensure_ascii=False)
    print("Data written successfully.")
except Exception as e:
    print(f"❌ Failed to write data: {e}")
