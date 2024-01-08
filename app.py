from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


users = {}
posts = {}


user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True, help='Username is required')
user_parser.add_argument('email', type=str, required=True, help='Email is required')

post_parser = reqparse.RequestParser()
post_parser.add_argument('title', type=str, required=True, help='Title is required')
post_parser.add_argument('content', type=str, required=True, help='Content is required')
post_parser.add_argument('author_id', type=int, required=True, help='Author ID is required')


class UserResource(Resource):
    def get(self, user_id):
        user = users.get(user_id)
        if user:
            return user, 200
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        if user_id in users:
            del users[user_id]
            return {'message': 'User deleted successfully'}, 200
        return {'message': 'User not found'}, 404


class UserListResource(Resource):
    def get(self):
        return users

    def post(self):
        args = user_parser.parse_args()
        user_id = len(users) + 1
        user = {'username': args['username'], 'email': args['email']}
        users[user_id] = user
        return {'message': 'User created successfully', 'user_id': user_id}, 201


class PostResource(Resource):
    def get(self, post_id):
        post = posts.get(post_id)
        if post:
            return post, 200
        return {'message': 'Post not found'}, 404

    def delete(self, post_id):
        if post_id in posts:
            del posts[post_id]
            return {'message': 'Post deleted successfully'}, 200
        return {'message': 'Post not found'}, 404


class PostListResource(Resource):
    def get(self):
        return posts

    def post(self):
        args = post_parser.parse_args()
        post_id = len(posts) + 1
        post = {'title': args['title'], 'content': args['content'], 'author_id': args['author_id']}
        posts[post_id] = post
        return {'message': 'Post created successfully', 'post_id': post_id}, 201


api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')

if __name__ == '__main__':
    app.run(debug=True)