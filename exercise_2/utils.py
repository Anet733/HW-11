import json

def load_candidates_from_json():
    """
    Возвращает список всех кандидатов
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidate(id):
    """
    Возвращает одного кандидата по его id
    """
    for candidate in load_candidates_from_json():
        if candidate['id'] == id:
            return candidate


def get_candidates_by_name(name):
    """
    Возвращает кандидатов по имени
    """
    names = []
    for candidate in load_candidates_from_json():
        if name.lower() in candidate['name'].lower():
            names.append(candidate)
    return names

def get_candidates_by_skill(skill):
    """
    Возвращает кандидатов по навыку
    """
    candidates = []
    for candidate in load_candidates_from_json():
        skills = candidate['skills'].lower().split(', ')
        if skill in skills:
            candidates.append(candidate)
    return candidates

