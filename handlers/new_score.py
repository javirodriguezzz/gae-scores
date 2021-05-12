#!/usr/bin/env python
#
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.score import Score
from model.team import Team
import time


class NewScoreHandler(webapp2.RequestHandler):
    def get(self):

        templates_val = {
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("new_score.html", **templates_val))

    def post(self):
        str_id = self.request.get("edId", "")
        t1_score = False
        t2_score = False

        str_abbreviation_t1 = self.request.get("edAbbreviationT1", "")
        str_abbreviation_t2 = self.request.get("edAbbreviationT2", "")
        str_creation_date_t1 = self.request.get("edCreationDateT1", "")
        str_creation_date_t2 = self.request.get("edCreationDateT2", "")

        str_score_t1 = self.request.get("edScoreT1", "")
        str_score_t2 = self.request.get("edScoreT2", "")

        usr = users.get_current_user()
        nick = "no especificado"

        if usr:
            nick = usr.nickname()
            # nick = usr.email()
            # nick = usr.user_id()
            # users.is_current_user_admin()

        try:
            id = int(str_id)
            t1_score = int(str_score_t1)
            t2_score = int(str_score_t2)
        except ValueError:
            id = -1

        if id < 0:
            return self.redirect("/")
        else:
            score = Score(id=id, team1_abbr=str_abbreviation_t1, team2_abbr=str_abbreviation_t2, team1_score=t1_score,
                          team2_score=t2_score)
            score.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/scores/new', NewScoreHandler)
], debug=True)
