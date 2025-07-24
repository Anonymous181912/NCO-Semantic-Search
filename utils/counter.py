import json
import os


with open("mapped_occupations_new.json", "r") as f:
    data = json.load(f)

divisions_count = 0
sub_divisions_count = 0
groups_count = 0
families_count = 0
occupations_count = 0

for divisions in data:
    divisions_count += 1
    for sub_divisions in divisions.get("sub_divisions", []):
        sub_divisions_count += 1
        for groups in sub_divisions.get("groups", []):
            groups_count += 1
            for families in groups.get("families", []):
                families_count +=1
                for occupations in families.get("occupations", []):
                        occupations_count +=1

print(f"Divisions: {divisions_count}")
print(f"Sub Divisions: {sub_divisions_count}")
print(f"Gruops: {groups_count}")
print(f"Families: {families_count}")
print(f"Occupations: {occupations_count}")