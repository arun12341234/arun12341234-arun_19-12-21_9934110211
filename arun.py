


from flask import Flask
from flask import Flask, redirect, url_for, render_template, request, flash
from sqlalchemy.orm.properties import ColumnProperty

app = Flask(__name__)







import psycopg2
conn_string = "host='49.206.19.247' dbname='demo' user='admin' password='root' port=8338"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()





import os

import redis
# from rq import Worker, Queue, Connection

# listen = ['default']

# redis_url = os.getenv('REDISTOGO_URL', 'redis://49.206.19.247/:9736')

# rd_conn = redis.from_url(redis_url)

# print(rd_conn)

# q = Queue(connection=rd_conn)
# print(q)
# print(q)
r = redis.Redis(host='49.206.19.247',
port=9736,
db=0)
# # print(r)
print(r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"}))
print(r.get("Bahamas").decode("utf-8"))


# print(q.enqueue('a'))


# r = redis.StrictRedis(host='49.206.19.247', port=9736, db=0)
# print(r)
# r.set('foo', 'bar')


# print(r.get('foo'))
# r.hmset('user', {'username': 'foo', 'birth_year': 1977})
# r.hmset('user', {'username': 'foo1', 'birth_year': 1977})
# print(r.hgetall('user'))

@app.route("/inbound/sms/",methods=['POST','GET'])
def inbound():

    if request.method == 'POST':

        
        data = request.get_json(force=True)

        if data['from']=='':
            return '{"message": "", "error": "from is missing”"}'
        elif data['to']=='':
            return '{"message": "", "error": "to is missing”"}'
        elif data['text']=='':
            return '{"message": "", "error": "text is missing”"}'
        elif len(data['from'])>16 or len(data['from'])<6:
            return '{"message": "", "error": "from is invalid"}'
        elif len(data['to'])>16 or len(data['to'])<6:
            return '{"message": "", "error": "to is invalid"}'
        elif len(data['text'])>120 or len(data['text'])<1:
            return '{"message": "", "error": "text is invalid"}'
        else:
            parameter_name_check = True

        if(parameter_name_check==True):
            # print('valid')

         


            cur.execute("SELECT * FROM phone_number WHERE number=%(number)s", {'number': data['to'] } )
            row = cur.fetchone()
            # print(row)

            if row == None:
                
                return '{"message”: "", "error": "to parameter not found"}'

            else:

                # STOP or STOP\n or STOP\r or STOP\r\n
                # print(row[2])
                if(data['text']=='STOP' or data['text']=='STOP\n' or data['text']=='STOP\r' or data['text']=='STOP\r\n'):
                    print('stored in cache as a unique entry')


                return '{"message": "inbound sms ok", "error": ""}'

 


       


            
# account








    








@app.route("/outbound/sms/",methods=['POST'])
def outbound():

    if request.method == 'POST':
        # print(type(request.data))
        
        data = request.get_json(force=True)
        print(data)
        print(len(data['from']))
        print(data['to'])
        print(data['text'])
        if data['from']=='':
            return '{"message": "", "error": "from is missing”"}'
        elif data['to']=='':
            return '{"message": "", "error": "to is missing”"}'
        elif data['text']=='':
            return '{"message": "", "error": "text is missing”"}'
        if len(data['from'])>16 or len(data['from'])<6:
            return '{"message": "", "error": "from is invalid"}'
        elif len(data['to'])>16 or len(data['to'])<6:
            return '{"message": "", "error": "to is invalid"}'
        elif len(data['text'])>120 or len(data['text'])<1:
            return '{"message": "", "error": "text is invalid"}'


    return '{"message": "inbound sms ok", "error": ""}'

    


if __name__ == '__main__':
    # app.debug = True
    app.run()