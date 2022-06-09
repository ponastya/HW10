import json


def load_json():
    with open("candidates.json", 'r', encoding="utf-8") as file:
        datas = json.load(file)
        return datas


def format_candidates(datas: list[dict]) -> str:
    text = '<pre>'
    for data in datas:
        text += f"""
        Имя кандидата: {data['name']}\n
        Позиция: {data['position']}\n
        Навыки: {data['skills']}\n
        """
    text += '</pre>'
    return text


def get_all_candidates() -> list[dict]:
    return load_json()

def get_candidate_by_id(uid: int):
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate
    return None

def candidate_by_skills(skill):
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', ') :
            result.append(candidate)
    return result

