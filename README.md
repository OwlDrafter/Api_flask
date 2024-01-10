Создать пользователя:
curl -X POST -H "Content-Type: application/json" \
-d '{"username":"Baldurusgate3_doe","email":"baldurus.gate3@example.com"}' http://localhost:5000/users

Получение списка всех пользователей:
curl http://localhost:5000/users

Получение пользователей по ID:
curl http://localhost:5000/users/1

Удаление пользователя по ID:
curl -X DELETE http://localhost:5000/users/1

Создание постов:
curl -X POST -H "Content-Type: application/json" \
-d '{"title":"First Post","content":"Hello, world!","author_id":1}' http://localhost:5000/posts

Получение списка постов:
curl http://localhost:5000/posts

Получение поста по ID:
curl http://localhost:5000/posts/1

Удаление поста по ID:
curl -X DELETE http://localhost:5000/posts/1


Сделал на Postman
