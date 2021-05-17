from google.appengine.ext import ndb

from score import Score


class Comment(ndb.Model):
    author = ndb.StringProperty(required=True, indexed=True)
    text = ndb.TextProperty()
    creation_date = ndb.DateTimeProperty(auto_now_add=True)
    score = ndb.KeyProperty(kind=Score)

    @staticmethod
    def recupera_para(req):
        try:
            id_score = req.GET["score"]
        except KeyError:
            id_score = ""

        if id_score:
            clave_score = ndb.Key(urlsafe=id_score)
            comments = Comment.query(clave_score == Comment.score)
            return clave_score.get(), comments
        else:
            print("ERROR: score no encontrada")
