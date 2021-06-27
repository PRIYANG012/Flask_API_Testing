from config import app, logger, db, bcrypt, jwtmanager

from flask import request, jsonify
from flask_restful import Resource
from sqlalchemy import Column, Integer, String, Text

from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

import datetime

class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(Text, nullable=False)
    


    def get_user_by_email(self, email):
        user = User.query.filter_by(email=email).first()
        return user

    

class UserRegistration(Resource):

   

    def post(self):
        try:

            data = request.json

            user = User()

            if user.get_user_by_email(data["email"]):
                return {
                    "msg": "Email already registered"
                }, 400

            else:
                # print(data['email'])
                user.first_name = data['first_name']
                user.last_name = data['last_name']
                user.username = data['username']
                user.email = data['email']
                password = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
                user.password = password
                db.session.add(user)
                db.session.commit()

                return {
                    "msg": "User created"
                }, 201

        except Exception as e:
            logger.exception(e)
            return {
                "msg": "Internal Error"
            }, 500


class UserLogin(Resource):

    def post(self):
        data = request.json

        user = User().get_user_by_email(email=data["email"])

        if user:
            if bcrypt.check_password_hash(user.password, data["password"]):
                
                expires = datetime.timedelta(days=365)

                access_token = create_access_token(
                    identity={
                        "email": str(user.email)
                    },
                    expires_delta=expires
                )

                return {
                    "msg": "Logged in successfully",
                    "token": access_token,
                    "user":user.first_name +" "+ user.last_name 
                }, 200
                
            else:
                return {
                    "msg": "Invalid Password"
                }, 401
        else:
            return {
                "msg": "Not Found"
            }, 404



class GetUserbyEmail(Resource):

    @jwt_required
    def post(self):
        try:

            data = request.json

            user = User().get_user_by_email(email=data["email"])

            if user:
                return {
                    "first_name":user.first_name,
                    "last_name":user.last_name,
                    "username":user.username
                }, 400

            else:
               
                return {
                    "msg": "user not exist"
                   
                }, 201
        
        except Exception as e:
            logger.exception(e)
            return {
                "msg": "Internal Error"
            }, 500
