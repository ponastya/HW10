from flask import Flask
from utils import load_json, format_candidates, get_candidate_by_id, get_all_candidates, candidate_by_skills

app = Flask(__name__)


@app.route("/")
def index():
    result = format_candidates(get_all_candidates())
    return result


@app.route("/candidate/<int:uid>")
def candidate_by_id(uid):
    candidate = get_candidate_by_id(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result


@app.route("/skills/<skill>")
def skills(skill):
    candidate = candidate_by_skills(skill.lower())
    result = format_candidates(candidate)
    return result


app.run(debug=True)
