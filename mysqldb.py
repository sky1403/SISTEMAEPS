import mysql.connector


conection = mysql.connector.connect(user='root', password='', host='localhost', database='epsg_colombia', port="3306")






def REGISTER(tdoc, id, user, r_social, phone, email, password):
    cursor=conection.cursor()
    insert="INSERT INTO `users_empresas`(`type_doc`, `id`, `user`, `r_social`, `phone`, `email`, `password`) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(tdoc, id, user, r_social, phone, email, password)
    cursor.execute(insert)
    conection.commit()
    
    if cursor.execute(insert):
        print("Error Al enviar Datos")
    else:
        print("Datos Enviados")
        conection.close()


def R_USERS(t_doc, doc, name, lname, date, phone, email, password):
    cursor=conection.cursor()
    sql="INSERT INTO `users_afl`(`t_document`, `document`, `name`, `lastname`, `date`, `phone`, `email`, `password`) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(t_doc, doc, name, lname, date, phone, email, password)
    cursor.execute(sql)
    conection.commit()

    if cursor.execute(sql):
        print("Error al registrar")
    else:
        print("Datos enviados") 
        conection.close()






def PQRS_INSERT(tdoc,doc,name,lname,email,PQRS):
    cursor=conection.cursor(buffered=True)
    QUERY="INSERT INTO `pqrs`(`t_doc`, `doc`, `name`, `lname`, `email`, `PQRS`) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(tdoc,doc,name,lname,email,PQRS)
    cursor.execute(QUERY)
    conection.commit()
    if cursor.execute(QUERY)==True:
        print("hecho")
    else:
        print("error")
    return True 

def InitialPQR(Pdoc,Pname,Pphone,Pemail,PPQRS):
    cursor=conection.cursor(buffered=True)
    QUERY="INSERT INTO `pqr_init`(`DOC`, `NAME`, `PHONE`, `EMAIL`, `PQRS`) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(Pdoc,Pname,Pphone,Pemail,PPQRS)
    cursor.execute(QUERY)
    conection.commit()
    if cursor.execute(QUERY)==True:
        print("hecho")
    else:
        print("error")
    return True 