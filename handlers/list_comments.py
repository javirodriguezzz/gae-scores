import webapp2
from webapp2_extras import jinja2

from model.comment import Comment


class CommentsListHandler(webapp2.RequestHandler):
    def get(self):
        score, comments = Comment.recupera_para(self.request)

        valores_plantilla = {
            "score": score,
            "comments": comments
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("comments_list.html",
                                  **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/scores/comments', CommentsListHandler)
], debug=True)
