from flask import Blueprint, url_for, flash, g
from werkzeug.utils import redirect

from shop import db
from shop.models import Question, Answer
from shop.views.auth import login_required

vt = Blueprint('vt', __name__, url_prefix='/vote')


@vt.route('/question/<int:question_id>/')
@login_required
def question(question_id):
    _question = Question.query.get_or_404(question_id)
    if g.user == _question.user:
        flash('본인이 작성한 글은 추천할수 없습니다')
    else:
        _question.voter.append(g.user)
        db.session.commit()
    return redirect(url_for('qa.detail', question_id=question_id))

@vt.route('/answer/<int:answer_id>/')
@login_required
def answer(answer_id):
    _answer = Answer.query.get_or_404(answer_id)
    if g.user == _answer.user:
        flash('본인이 작성한 글은 추천할수 없습니다')
    else:
        _answer.voter.append(g.user)
        db.session.commit()
    return redirect(url_for('qa.detail', question_id=_answer.question.id))