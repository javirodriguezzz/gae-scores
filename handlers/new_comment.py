#!/usr/bin/env python
#
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from google.appengine.ext import ndb
import base64

from model.comment import Comment
import time


class NewCommentHandler(webapp2.RequestHandler):
    def get(self):

        templates_val = {
            "clave_score": self.request.GET["score"]
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("new_comment.html", **templates_val))

    def post(self):
        text = self.request.get("edText", "")
        clave_score = self.request.GET["score"]

        usr = users.get_current_user()
        nick = "no especificado"

        if usr:
            nick = usr.nickname()

        comment = Comment(author=nick, text=text,
                          score=ndb.Key(urlsafe=clave_score))
        comment.put()
        time.sleep(1)
        return self.redirect("/scores/comments?score="+clave_score)


app = webapp2.WSGIApplication([
    ('/comment/new', NewCommentHandler)
], debug=True)
