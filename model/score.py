from google.appengine.ext import ndb

from team import Team


class Score(ndb.Model):
    time = ndb.DateTimeProperty(auto_now_add=True)
    id = ndb.IntegerProperty(indexed=True)
    team1_abbr = ndb.StringProperty(required=True)
    team2_abbr = ndb.StringProperty(required=True)
    team1_score = ndb.IntegerProperty()
    team2_score = ndb.IntegerProperty()
    team1 = ndb.KeyProperty(kind=Team)
    team2 = ndb.KeyProperty(kind=Team)

    @staticmethod
    def recupera_team_para(req):
        try:
            id_team = req.GET["id"]
        except KeyError:
            id_team = ""

        if id_team:
            clave_team = ndb.Key(urlsafe=id_team)
            return clave_team.get()
        else:
            print("ERROR: equipo no encontrado")

    @staticmethod
    def recupera_scores_team(abrv):
        scores = Score.query(ndb.OR(Score.team1_abbr == abrv, Score.team2_abbr == abrv))
        return scores

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()