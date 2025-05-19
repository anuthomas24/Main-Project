from flask import *
from database import *




public=Blueprint("public",__name__)

@public.route('/')
def home_page():
    return render_template('home.html')

@public.route('/login',methods=['get','post'])
def login():
    if 'login' in request.form:
        uname=request.form['uname']
        password=request.form['pwd']

        qry="select * from login where user_name='%s' and password ='%s'"%(uname,password)
        res=select(qry)

        if res:
            session['login_id']=res[0]['login_id']

            if res[0]['usertype']=='admin':
                return ("<script>alert('login successfull');window.location='/admin_home'</script>")
            
            if res[0]['usertype']=='seller':
                qrt="select * from seller where login_id='%s'"%(session['login_id'])
                res1=select(qrt)

                if res1:
                    session['seller_id']=res1[0]['seller_id']
                    session['oname']=res1[0]['seller_name']

                    print(session['seller_id'],"_________________")

                return ("<script>alert('login successfull');window.location='/sellers_home'</script>")
        
                        
            if res[0]['usertype']=='user':

                qrt="select * from user where login_id='%s'"%(session['login_id'])
                res2=select(qrt)

                if res2:
                    session['user_id']=res2[0]['user_id']
                    session['uname']=res2[0]['fname']

                return ("<script>alert('login successfull');window.location='/users_home'</script>")
            
        else:
            return ("<script>alert('Invalid Username or Password ');window.location='/login'</script>")

    return render_template('login.html')




@public.route('/public_user_registration',methods=['get','post'])
def public_user_registration():
    if 'add' in request.form:
        username = request.form['uname']
        
        # Check username availability again before insert
        qry_check = "SELECT * FROM login WHERE user_name='%s'" % username
        res_check = select(qry_check)
        
        if len(res_check) > 0:
            return "<script>alert('Username already exists');window.location='/user_register'</script>"

        # Rest of your existing registration code
        fname = request.form['fname']
        lname = request.form['lname']
        place = request.form['place']
        phone = request.form['phone']
        email = request.form['mail']
        password = request.form['pwd']

        qry = "insert into login values(null,'%s','%s','user')" % (username, password)
        res = insert(qry)

        qry1 = "insert into user values(null,'%s','%s','%s','%s','%s','%s')" % (
            res, fname, lname, place, phone, email)
        res1 = insert(qry1)

        return "<script>alert('Register successful');window.location='/login'</script>"
    

    return render_template('public_user_registration.html')




@public.route('/public_seller_registration',methods=['get','post'])
def public_seller_registration():
    if 'add' in request.form:
        username = request.form['uname']
        
        # Check username availability again before insert
        qry_check = "SELECT * FROM login WHERE user_name='%s'" % username
        res_check = select(qry_check)
        
        if len(res_check) > 0:
            return "<script>alert('Username already exists');window.location='/user_register'</script>"

        # Rest of your existing registration code
        fname = request.form['fname']
        license = request.form['lname']
        place = request.form['place']
        phone = request.form['phone']
        email = request.form['mail']
        password = request.form['pwd']

        qry = "insert into login values(null,'%s','%s','pending')" % (username, password)
        res = insert(qry)

        qry1 = "insert into seller values(null,'%s','%s','%s','%s','%s','%s')" % (
            res, fname, place, phone, email,license)
        res1 = insert(qry1)

        return "<script>alert('Register successful');window.location='/login'</script>"
    

    return render_template('public_seller_registration.html')



# Add this new route to check username availability
@public.route('/check_username', methods=['POST'])
def check_username():
    username = request.form['username']
    
    # Query to check if username exists
    qry = "SELECT * FROM login WHERE user_name='%s'" % username
    res = select(qry)
    
    # Return JSON response
    return jsonify({'available': len(res) == 0})