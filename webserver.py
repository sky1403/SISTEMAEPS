import mysql.connector
from flask import Flask,render_template, request, redirect, url_for, session
from mysqldb import REGISTER, R_USERS, conection, PQRS_INSERT, InitialPQR





app= Flask("EPS Gran colombia")

app.secret_key="meditta6@1235"


"""PLANTILLAS"""
@app.route("/", methods=['POST', 'GET'])
def principal_page():
    return render_template('index.html')



@app.route("/data-successfully", methods=["POST","GET"])
def AjaxData():
    if request.method=="POST":
        PQR_NAME=request.form['name'] 
        PQR_DOC=request.form['id']
        PQR_EMAIL=request.form['email']
        PQR_PHONE=request.form['phone']
        PQR_PQR=request.form['PQRS']    
        activator= None
        if activator is None:
                try:
                    InitialPQR(PQR_DOC,PQR_NAME,PQR_PHONE,PQR_EMAIL,PQR_PQR)
                except:
                    activator = "Ya se ha enviado la peticion"
    return redirect(url_for('principal_page'))

@app.route("/oficina-virtual-afiliados")
def office_afl():
    return render_template('lgafl.html')

@app.route("/oficina-virtual-empleadores", methods=['POST', 'GET'])
def virtual_office_workers():
    return render_template('lgemple.html')

@app.route("/PQRS", methods=['POST', 'GET'])
def PQRS():
    return render_template('PQRS.html')


@app.route("/registro-empresas", methods=['POST', 'GET'])
def reg_empre():
    return render_template('reg_empre.html')


@app.route("/new-user-afl")
def register_afl():
    return render_template('register.html')




@app.route("/<name>")
def titulo_dinamico(name):
    return render_template('404.html', titulo=name)


"""AJAX CONTENT- DASHBOARD USUARIOS"""

@app.route("/agenda")
def agenda():
    if 'id' in session:
            return render_template('agenda.html')
    return redirect(url_for('principal_page'))

@app.route("/home")
def home():
    if 'id' in session:
            return render_template('home.html')
    return redirect(url_for('principal_page'))
    
@app.route("/rcar")
def rcar():
    if 'id' in session:
            return render_template('rcar.html')
    return redirect(url_for('principal_page'))

@app.route("/rlab")
def rlab():
    if 'id' in session:
            return render_template('rlab.html')
    return redirect(url_for('principal_page'))

@app.route("/au")
def au():
    if 'id' in session:
            return render_template('au.html')
    return redirect(url_for('principal_page'))

@app.route("/cer")
def cer():
    if 'id' in session:
            return render_template('cer.html')
    return redirect(url_for('principal_page'))

@app.route("/update")
def update():
    if 'id' in session:
        return render_template('update.html')
    return redirect(url_for('principal_page'))





"""REGISTRO EMPRESAS"""""       

@app.route("/success-register",  methods=["POST", "GET"])
def Insertdata():
    if request.method == "POST":
        hw_pw= request.form['password']
        username=request.form['username'] 
        typedoc=request.form['tdocument']
        document=request.form['document']
        email=request.form['email']
        social=request.form['razonsocial']
        phone=request.form['phone']    
        error= None
        if error is None:
                try:
                    REGISTER(typedoc, document, username, social, phone, email, hw_pw)
                except:
                    error = f"el usuario {username} ya se encuentra registrado"

    return redirect(url_for("virtual_office_workers"))
    

"""REGISTRO DE USUARIOS"""

@app.route("/success-r", methods=["POST", "GET"])
def r_users():
    if request.method == "POST":
        t_doc=request.form['tdocumento'] 
        doc=request.form['documento'] 
        name=request.form['name']  
        lname=request.form['lname']  
        date=request.form['date']  
        phone=request.form['phone']  
        email=request.form['email']  
        password= request.form['password']
        error = None
        if error is None:
            try:
                R_USERS(t_doc, doc, name, lname, date, phone, email, password)
            except:
                error=f"el usuario {doc} ya se encuentra registrado"
    return redirect(url_for("office_afl"))

"""PQRS"""

@app.route("/successfuly", methods=["POST", "GET"])
def PQRS_SUCCESS():
    if request.method == "POST":
        typedoc= request.form['tdoc']
        name=request.form['name'] 
        lastname=request.form['lname']
        documento=request.form['doc']
        correo=request.form['email']
        PQRS=request.form['PQRS']   
        enter= None
        if enter is None:
            try:
                PQRS_INSERT(typedoc,documento,name,lastname,correo,PQRS)
                    
            except:
                print("ERROR")
    return redirect(url_for("PQRS"))
    



"""DESTRUCCION DE SESIONES Y SESIONES"""


"""SESION USUARIOS"""
@app.route("/office-user")
def dashboard():
    if 'id' in session:
        return render_template('dashboard.html', USER=session['username'])

    return redirect(url_for('principal_page'))


"""SESION EMPRESAS"""
@app.route("/dashboard-workers")
def d_workers():
    if 'username' in session:
            return render_template('dash-empresa.html', username=session['username'])
    return redirect(url_for('principal_page'))
    

"""LOGOUT USUARIOS"""
@app.route("/logout")
def logout():
    if 'id' in session:
        session.pop('id', None)
        return redirect(url_for('office_afl'))
    

"""LOGOUT EMPRESAS"""
@app.route("/destroylogout")
def logoutempresas():
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for('virtual_office_workers'))









"""VALIDACIONES"""

@app.route('/login', methods=['POST', 'GET'])
def validate():
    if request.method == 'POST':
        TYPE=request.form['tdoc']
        Document=str(request.form['DOC'])
        PW=request.form['PASSWORD']
        cursor=conection.cursor(buffered=True, dictionary=True)
        query="SELECT  NAME, lastname, PASSWORD  FROM `users_afl` WHERE `document` = {0}".format(Document)
        cursor.execute(query)
        datos=cursor.fetchone()
        pw_hash=datos['PASSWORD']
        if PW == pw_hash:
            session['id'] = Document
            session['username'] = datos['NAME'] + datos['lastname']
            conection.close()
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('office_afl'))
            conection.close()


@app.route('/empresas', methods=['POST', 'GET'])
def validate_empresas():
    if request.method == 'POST':
        user=request.form['username']
        PASS=request.form['password']
        cursor=conection.cursor(buffered=True, dictionary=True)
        QUERY=("SELECT * FROM users_empresas WHERE user='%s'" % (user,))
        cursor.execute(QUERY)
        data=cursor.fetchone()
        pw_hash2=data['password']
        id_user=data['id']
        if PASS == pw_hash2:
            session['id'] = id_user
            session['username'] = data['user']
            return redirect(url_for('d_workers'))
        else:
            return redirect(url_for('virtual_office_workers'))
            
            




if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0', port='5000')
