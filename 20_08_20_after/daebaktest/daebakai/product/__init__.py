# product
from flask import Flask , render_template, url_for, request, redirect, Blueprint, session, flash
from daebakai import db 

product = Blueprint('product', __name__,url_prefix='/product')
 

@product.route("/")
def Main():
    
   
    return render_template('product-main.html')
    
    
@product.route("/register", methods=['GET', 'POST'])
def Register():

    author_id = session['id']
    mother_id = '1'
    if request.method == 'POST':
        
        data = request.form.to_dict()
  
        del data['csrf_token']

        columns = '`id`,'+'`a_id`,'+'`mother_id`,'
        values = "NULL,"+"'"+str(author_id)+"',"+"'"+str(author_id)+"',"
        columns += ', '.join("`"+str(x)+"`" for x in data.keys())
        values += ', '.join("'"+str(x)+"'" for x in data.values())

        sql = "INSERT INTO %s (%s) VALUES (%s)"%('`user-product`',columns, values)

  
        # DB 사용
        cursor = db.get_db().cursor() 
        
        
        cursor.execute(sql)
        db.get_db().commit()
       
      
        # flash("저장하였습니다")
        flash(sql)
        return render_template('product-main.html')
        


   
   
    return render_template('product-main.html')
    
    
 
 
