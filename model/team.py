from google.appengine.ext import ndb


class Team(ndb.Model):
    name = ndb.StringProperty(required=True)
    abbreviation = ndb.StringProperty(required=True, indexed=True)
    description = ndb.TextProperty()
    creation_date = ndb.IntegerProperty()

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()
