from main import ma
from models.Book import Book
from marshmallow.validate import Length
from schemas.UserSchema import UserSchema
class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book

    # add validation
    title = ma.String(required=True, validate=Length(min=1))
    user = ma.Nested(UserSchema)

book_schema = BookSchema()
books_schema = BookSchema(many=True)