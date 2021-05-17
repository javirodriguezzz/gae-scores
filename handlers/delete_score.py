import webapp2
import time

from model.score import Score


class DeleteScoreHandler(webapp2.RequestHandler):
    def get(self):
        score = Score.recupera(self.request)
        score.key.delete()
        time.sleep(1)
        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/scores/delete', DeleteScoreHandler)
], debug=True)