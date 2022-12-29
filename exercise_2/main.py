from flask import Flask, request, render_template
import utils

app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = utils.load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:id>')
def candidate_by_id(id):
    candidate = utils.get_candidate(id)
    return render_template('card.html', candidate=candidate)


@app.route('/search/<name>')
def candidate_by_name(name):
    candidates = utils.get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates, count_candidates=len(candidates))


@app.route('/skill/<skill>')
def candidate_by_skill(skill):
    candidates = utils.get_candidates_by_skill(skill)
    return render_template('skill.html', candidates=candidates, count_cand=len(candidates))

app.run(debug=True)