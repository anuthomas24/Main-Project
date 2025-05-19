
from flask import *
from public import public
from admin import admin
from sellers import sellers
from users import users

app=Flask(__name__)

app.secret_key="sdfgh"


app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(sellers)
app.register_blueprint(users)



app.run(debug=True,port=5007)




