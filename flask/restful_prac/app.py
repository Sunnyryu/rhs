from flask import Flask
from flask_restful import reqparse, Api, abort, Resource

# Flask 인스턴스!!
app = Flask(__name__)
api = Api(app)

#마이리스트 
TODOS = {
    'todo1' : {'task': 'try to lotto'},
    'todo2' : {'task': 'watch movie'},
    'todo3' : {'task': 'life coding'}
}

# except 
def abort_if_todo_not_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} not exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

# 마이리스트
# GET, DELETE, PUT 정의
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_not_exist(todo_id)
        return TODOS[todo_id]
    
    def delete(self, todo_id):
        abort_if_todo_not_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task 
        return task, 201 


# 리스트 
# GET POST 
class Todolist(Resource):
    def get(self):
        return TODOS 
    
    def post(self):
        args = parser.parse_args()
        todo_id = 'todo%d' % (len(TODOS) + 1)
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


## url Router에 맵핑 (REST Url 정의 )

api.add_resource(Todolist, '/todos/')
api.add_resource(Todo, '/todos/<string:todo_id>')

# 터미널에서 curl을 이용한 restful!!
# curl http://localhost:5000/todos => 목록 가져오기 
# curl curl http://localhost:5000/todos/todo3 => 단일 테스크 가져오기!
# curl http://localhost:5000/todos/todo2 -X DELETE -v => 2번 테스크 삭제
# curl http://localhost:5000/todos -d "task=something new" -X POST -v =>테스크 추가 
# curl http://localhost:5000/todos/todo3 -d "task=something different" -X PUT -v => 테스크 업데이트 

# 서버 실행 
if __name__=='__main__':
    app.run(debug=True)
