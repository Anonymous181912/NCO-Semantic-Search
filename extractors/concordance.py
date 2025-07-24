import pdfplumber
import json

structured = []
current_div = current_subdiv = current_group = current_family = None

with pdfplumber.open("sources/occupation_table.pdf") as pdf:
    for page_num, page in enumerate(pdf.pages):
        try:
            table = page.extract_table()
            if not table:
                print(f"[Page {page_num}] No table found.")
                continue

            for row_num, row in enumerate(table):
                if not row or len(row) < 4:
                    print(f"[Page {page_num} Row {row_num}] Skipped incomplete row: {row}")
                    continue

                label, code, title, alt_code = [cell.strip() if cell else "" for cell in row]

                if label.startswith("NCO") or label in ["Header", "Table", "Metadata"]:
                    continue

                if label == "Division":
                    current_div = {
                        "division_code": code,
                        "division_title": title,
                        "sub_divisions": []
                    }
                    structured.append(current_div)

                elif "Sub" in label: 
                    if not current_div:
                        print(f"[Page {page_num}] Sub-Division found without Division.")
                        continue
                    current_subdiv = {
                        "sub_division_code": code,
                        "sub_division_title": title,
                        "groups": []
                    }
                    current_div["sub_divisions"].append(current_subdiv)

                elif label == "Group":
                    if not current_subdiv:
                        print(f"[Page {page_num}] Group found without Sub-Division.")
                        continue
                    current_group = {
                        "group_code": code,
                        "group_title": title,
                        "families": []
                    }
                    current_subdiv["groups"].append(current_group)

                elif label == "Family":
                    if not current_group:
                        print(f"[Page {page_num}] Family found without Group.")
                        continue
                    current_family = {
                        "family_code": code,
                        "family_title": title,
                        "occupations": []
                    }
                    current_group["families"].append(current_family)

                elif label == "":
                    if not current_family:
                        print(f"[Page {page_num}] Occupation found without Family.")
                        continue
                    occupation = {
                        "code": code,
                        "title": title,
                        "nco_2004_code": alt_code
                    }
                    current_family["occupations"].append(occupation)

                else:
                    print(f"[Page {page_num} Row {row_num}] Unknown label: {label}")

        except Exception as e:
            print(f"[Page {page_num}] Error: {e}")


with open("data/concordance.json", "w", encoding="utf-8") as f:
    json.dump(structured, f, indent=4, ensure_ascii=False)
