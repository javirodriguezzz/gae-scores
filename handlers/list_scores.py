import webapp2
from webapp2_extras import jinja2

from model.score import Score


class ScoresListHandler(webapp2.RequestHandler):
    def get(self):
        team = Score.recupera_team_para(self.request)
        scores = Score.recupera_scores_team(team.abbreviation)

        valores_plantilla = {
            "scores": scores,
            "team": team
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("scores_list.html",
                                  **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/teams/scores', ScoresListHandler)
], debug=True)