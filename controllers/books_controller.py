from models.Book import Book
from main import db
from flask import Blueprint, request, jsonify
from schemas.BookSchema import books_schema
books = Blueprint("books", __name__, url_prefix="/books")


@books.route("/", methods=["GET"])
def book_index():
    #Return all books
    books = Book.query.all()
    serialised_data = books_schema.dump(books)
    return jsonify(serialised_data)

    # books_list = []
    # for book in books:
    #     books_list.append({
    #         "id" : book.id,
    #         "title" : book.title
    #     })

    # raw_data = [
    #     {
    #     "id": 1,
    #     "title": "New title"
    #     },
    #     {
    #     "id": 2,
    #     "title": "testing"
    #     },
    #     {
    #     "id": 3,
    #     "title": "ABC"
    #     }
    #     ]
    
    # for book in raw_data:
    #     new_book = Book()
    #     new_book.id = book["id"]
    #     new_book.title = book["title"]
    #     books_list.append(new_book)

    

# @books.route("/", methods=["POST"])
# def book_create():
#     #Create a new book
#     sql = "INSERT INTO books (title) VALUES (%s);"
#     cursor.execute(sql, (request.json["title"],))
#     connection.commit()

#     sql = "SELECT * FROM books ORDER BY ID DESC LIMIT 1"
#     cursor.execute(sql)
#     book = cursor.fetchone()
#     return jsonify(book)

# @books.route("/<int:id>", methods=["GET"])
# def book_show(id):
#     #Return a single book
#     sql = "SELECT * FROM books WHERE id = %s;"
#     cursor.execute(sql, (id,))
#     book = cursor.fetchone()
#     return jsonify(book)

# @books.route("/<int:id>", methods=["PUT", "PATCH"])
# def book_update(id):
#     #Update a book
#     sql = "UPDATE books SET title = %s WHERE id = %s;"
#     cursor.execute(sql, (request.json["title"], id))
#     connection.commit()

#     sql = "SELECT * FROM books WHERE id = %s"
#     cursor.execute(sql, (id,))
#     book = cursor.fetchone()
#     return jsonify(book)

# @books.route("/<int:id>", methods=["DELETE"])
# def book_delete(id):
#     sql = "SELECT * FROM books WHERE id = %s;"
#     cursor.execute(sql, (id,))
#     book = cursor.fetchone()
    
#     if book:
#         sql = "DELETE FROM books WHERE id = %s;"
#         cursor.execute(sql, (id,))
#         connection.commit()

#     return jsonify(book)