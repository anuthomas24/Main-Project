

from datetime import date
import uuid
from flask import *
from database import *
from blk import *


sellers=Blueprint("sellers",__name__)



@sellers.route('/sellers_home')
def sellers_home():
    return render_template("sellers_home.html")



@sellers.route('/sellers_view_category')
def sellers_view_category():
    data={}

    qry="select * from category"
    res=select(qry)
    data["category"]=res
    return render_template("sellers_view_category.html",data=data)



@sellers.route('/seller_add_product',methods=['get','post'])
def seller_add_product():
    data={}

    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    res = []
    try:
        for i in range(blocknumber, 0, -1):
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input, "///////////////////")
            if str(decoded_input[0]) == "<Function add_product(uint256,uint256,uint256,string,string,string,string)>":
                if int(decoded_input[1]['seller_id']) == int(session['seller_id']):
                    res.append(decoded_input[1])
    except Exception as e:
        print("", e)
    data['product'] = res


    cid=request.args['id']

 
    if 'add'  in request.form:

        pname=request.form['pname']
        description=request.form['desc']
        images=request.files['image']
        amt=request.form['amt']


        path = 'static/product_images/' + str(uuid.uuid4()) + images.filename
        images.save(path)

        qry="insert into product values(null,'%s','%s','%s','%s','%s','%s')"%(cid,session['seller_id'],pname,amt,description,path)
        res=insert(qry)

        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
        id=web3.eth.get_block_number()
        message = contract.functions.add_product(int(id),int(cid),int(session['seller_id']),pname,amt,description,path).transact()
        print(message)

        
        return ("<script>alert('Add successfull');window.location='/sellers_home'</script>")

    # if  'action' in request.args:
    #     id=request.args['id']
    #     action=request.args['action']

    # else:
    #     action=None

    # if  action=='update':

    #     qryup="select * from product where product_id='%s'"%(id)
    #     resup=select(qryup)
    #     data['up']=resup

    # if  'up'  in request.form:

    #     pname=request.form['pname']
    #     description=request.form['desc']
    #     images=request.files['image']
    #     amt=request.form['amt']


    #     path = 'static/product_images/' + str(uuid.uuid4()) + images.filename
    #     images.save(path)

    #     qry="update product set product_name='%s',amount='%s',description='%s',image='%s' where  product_id='%s'"%(pname,amt,description,path,id)
    #     res=update(qry)

    #     return ("<script>alert('Update successfull');window.location='/sellers_home'</script>")
    
    # if  action=='delete':

    #     qrydel="delete from product where product_id='%s'"%(id)
    #     res=delete(qrydel)

    #     return ("<script>alert('Delete successfull');window.location='/sellers_home'</script>")

    return render_template('seller_add_product.html',data=data)




@sellers.route('/seller_add_products_images',methods=['get','post'])
def seller_add_products_images():
    id=request.args['id']

    data={}

    qry="select * from product_images where product_id='%s'"%(id)
    res=select(qry)
    data['images']=res



    if   'add'  in request.form:

        images=request.files['image']
        
        path = 'static/product_images/' + str(uuid.uuid4()) + images.filename
        images.save(path)

        qry="insert into product_images values(null,'%s','%s')"%(id,path)
        res=insert(qry)

        return ("<script>alert('Add successfull');window.location='/sellers_home'</script>")
    

    return render_template('seller_add_products_images.html',data=data)



@sellers.route('/sellers_view_rating_by_users')
def sellers_view_rating_by_users():
    data={}

    qry="SELECT * FROM rating INNER JOIN product USING (product_id) WHERE product.seller_id='%s'"%(session['seller_id'])
    res=select(qry)
    data['view']=res

    return render_template('sellers_view_rating_by_users.html',data=data)


@sellers.route('/sellers_view_products_orders')
def sellers_view_products_orders():
    data={}

    qry="SELECT * FROM  orders INNER JOIN  product  USING(product_id) WHERE product.seller_id='%s'"%(session['seller_id'])
    res=select(qry)
    data['view']=res

    return render_template('sellers_view_products_orders.html',data=data)

@sellers.route('/seller_view_payments')
def seller_view_payments():
    id=request.args['id']
    
    data={}
    qry="select * from payment where order_id='%s'"%(id)
    res=select(qry)
    data['view']=res

    return render_template('seller_view_payments.html',data=data)



@sellers.route('/sellers_manage_auction',methods=['get','post'])
def sellers_manage_auction():
    data={}

    qry1="select * from auction where seller_id='%s'"%(session['seller_id'])
    res=select(qry1)
    data['view']=res
    
    if 'add'  in request.form:
    
        pname=request.form['pname']
        description=request.form['desc']
        images=request.files['image']
        amt=request.form['amt']
        dates=request.form['dates']

        path = 'static/product_images/' + str(uuid.uuid4()) + images.filename
        images.save(path)

        qry="insert into auction values(null,'%s','%s','%s','%s','%s',curdate(),'%s','0','pending')"%(session['seller_id'],pname,path,description,amt,dates)
        res=insert(qry)

        return ("<script>alert('Add successfull');window.location='/sellers_home'</script>")

    return render_template('sellers_manage_auction.html',data=data)




@sellers.route('/sellers_view_auction',methods=['get','post'])
def sellers_view_auction():
    data={}

    current_date = date.today().strftime('%Y-%m-%d')
    
    qry1="select * from auction inner join bid using(auction_id) where seller_id='%s'"%(session['seller_id'])
    res=select(qry1)
    data['view']=res
    
    return render_template('sellers_view_auction.html',data=data,current_date=current_date)



@sellers.route('/auction_finish')
def auction_finish():
    aid=request.args['aid']
    bid=request.args['bid']


    qrt="SELECT user_id, MAX(amount) AS max_bid FROM bid  WHERE auction_id = '%s' GROUP BY user_id ORDER BY max_bid DESC LIMIT 1 "%(aid)
    ress=select(qrt)
    wid=ress[0]['user_id']
    amt=ress[0]['max_bid']


    print(ress,"////////////////////////")


    qry1="update auction set status='Finished',winner_id='%s' where auction_id='%s'"%(wid,aid)
    res=update(qry1)


    qrt1="insert into auction_result values(null,'%s','%s','%s',curdate())"%(wid,aid,amt)
    insert(qrt1)


    
    return ("<script>alert('Auction Finish successfull');window.location='/sellers_home'</script>")




@sellers.route('/sellers_view_result')
def sellers_view_result():
    data={}

    id=request.args['id']

    qry="select * from auction_result where auction_id='%s'"%(id)
    res=select(qry)
    data['view']=res

    return render_template('sellers_view_result.html',data=data)


@sellers.route('/sellers_view_users')
def sellers_view_users():
    data={}
    id=request.args['id']

    qry="select * from user where user_id='%s'"%(id)
    res=select(qry)
    data['view']=res

    return render_template('sellers_view_users.html',data=data)


@sellers.route('/sellers_chat_user',methods=['get','post'])
def sellers_chat_user():
    pid=request.args['id']
    t="select * from user where login_id='%s'"%(pid)
    tr=select(t)
    pname=tr[0]['fname']
    cht={}
    dname=session['oname']
    s="SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' UNION SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' ORDER BY date,time"%(session['login_id'],pid,pid,session['login_id'])
    se=select(s)
    cht['view']=se
    
    if "submit" in request.form:
        print("#################################################################################################")
        msg=request.form['msg']
        c="insert into chat values(null,'%s','seller','%s','user','%s',curdate(),curtime())"%(session['login_id'],pid,msg)
        insert(c)
        return redirect(url_for('sellers.sellers_chat_user',id=pid))
      

    return render_template('sellers_chat_user.html',cht=cht,dname=dname,pname=pname)