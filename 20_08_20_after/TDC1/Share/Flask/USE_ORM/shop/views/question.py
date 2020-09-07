# home 
from flask import Flask , render_template, url_for, request, redirect, Blueprint,session, g
from shop.models import Question, Answer, User, question_voter, answer_voter
from shop.forms import QuestionForm, AnswerForm
from shop import db
from werkzeug.utils import redirect
from datetime import datetime
from shop.views.auth import login_required
from sqlalchemy import func
qa = Blueprint('qa', __name__, url_prefix='/question')

@qa.route("/")
def question():
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    so = request.args.get('so', type=str, default='recent')
    # ---------------------------------------------------------------------------------------- #
    # 정렬
    if so == 'recommend':
        sub_query = db.session.query(question_voter.c.question_id, func.count('*').label('num_voter')) \
            .group_by(question_voter.c.question_id).subquery()
        question_list = Question.query \
            .outerjoin(sub_query, Question.id == sub_query.c.question_id) \
            .order_by(sub_query.c.num_voter.desc(), Question.create_date.desc())
    elif so == 'popular':
        sub_query = db.session.query(Answer.question_id, func.count('*').label('num_answer')) \
            .group_by(Answer.question_id).subquery()
        question_list = Question.query \
            .outerjoin(sub_query, Question.id == sub_query.c.question_id) \
            .order_by(sub_query.c.num_answer.desc(), Question.create_date.desc())
    else:  # recent
        question_list = Question.query.order_by(Question.create_date.desc())
    
    #question_list = Question.query.order_by(Question.create_date.desc())
    if kw:
        search = '%%{}%%'.format(kw)
        sub_query = db.session.query(Answer.question_id, Answer.content, User.username) \
            .join(User, Answer.user_id == User.id).subquery()
        question_list = question_list \
            .join(User) \
            .outerjoin(sub_query, sub_query.c.question_id == Question.id) \
            .filter(Question.subject.ilike(search) |  # 질문제목
                    Question.content.ilike(search) |  # 질문내용
                    User.username.ilike(search) |  # 질문작성자
                    sub_query.c.content.ilike(search) |  # 답변내용
                    sub_query.c.username.ilike(search)  # 답변작성자
                    ) \
            .distinct()
    # ---------------------------------------- [edit] ---------------------------------------- #
    question_list = question_list.paginate(page, per_page=10, error_out=False)
    return render_template('question.html', question_list=question_list, page=page, kw=kw, so=so)

@qa.route('/detail/<int:question_id>/')
def detail_rc(question_id):
    print(question_id)
    page = request.args.get('page', type=int, default=1)
    so = request.args.get('so', type=str, default='recent')
    form = AnswerForm()
    answer_list = Answer.query.filter_by(question_id=question_id).order_by(Answer.create_date.desc())
    question = Question.query.get_or_404(question_id)    
    a = Question.query.filter_by(id=question_id).first()
    query = Question.query.get(question_id)
    if question_id:
        a.read_count = a.read_count + 1
        print(55)
        db.session.commit()
        
    #answer_list = Answer.query.filter_by(question_id=question_id).order_by(Answer.create_date.desc())
    answer_list = answer_list.paginate(page, per_page=5, error_out=False)   
    return render_template('question_detail.html', question=question, form=form, answer_list=answer_list, so=so)

@qa.route('/detail/<int:question_id>/')
def detail(question_id):
    print(question_id)
    page = request.args.get('page', type=int, default=1)
    so = request.args.get('so', type=str, default='recent')
    form = AnswerForm()
    if so == 'recommend':
        sub_query = db.session.query(answer_voter.c.answer_id, func.count('*').label('num_voter')) \
            .group_by(answer_voter.c.answer_id).subquery()
        answer_list = Answer.query \
            .outerjoin(sub_query, Answer.id == sub_query.c.answer_id) \
            .order_by(sub_query.c.num_voter.desc(), Answer.create_date.desc())
        question = Question.query.get_or_404(question_id)    
        answer_list = answer_list.paginate(page, per_page=5, error_out=False)   
        return render_template('question_detail.html', question=question, form=form, answer_list=answer_list, so=so)
    else:  # recent
        answer_list = Answer.query.filter_by(question_id=question_id).order_by(Answer.create_date.desc())
        question = Question.query.get_or_404(question_id)    
        answer_list = answer_list.paginate(page, per_page=5, error_out=False)   
        return render_template('question_detail.html', question=question, form=form, answer_list=answer_list, so=so)

    question = Question.query.get_or_404(question_id)
    #answer_list = Answer.query.filter_by(question_id=question_id).order_by(Answer.create_date.desc())
    answer_list = answer_list.paginate(page, per_page=5, error_out=False)   
    return render_template('question_detail.html', question=question, form=form, answer_list=answer_list, so=so)
@qa.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    form = QuestionForm()
    print(form)
    print(form.validate_on_submit())
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now(), read_count=0, user=g.user)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('hm.index'))
    return render_template('question_form.html', form=form)

@qa.route('/modify/<int:question_id>', methods=('GET', 'POST'))
@login_required
def modify(question_id):
    question = Question.query.get_or_404(question_id)
    if g.user != question.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('qa.detail', question_id=question_id))
    if request.method == 'POST':
        form = QuestionForm()
        if form.validate_on_submit():
            form.populate_obj(question)
            question.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('qa.detail', question_id=question_id))
    else:
        form = QuestionForm(obj=question)
    return render_template('question_form.html', form=form)


@qa.route('/delete/<int:question_id>')
@login_required
def delete(question_id):
    question = Question.query.get_or_404(question_id)
    if g.user != question.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('qa.detail', question_id=question_id))
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('qa.question'))