import json
from pathlib import Path
from db import get_db

def load_json(path_str):
    p = Path(path_str)
    if not p.exists():
        return []
    with p.open(encoding="utf-8") as f:
        return json.load(f)

def main():
    db = get_db()

    internships = load_json("internships.json")
    apprenticeships = load_json("apprenticeships.json")

    if internships:
        db.internships.delete_many({})
        db.internships.insert_many(internships)

    if apprenticeships:
        db.apprenticeships.delete_many({})
        db.apprenticeships.insert_many(apprenticeships)

    print("✅ Seed complete.",
          f"internships: {db.internships.count_documents({})},",
          f"apprenticeships: {db.apprenticeships.count_documents({})}")

if __name__ == "__main__":
    main()
