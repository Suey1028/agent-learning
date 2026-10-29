from pathlib import Path
import json
def save_user(user_id:int,data:dict):
    output_dir=Path("output")
    output_dir.mkdir(exist_ok=True)
    file_path=output_dir/f"user_{user_id}.json"
    with open(file_path,"w",encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False,indent=2)
    return file_path
    