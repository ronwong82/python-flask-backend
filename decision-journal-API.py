from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_restful import reqparse
import psycopg2

app = Flask(__name__)
CORS(app)
api = Api(app)

# postgres configurations

conn = psycopg2.connect("dbname='decision_journal' user='postgres' host='localhost' password='qctech123'")


class CreateUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, help='Username to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()

            _userName = args['username']
            _userPassword = args['password']

            #conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('decision_journal_CreateUser', (_userName, _userPassword))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode': 200, 'Message': 'User creation success'}
            else:
                return {'StatusCode': 1000, 'Message': str(data[0])}

        except Exception as e:
            return {'error': str(e)}


class AuthenticateUser(Resource):
    def post(self):
        try:
            # Parse the arguments

            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, help='Username for Authentication')
            parser.add_argument('password', type=str, help='Password for Authentication')
            args = parser.parse_args()

            _userName = args['username']
            _userPassword = args['password']

            #conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('decision_journal_AuthenticateUser', (_userName, _userPassword))
            data = cursor.fetchall()

            if len(data) > 0:
                return {'status': 200, 'UserId': str(data[0][0])}
            else:
                return {'status': 100, 'message': 'Authentication failure'}

        except Exception as e:
            return {'error': str(e)}


class AddDecision(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str)
            parser.add_argument('date', type=str)
            parser.add_argument('time', type=str)
            parser.add_argument('title', type=str)
            parser.add_argument('is_energized', type=bool)
            parser.add_argument('is_focused', type=bool)
            parser.add_argument('is_relaxed', type=bool)
            parser.add_argument('is_confident', type=bool)
            parser.add_argument('is_tired', type=bool)
            parser.add_argument('is_accepting', type=bool)
            parser.add_argument('is_accomodating', type=bool)
            parser.add_argument('is_anxious', type=bool)
            parser.add_argument('is_resigned', type=bool)
            parser.add_argument('is_frustrated', type=bool)
            parser.add_argument('is_angry', type=bool)
            parser.add_argument('situation', type=str)
            parser.add_argument('problem', type=str)
            parser.add_argument('variables', type=str)
            parser.add_argument('complications', type=str)
            parser.add_argument('alternatives', type=str)
            parser.add_argument('outcomes', type=str)
            parser.add_argument('expectations', type=str)
            parser.add_argument('outcome', type=str)
            parser.add_argument('review_date', type=str)
            parser.add_argument('learning', type=str)

            args = parser.parse_args()

            _username = args['username']
            _date = args['date']
            _time = args['time']
            _title = args['title']
            _is_energized = args['is_energized']
            _is_focused = args['is_focused']
            _is_relaxed = args['is_relaxed']
            _is_confident = args['is_confident']
            _is_tired = args['is_tired']
            _is_accepting = args['is_accepting']
            _is_accomodating = args['is_accomodating']
            _is_anxious = args['is_anxious']
            _is_resigned = args['is_resigned']
            _is_frustrated = args['is_frustrated']
            _is_angry = args['is_angry']
            _situation = args['situation']
            _problem = args['problem']
            _variables = args['variables']
            _complications = args['complications']
            _alternatives = args['alternatives']
            _outcomes = args['outcomes']
            _expectations = args['expectations']
            _outcome = args['outcome']
            _review_date = args['review_date']
            _learning = args['learning']

            #conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('decision_journal_DecisionEntry', (_username, _date, _time, _title, _is_energized, _is_focused, _is_relaxed, _is_confident, _is_tired, _is_accepting, _is_accomodating, _is_anxious, _is_resigned, _is_frustrated, _is_angry, _situation, _problem, _variables, _complications, _alternatives, _outcomes, _expectations, _outcome, _review_date, _learning))
            data = cursor.fetchall()

            conn.commit()
            return {'StatusCode': 200, 'Message': 'Success'}

        except Exception as e:
            return {'error': str(e)}


class GetDecisions(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str)
            parser.add_argument('decision_title', type=str)
            args = parser.parse_args()

            _username = args['username']
            _decision_title = args['decision_title']

            #conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('decision_journal_GetDecisions', (_username, _decision_title))
            data = cursor.fetchall()

            items_list = [];
            for item in data:
                i = {
                    'decision_id': item[0],
                    'decision_username': item[1],
                    'decision_title': item[2],
                    'decision_is_energized': item[3],
                    'decision_is_focused': item[4],
                    'decision_is_relaxed': item[5],
                    'decision_is_confident': item[6],
                    'decision_is_tired': item[7],
                    'decision_is_accepting': item[8],
                    'decision_is_accomodating': item[9],
                    'decision_is_anxious': item[10],
                    'decision_is_resigned': item[11],
                    'decision_is_frustrated': item[12],
                    'decision_is_angry': item[13],
                    'decision_situation': item[14],
                    'decision_problem': item[15],
                    'decision_variables': item[16],
                    'decision_complications': item[17],
                    'decision_alternatives': item[18],
                    'decision_outcomes': item[19],
                    'decision_expectations': item[20],
                    'decision_outcome': item[21],
                    'decision_learning': item[22],
                    'decision_date': str(item[23]),
                    'decision_time': str(item[24]),
                    'decision_review_date': str(item[25])
                }
                items_list.append(i)

            return {'StatusCode': '200', 'Items': items_list}

        except Exception as e:
            return {'error': str(e)}


class UpdateUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, help='Username to update user')
            parser.add_argument('password', type=str, help='password to be updated')
            parser.add_argument('email', type=str, help='email to be updated')
            parser.add_argument('index', type=int, help='selection of attribute to be updated')
            args = parser.parse_args()

            _userName = args['username']
            _userPassword = args['password']
            _userEmail = args['email']
            _userSelection = args['index']

            #conn = mysql.connect()
            cursor = conn.cursor()
            if _userSelection == 1:
                cursor.callproc('decision_journal_UpdateProfile', (_userName, _userPassword, _userSelection))
            elif _userSelection == 2:
                cursor.callproc('decision_journal_UpdateProfile', (_userName, _userEmail, _userSelection))
            data = cursor.fetchall()

            conn.commit()
            return {'StatusCode': 200, 'Message': 'User Update success'}

        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateUser, '/CreateUser')
api.add_resource(AuthenticateUser, '/AuthenticateUser')
api.add_resource(AddDecision, '/AddDecision')
api.add_resource(GetDecisions, '/GetDecisions')
api.add_resource(UpdateUser, '/UpdateUser')

if __name__ == '__main__':
    app.run(debug=True)
