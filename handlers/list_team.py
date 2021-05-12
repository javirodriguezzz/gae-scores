import webapp2
from webapp2_extras import jinja2

from model.team import Team


class TeamListHandler(webapp2.RequestHandler):
    def get(self):
        team = Team.recupera(self.request)

        valores_plantilla = {
            "team": team
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("team_list.html",
                                  **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/teams/list', TeamListHandler)
], debug=True)