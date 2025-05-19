from datetime import date
from flask import *
from database import *
from blk import *



users=Blueprint("users",__name__)



@users.route('/users_home')
def users_home():
    return render_template("users_home.html")



@users.route('/user_view_shops')
def user_view_shops():
    data={}

    qry="select * from seller"
    res=select(qry)
    data["seller"]=res

    return render_template('user_view_shops.html',data=data)




@users.route('/user_chat_sellers',methods=['get','post'])
def user_chat_sellers():
    id=request.args['id']
    t="select * from seller where seller_id='%s'"%(id)
    tr=select(t)
    pname=tr[0]['seller_name']
    pid=tr[0]['login_id']
    cht={}

    dname=session['uname']

    s="SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' UNION SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' ORDER BY date,time"%(session['login_id'],pid,pid,session['login_id'])
    se=select(s)
    cht['view']=se

    if "submit" in request.form:
        print("#################################################################################################")
        msg=request.form['msg']
        c="insert into chat values(null,'%s','user','%s','seller','%s',curdate(),curtime())"%(session['login_id'],pid,msg)
        insert(c)
        return redirect(url_for('users.user_chat_sellers',id=id))
    

    return render_template('user_chat_sellers.html',cht=cht,dname=dname,pname=pname)



@users.route('/users_view_products',methods=['get','post'])
def users_view_products():
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
                    res.append(decoded_input[1])
    except Exception as e:
        print("", e)
    data['product'] = res

    print(res,")))))))))))))))))))))))))))))))))))0")

    if  'ser' in request.form:
        search=request.form['search']
        
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
                    if int(decoded_input[1]['product_name']) == search:
                        res.append(decoded_input[1])
        except Exception as e:
            print("", e)
        data['product'] = res

        print(res,"lllllllllllllllllllllllllllllllllllllllllllllllll")
 

    return render_template('users_view_products.html',data=data)

 

@users.route("/users_send_complaints",methods=['get','post'])
def  users_send_complaints():
    data={}

    qry1="select * from complaints where sender_id='%s'"%(session['login_id'])
    res=select(qry1)
    data['complaints']=res

    if 'send' in request.form:
        title=request.form['title']
        complaimnts=request.form['comp']

        qry="insert into complaints values (null,'%s','%s','%s','pending',curdate())"%(session['login_id'],title,complaimnts)
        insert(qry)

        return ("<script>alert('Send  successfull');window.location='/users_home'</script>")

    return render_template('users_send_complaints.html',data=data)


@users.route('/user_buy_product')
def user_buy_product():
    id=request.args['id']

    qry="insert into orders values(null,'%s','%s',curdate(),'pending')"%(session['user_id'],id)
    res=insert(qry)

    return ("<script>alert('Orderd  successfull');window.location='/users_home'</script>")



@users.route('/users_view_orderd_products')
def users_view_orderd_products():
    data={}

    qry="SELECT * FROM  orders INNER JOIN  product  USING(product_id) WHERE  orders.user_id='%s'"%(session['user_id'])
    res=select(qry)
    data['view']=res

    return render_template('users_view_orderd_products.html',data=data)


@users.route('/user_make_payments',methods=['get','post'])
def  user_make_payments():
    data={}

    id=request.args['id']
    amt=request.args['amt']
    data['view']=amt


    if 'add' in request.form:
        amt=request.form['amt']

        qrup="update orders set status='paid' where order_id='%s'"%(id)
        update(qrup)

        qry="insert payment values (null,'%s','%s',curdate(),'paid')"%(id,amt)
        res=insert(qry)

        return ("<script>alert('Pay  successfull');window.location='/users_home'</script>")


    return render_template('user_make_payments.html',data=data)


@users.route('/user_view_orders_history')
def user_view_orders_history():
    data={}

    qry="SELECT * FROM  orders INNER JOIN  product  USING(product_id) WHERE  orders.user_id='%s' and orders.status='paid'"%(session['user_id'])
    res=select(qry)
    data['view']=res

    return render_template('user_view_orders_history.html',data=data)


@users.route('/user_add_rating',methods=['get','post'])
def user_add_rating():
    id=request.args['id']

    if 'add' in request.form:
        rating=request.form['rate']
        review=request.form['review']

        qry="insert into rating values(null,'%s','%s','%s','%s',curdate())"%(session['user_id'],id,rating,review)
        res=insert(qry)

        return ("<script>alert('Add  successfull');window.location='/users_home'</script>")

    return render_template('user_add_rating.html')



@users.route('/user_view_auction')
def user_view_auction():
    data={}
    
    current_date = date.today().strftime('%Y-%m-%d')
    
    qry="select * from auction "
    res=select(qry)
    data['view']=res


    return render_template('user_view_auction.html',data=data,current_date=current_date)



# @users.route('/users_bid_amount',methods=['get','post'])
# def users_bid_amount():
#     data={}

#     id=request.args['id']

#     qry="select * from auction inner join bid using(auction_id)"
#     res=select(qry)
#     data['view']=res
#     # amt=res[0]['base_amount']



#     if 'send' in request.form:
#         amt=request.form['amt']

#         qry="insert into bid values(null,'%s','%s','%s',curdate())"%(id,session['user_id'],amt)
#         res=insert(qry)

#         return ("<script>alert('Add  successfull');window.location='/user_view_auction'</script>")

#     return render_template('users_bid_amount.html',data=data)


@users.route('/users_bid_amount', methods=['GET', 'POST'])
def users_bid_amount():
    data = {}
    id = request.args['id']

    # First, get the auction details to ensure we have the base amount
    auction_qry = "SELECT * FROM auction WHERE auction_id = '%s'" % id
    auction_res = select(auction_qry)
    
    if not auction_res:
        return "<script>alert('Auction not found'); window.location='/user_view_auction'</script>"

    # Check if there are any existing bids for this auction
    bid_qry = "SELECT * FROM bid WHERE auction_id = '%s'" % id
    bid_res = select(bid_qry)

    # If no bids exist yet, create a view with just the auction details
    if not bid_res:
        # Modify the auction result to match the expected structure
        auction_res[0]['amount'] = ''  # No bid amount yet
        auction_res[0]['date'] = ''    # No bid date yet
        auction_res[0]['status'] = 'Pending'
        data['view'] = auction_res
    else:
        # If bids exist, proceed with the original query
        full_qry = "SELECT * FROM auction INNER JOIN bid USING(auction_id) WHERE auction_id = '%s'" % id
        res = select(full_qry)
        data['view'] = res

    # Handle bid submission
    if 'send' in request.form:
        amt = request.form['amt']
        base_amount = auction_res[0]['base_amount']

        # Validate bid amount
        if float(amt) < float(base_amount):
            return f"<script>alert('Bid amount must be at least {base_amount}'); window.location='/users_bid_amount?id={id}'</script>"

        # Insert new bid
        insert_qry = "INSERT INTO bid VALUES(NULL, '%s', '%s', '%s', now())" % (id, session['user_id'], amt)
        insert(insert_qry)

        return "<script>alert('Bid successful'); window.location='/user_view_auction'</script>"

    return render_template('users_bid_amount.html', data=data)



@users.route('/users_view_result')
def users_view_result():
    data={}
    id=request.args['id']


    qry="select * from auction_result where auction_id='%s'"%(id)
    res=select(qry)
    data['view']=res


    return render_template('users_view_result.html',data=data)