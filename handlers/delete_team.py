import webapp2
import time

from model.team import Team


class DeleteTeamHandler(webapp2.RequestHandler):
    def get(self):
        team = Team.recupera(self.request)
        team.key.delete()
        time.sleep(1)
        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/teams/delete', DeleteTeamHandler)
], debug=True)