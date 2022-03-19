from flask import Flask, render_template
import util

app = Flask(__name__)

#THESE WERE THE VARIABLES I NEEDED TO TEST LOCALLY
# username="postgres"
# password="test"
# host="localhost"
# port="5432"
# database="hw3"

#THESE ARE THE VARIABLES PROFESSOR WU SHOULD BE USING
username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

@app.route('/')
def index():
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "SELECT a, fruit_a, b, fruit_b FROM basket_a FULL JOIN basket_b ON fruit_a = fruit_b;")
    if record == -1:
        # Error message in case something goes wrong
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        col_names = [desc[0] for desc in cursor.description]
        log = record
    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('index.html', sql_table = log, table_title=col_names)

@app.route('/api/update_basket_a')
def update_basket_a():
# connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands
    log = util.run_and_insert_sql(cursor, connection, "INSERT INTO basket_a (a, fruit_a) VALUES(5,'Cherry');")
    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    #Respond based on success or failure
    if log == 1:
        return render_template('/update_basket_a.html', log_html="Success!")
    else:
        return render_template('/update_basket_a.html', log_html=log)

        
@app.route('/api/unique')
def unique():
# connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "SELECT a, fruit_a, b, fruit_b FROM basket_a FULL JOIN basket_b ON fruit_a = fruit_b WHERE  a is NULL OR b is NULL;")
    if record == -1:
        #print error message
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        col_names = [desc[0] for desc in cursor.description]
        # only use the first five rows
        log = record
    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('unique.html', sql_table = log, table_title=col_names)


    	

if __name__ == '__main__':
	# set debug mode
    app.debug = True
     
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
    