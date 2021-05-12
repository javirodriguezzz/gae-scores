#!/usr/bin/env python
#
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.score import Score
from model.team import Team
import time


class NewTeamHandler(webapp2.RequestHandler):
    def get(self):

        templates_val = {
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("new_team.html", **templates_val))

    def post(self):
        str_id = self.request.get("edId", "")
        creation_date = False

        str_name = self.request.get("edName", "")
        str_abbreviation = self.request.get("edAbbreviation", "")
        str_description = self.request.get("edDescription", "")
        str_creation_date = self.request.get("edCreationDate", "")

        usr = users.get_current_user()
        nick = "no especificado"

        if usr:
            nick = usr.nickname()
            # nick = usr.email()
            # nick = usr.user_id()
            # users.is_current_user_admin()

        try:
            creation_date = int(str_creation_date)
        except ValueError:
            creation_date = -1

        if creation_date < 0:
            return self.redirect("/")
        else:
            team = Team(name=str_name,
                        abbreviation=str_abbreviation,
                        description=str_description,
                        creation_date=creation_date)

            team.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/teams/new', NewTeamHandler)
], debug=True)