from flask import *
from database import *



admin=Blueprint("admin",__name__)



@admin.route('/admin_home')
def admin_home():
    return render_template("admin_home.html")



@admin.route('/admin_view_sellers')
def admin_view_sellers():
    data={}

    qry="SELECT * FROM login INNER JOIN seller USING(login_id)"
    res=select(qry)
    data['view']=res

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None

    if action=='accept':
        qrty="update login set usertype='seller' where login_id='%s'"%(id)
        update(qrty)
        return ("<script>alert('Accept successfull');window.location='/admin_view_sellers'</script>")


    if action=='reject':
        qrty1="update login set usertype='pending' where login_id='%s'"%(id)
        update(qrty1)

        return ("<script>alert('Reject successfull');window.location='/admin_view_sellers'</script>")

    return render_template('admin_view_sellers.html',data=data)



@admin.route('/admin_view_complaints')
def admin_view_complaints():

    data={}

    qry="select * from complaints"
    res=select(qry)
    data['complaints']=res


    return render_template("admin_view_complaints.html",data=data)


@admin.route('/admin_send_reply',methods=['get','post'])
def admin_send_reply():
    id=request.args['id']

    if 'send' in request.form:

        Reply=request.form['rep']

        qry="update complaints set reply='%s' where complaints_id='%s'"%(Reply,id)
        update(qry)

        return ("<script>alert('Send successfull');window.location='/admin_view_complaints'</script>")


    return render_template("admin_send_reply.html")




@admin.route("/admin_view_customers")
def admin_view_customers():
    data={}

    qry="select * from user"
    res=select(qry)
    data['view']=res

    return render_template('admin_view_customers.html',data=data)



@admin.route('/admin_manage_category',methods=['get','post'])
def admin_manage_category():
    data={}

    qry="select * from category"
    res=select(qry)
    data['category']=res


    if  'add'  in request.form:
        category_name=request.form['cat']


        qrt="insert into category values(null,'%s')"%(category_name)
        res=insert(qrt)

        return ("<script>alert('Add successfull');window.location='/admin_home'</script>")
    
    if  'action' in request.args:
        id=request.args['id']
        action=request.args['action']

    else:
        action=None

    if  action=='update':

        qryup="select * from category where category_id='%s'"%(id)
        resup=select(qryup)
        data['up']=resup

    if  'up'  in request.form:
        category_name=request.form['cat']


        qry="update category set category_name='%s' where  category_id='%s'"%(category_name,id)
        res=update(qry)
        return ("<script>alert('Update successfull');window.location='/admin_manage_category'</script>")
    
    if  action=='delete':

        qrydel="delete from category where category_id='%s'"%(id)
        res=delete(qrydel)

        return ("<script>alert('Delete successfull');window.location='/admin_manage_category'</script>")


    return render_template('admin_manage_category.html',data=data)