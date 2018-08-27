import logging, sys
from datetime import datetime
from random import randint
import requests, json, redis
from bottle import response
from rnames import random_username

redis_host = "redis-XXX.YYY.us-east-1-2.ec2.cloud.redislabs.com"
redis_port = XXXXXXX
redis_auth = "XXXXXXXXXXXXXXXXXX"

def axwaydroid_swagger():

    swagger="""{
  "swagger" : "2.0",
  "host" : "__HOST__",
  "basePath" : "/axwaydroid",
  "schemes" : [ "http" ],
  "paths" : {
    "/reply" : {
      "post" : {
        "description" : "",
        "operationId" : "reply_to_message",
        "summary" : "Reply to an incoming message. This method will only be used by the LINE API Webhook.",
        "consumes" : [ "application/json" ],
        "responses" : {
          "200" : {
            "description" : "OK"
          }
        }
      }
    },
    "/users" : {
      "get" : {
        "description" : "",
        "operationId" : "get_users",
        "summary" : "Get a list of usernames that are registered with the Axway LINE Droid",
        "produces" : [ "application/json" ],
        "responses" : {
          "200" : {
            "description" : "OK"
          }
        }
      }
    },
    "/msg" : {
      "get" : {
        "description" : "",
        "operationId" : "send_message",
        "summary" : "Send a message to a user",
        "parameters" : [ {
          "description" : "The message you'd like to send",
          "required" : true,
          "in" : "query",
          "name" : "message",
          "type" : "string"
        }, {
          "description" : "The user who should receive the message",
          "required" : true,
          "in" : "query",
          "name" : "user",
          "type" : "string"
        } ],
        "responses" : {
          "200" : {
            "description" : "OK"
          },
          "404" : {
            "description" : "User not found"
          }
        }
      }
    }
  },
  "info" : {
    "title" : "Axway LINE Droid",
    "description" : "",
    "version" : "1.0",
    "description" : "An API to interact with the Axway LINE Droid. QR Code: http://bit.ly/axwaydroidqr"
  }
}"""
    response.content_type = 'application/json'
    return swagger

def axwaydroid_users():

    rc = redis.StrictRedis(host=redis_host, port=redis_port, db=0, password=redis_auth)

    return( dict(  {"users": rc.lrange("username_list", 0, -1) }  ))

def axwaydroid_msg(request_query):

    try:
        msg = request_query['message']
    except:
        msg = "test message"

    try:
        user = request_query['user']
    except:
        response.status = 500

        return dict( {"message": "error - please specify user id"})

    rc = redis.StrictRedis(host=redis_host, port=redis_port, db=0, password=redis_auth)

    receiver = rc.get(user)

    if receiver == None:
        response.status = 404
        response.content_type = 'application/json'

        return dict( {"message": "error - no such user id"})


    # Access Token for the Bot
    access_token = "XYZ"



    url = "https://api.line.me/v2/bot/message/push"

    payload = "{\"to\":\"" + receiver + "\", \"messages\":[{\"type\":\"text\", \"text\":\"" + msg + "\"}]}"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + access_token,
        'Cache-Control': "no-cache"
        }

    response_txt = requests.request("POST", url, data=payload, headers=headers)

    return "OK"


def axwaydroid_reply(request_json):

    # Access Token for the Bot
    access_token = "XYZ"

    # Set up Logging
    logger = logging.getLogger('axway')
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler('axway.log')
    formatter = logging.Formatter('%(msg)s')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Capture JSON
    line_json = request_json

    # Get Message and replyToken
    line_token = line_json["events"][0]["replyToken"]
    line_msg = line_json["events"][0]["message"]["text"]
    line_user = line_json["events"][0]["source"]["userId"]

    # Log the info
    logger.info(str(datetime.now()) + " Message: " + line_msg + " User: " + line_user + " Token: " + line_token + " JSON: " + json.dumps(request_json))

    rc = redis.StrictRedis(host=redis_host, port=redis_port, db=0, password=redis_auth)

    existing_users = rc.lrange("line_id_list", 0, -1)

    if line_user in existing_users:
        username = rc.get(line_user)

        addstr = "You're already on my list as '" + username + "'. I'll ping you if I have any updates for you!"
    else:
        new_username = random_username()
        addstr = "I don't have your ID in my list, will add you as '" + new_username + "'"
        rc.lpush("line_id_list", line_user)
        rc.lpush("username_list", new_username)
        rc.set(line_user, new_username)
        rc.set(new_username, line_user)

    # Post reply to LINE
    endpoint = "https://api.line.me/v2/bot/message/reply"
    send_text = "Your friendly Axway Droid here! " + addstr
    payload = "{\n    \"replyToken\":\"" + line_token + "\",\n    \"messages\":[\n        {\n            \"type\":\"text\",\n            \"text\":\"" + send_text + "\"\n        }\n    ]\n}"
    headers = {
    'Content-Type': "application/json", 'Authorization': "Bearer " + access_token, 'Cache-Control': "no-cache"}

    response = requests.request("POST", endpoint, data=payload, headers=headers)

    return 'OK'
