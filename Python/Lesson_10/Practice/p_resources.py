from flask_restful import Resource
from flask import request, jsonify
from p_models import Tag, Author, Publication
from p_schemas import TagSchema, AuthorSchema, PublicationSchema, ValidationError
from datetime import datetime


class TagResource(Resource):

    def get(self, tag_id=None):
        if tag_id:
            tag = Tag.objects.get(id=tag_id)
            posts = Publication.objects.filter(tags__contains=tag)

            tag = TagSchema().dump(tag)
            posts = PublicationSchema().dump(posts, many=True)

            json = {'tag': tag, 'posts': posts}
            return jsonify(json)
        elif not tag_id:
            tags = Tag.objects
            return TagSchema().dump(tags, many=True)

    def post(self):
        try:
            tag = TagSchema().load(request.get_json())
        except ValidationError as err:
            return str(err)
        return Tag.objects.create(**tag).save().to_json()

    def put(self, tag_id):
        pass

    def delete(self, tag_id):
        pass


class AuthorResource(Resource):

    def get(self, author_id=None):
        if author_id:
            author = Author.objects.get(id=author_id)
            posts_by_author = Publication.objects.filter(author=author_id)

            author = AuthorSchema().dump(author)
            posts_by_author = PublicationSchema(exclude=['author']). \
                dump(posts_by_author, many=True)

            json = {'author': author, 'posts': posts_by_author}
            return jsonify(json)
        elif not author_id:
            return AuthorSchema().dump(Author.objects, many=True)

    def post(self):
        try:
            author = AuthorSchema().load(request.get_json())
        except ValidationError as err:
            return str(err)
        return AuthorSchema().dump(Author.objects.create(**author).save())

    def put(self, author_id):
        pass

    def delete(self, author_id):
        pass


class PublicationResource(Resource):

    def get(self, publication_id=None):
        if publication_id:
            publication = Publication.objects.get(id=publication_id)
            publication.seen_by += 1
            publication.save()
            return PublicationSchema().dump(publication)
        elif not publication_id:
            return PublicationSchema().dump(Publication.objects, many=True)

    def post(self):
        publication = request.get_json()
        if 'date' not in publication:
            print("HELLO")
            publication['date'] = f"{str(datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))}.000000+00:00"
            print(str(publication['date']))
        try:
            publication = PublicationSchema().load(request.get_json())
        except ValidationError as err:
            return str(err)
        author = Author.objects.get(id=publication['author'])
        author.number_of_publications += 1
        author.save()
        return PublicationSchema().dump(Publication.objects.create(**publication).save())

    def put(self):
        pass

    def delete(self):
        pass
