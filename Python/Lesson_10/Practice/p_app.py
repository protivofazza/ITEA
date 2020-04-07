from flask import Flask
from flask_restful import Api
import p_resources
from p_models import Publication, Tag, Author


app = Flask(__name__)
api = Api(app)

api.add_resource(p_resources.TagResource, '/get_tags', '/get_tags/<tag_id>')
api.add_resource(p_resources.AuthorResource, '/get_authors', '/get_authors/<author_id>')
api.add_resource(p_resources.PublicationResource, '/get_publications', '/get_publications/<publication_id>')


if __name__ == '__main__':
    app.run(debug=True)