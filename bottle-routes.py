from axway_droid import axwaydroid_reply, axwaydroid_msg, axwaydroid_swagger, axwaydroid_users

@route('/axwaydroid/swagger')
def axswg():
    out = axwaydroid_swagger()
    return out

@post('/axwaydroid/reply')
def axreply():
    out = axwaydroid_reply(request.json)
    return out

@route('/axwaydroid/users')
def axmsg():
    out = axwaydroid_users()
    return out

@route('/axwaydroid/msg')
def axmsg():
    out = axwaydroid_msg(request.query)
    return out

