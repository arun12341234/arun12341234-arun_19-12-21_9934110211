


from datetime import date
from flask import Flask
from flask import Flask, redirect, url_for, render_template, request, flash
# from sqlalchemy.orm.properties import ColumnProperty

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
# r = redis.Redis(host='49.206.19.247',
# port=9736,
# db=0)
# # print(r)
# print(r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"}))
# print(r.get("Bahamas").decode("utf-8"))


# print(q.enqueue('a'))


r = redis.StrictRedis(host='49.206.19.247', port=9736, db=0)
# print(r)
# r.set('foo', 'bar')


# print(r.get('foo'))
# r.hmset('user', {'username': 'foo', 'birth_year': 1977})
# r.hmset('user', {'username': 'foo1', 'birth_year': 1977})
# print(r.hgetall('user'))

# r.sadd('a',1)
# # print(r.smembers('a'))

# # r.srem('a',1)
# # print(type(r.smembers('a')))
# s = r.smembers('a')
# # print(type(s))
# # print(len(s))
# if len(s) == 0:
#     print("Set is empty")
# else:
#     print("Set is not empty")


#     for x in range(50):

#         new_s= r.scard('a')+1
#         print(new_s)
#         print(r.srem('a',r.scard('a')))
#         print(new_s)
#         print(r.sadd('a',new_s))

#     if(r.scard('a')==50):
#         # return '{"message": "", "error": "limit reached for from <from>”"}'
#         print('limit reached for from <from>')



    # print(r.smembers('a'))

# import datetime


# pint(new Date)
# r.expire(name, time)




# reset counter




def addToCache(k,t):
    r.hset(k)

    r.expire(k, t)



def formatKey(_to,_from):
  return "STOP_" + str(min(_to,_from))+"_"+str(max(_to,_from))

def formatapiKey(_to,_from):
  return "API_" + str(_from)+"_"+str(_to)


# r.hget(formatKey(10,29),1)
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
                    # print('stored in cache as a unique entry')

                    # setdata = {"from": data['from'], "to": data['to']}
                    # print(setdata)
                    

                    # r.mset(setdata)
                    # print(r.get("from").decode("utf-8"))
                    # print(r.get("to"))

                    k = formatKey(data['to'],data['from'])
                    # # 'STOP_'+str(data['to'])+'_'+str(data['from'])
                    # print(k)
                    
                    # addToCache(k)
                    # print(r.hgetall(k))

                    
                    exist = r.hget(k, 'from')
                    if exist==None:


                        r.hmset(k, {'from': data['from'], 'to': data['to']})
                        r.expire(k,14400)

                    # for x in range(200):
                    #     print(r.hget(k, 'from').decode("utf-8"))

                    # print(
                    # r.hget('user', 'from').decode("utf-8")
                    # )
                    




                    return '{"message": "inbound sms ok", "error": ""}'

                else:
                    return '{"message”: "", "error": "unknown failure"}'


 


       


            
# account








    








@app.route("/outbound/sms/",methods=['POST'])
def outbound():

    if request.method == 'POST':
        # print(type(request.data))
        
        data = request.get_json(force=True)
        # print(data)
        # print(len(data['from']))
        # print(data['to'])
        # print(data['text'])
        # print(r.hgetall('user'))






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

        else:
            parameter_name_check = True

        if(parameter_name_check==True):
            # print(data['from'],r.hget('user', 'from').decode("utf-8"))
            # print(data['from'], r.hget('user', 'to').decode("utf-8"))
            k = formatKey(data['to'],data['from'])
            exist = r.hget(k, 'from')
            # print( r.hget(k, 'from'), r.hget(k, 'to'))

            # return str(exist)
            if exist!=None:
            # if(data['from']== r.hget('user', 'from').decode("utf-8") and data['to']== r.hget('user', 'to').decode("utf-8")):
                # print('here')

                return '{"message": "", "error": "sms from '+ data["from"] +' to '+data["to"]+' blocked by STOP request"}'

                

            else:
                k_api = formatapiKey(data['to'],data['from'])

                s = r.smembers(k_api)
                # r.expire(k_api,0)
                # print(r.smembers(k_api))


                if len(s) == 0:
                    print(s)
                    # r.sadd(k_api,1)
                    r.hset(k_api, 1, 1)
                    r.expire(k_api,86400)

                else:
                    # print(s)
                    new_s= r.scard(k_api)+1
                    print(new_s,'new_s')
                    # r.srem(k_api,r.scard(k_api))
                    # print(r.scard(k_api),'scard')

                    # print(
                    # # r.sadd(k_api,100)
                    # r.sadd(k_api, 1, 2, 3)
                    #     )
                    # # print(new_s,'new_s1')
                    # print(r.scard(k_api),'scard2')
                    r.sadd(k_api,new_s)
                    # print(r.scard(k_api))
                    # r.srem(k_api,r.scard(k_api))
                    # print(r.scard(k_api),'scard2')
                    # print(r.scard(k_api))
                    # print(r.smembers(k_api))
                    # r.hset(k_api, new_s, 1)
                    # print(r.hkeys(k_api))
                    # r.sadd(k_api, new_s)

                    r.sdiff(k_api,new_s)#this will retive with new set as well as old together
                    print(r.smembers(k_api))
                    print(
                        len(r.smembers(k_api))
                        )
                    # print(r.s)
                    if len(r.smembers(k_api))>50:
                        print("error")
                        return '{"message": "", "error": "limit reached for from '+str(data["from"])+'"}'
                        
                    
                    # else:
                        



      


                    # if(r.scard(k_api)>=50):
                        
                        
                    # else:

                # api_exist = r.hget(k_api, 'from')
                # if api_exist==None:
                #     r.hmset(k, {'from': data['from'], 'to': data['to']})

                        cur.execute("SELECT * FROM phone_number WHERE number=%(number)s", {'number': data['from'] } )
                        row = cur.fetchone()

                        print(row,'row')


                        if row == None:
                        
                            return '{"message”: "", "error": "from parameter not found"}'
            


        # print(
        #     r.hget('user', 'from').decode("utf-8")
        #     )

            # if 

            # {“message”: “”, “error”: “sms from <from> to <to> blocked by STOP request”}


    return '{"message": "outbound sms ok", "error": ""}'

    


if __name__ == '__main__':
    # app.debug = True
    app.run()