from config import app, api, logger

from resources.Users import UserRegistration, UserLogin,GetUserbyEmail

"""
    Routing
"""

api.add_resource(UserRegistration, '/api/add_user', endpoint='AddUser')
api.add_resource(UserLogin, '/api/login', endpoint='UserLogin')
api.add_resource(GetUserbyEmail, '/api/getuserbymail', endpoint='getuserbymail')



if __name__ == "__main__":
    app.run(debug=True)