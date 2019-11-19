from django.shortcuts import render, redirect
from .models import Question, Choice
# Create your views here.
def index(request):
    questions = Question.objects.all()

    context = {
            'questions': questions
    }
    return render(request, 'question/index.html', context)
def new(request):
    if request.method == "POST":
        question = Question(question=request.POST.get('question'))
        question.save()
        return redirect('question:index')
    else:
        return render(request, 'question/new.html')
def detail(request, que_id):
    question = Question.objects.get(id=que_id)
    surveys = question.choice_set.all()
    context = {

            'question': question,
            'surveys': surveys


            }
    return render(request, 'question/detail.html', context)

def edit(request, que_id):
    que = Question.objects.get(id=que_id)
    if request.method == "POST":
        text = request.POST.get('question')
        que.question = text
        que.save()
        return redirect('question:detail', que.id)
    else:
        context = {
                "question":que
        }
        return render(request, 'question/edit.html', context)
def delete(request, que_id):
    que = Question.objects.get(id=que_id)
    if request.method == "POST":
        que.delete()
    return redirect('question:index')
def survey(request, que_id):
    question = Question.objects.get(id=que_id)
    if request.method == "POST":
        text = request.POST.get('survey')
        s = Choice()
        s.survey = text
        s.question = question
        s.save()
    return redirect('question:detail', question.id)
def survey_edit(request, c_id):
    survey = Choice.objects.get(id=c_id)

    if request.method == "POST":
        text = request.POST.get('survey')
        survey.survey = text
        survey.save()
        return redirect('question:detail', survey.question_id)
    else:
        context = {
                "survey": survey
                }
        return render(request, 'question/sur_edit.html', context)
def survey_del(request, c_id):
    survey = Choice.objects.get(id=c_id)
    if request.method == "POST":
        survey.delete()

    return redirect('question:detail', survey.question_id)
def vote(request, c_id):
    survey = Choice.objects.get(id=c_id)
    if request.method == "POST":
        survey.votes += 1
        survey.save()
        return redirect('question:detail', survey.question_id)
