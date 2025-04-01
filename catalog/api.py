from datetime import date

from django.shortcuts import get_object_or_404
from catalog.models import Author, Genre, Language
from ninja import Schema
from ninja import UploadedFile, File

class AuthorIn(Schema):
    first_name: str
    last_name: str
    date_of_birth: date = None
    date_of_death: date = None


class AuthorOut(Schema):
    id: int
    first_name: str
    last_name: str
    date_of_birth: date = None
    date_of_death: date = None


@api.post("/author")
def create_author(request, payload: AuthorIn):
    author = Author.objects.create(**payload.dict())
    return {"id": author.id}


@api.get("/authors/{author_id}", response=AuthorOut)
def get_author(request, author_id: int):
   author = get_object_or_404(Author, id=author_id)
   return author

@api.put("/authors/{author_id}")
def update_author(request, author_id: int, payload: AuthorIn):
    author = get_object_or_404(Author, id=author_id)
    for attr, value in payload.dict().items():
        setattr(author, attr, value)
    author.save()
    return {"success": True}

@api.delete("/authors/{author_id}")
def delete_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    author.delete()
    return {"success": True}


class GenreIn(Schema):
    name: str


class GenreOut(Schema):
    name: str


@api.post("/genre")
def create_genre(request, payload: GenreIn):
    genre = Genre.objects.create(**payload.dict())
    return {"name": genre.name}


@api.get("/genres/{genre_id}", response=GenreOut)
def get_genre(request, genre_id: int):
   genre = get_object_or_404(Genre, id=genre_id)
   return genre

@api.put("/genres/{genre_id}")
def update_genre(request, genre_id: int, payload: GenreIn):
    genre = get_object_or_404(Genre, id=genre_id)
    for attr, value in payload.dict().items():
        setattr(genre, attr, value)
    genre.save()
    return {"success": True}

@api.delete("/genres/{genre_id}")
def delete_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.delete()
    return {"success": True}


class LanguageIn(Schema):
    name: str


class LanguageOut(Schema):
    name: str


@api.post("/language")
def create_language(request, payload: LanguageIn):
    language = Language.objects.create(**payload.dict())
    return {"id": language.id}


@api.get("/language/{language_id}", response=LanguageOut)
def get_language(request, language_id: int):
   language = get_object_or_404(Language, id=language_id)
   return language

@api.put("/languages/{language_id}")
def update_language(request, language_id: int, payload: LanguageIn):
    language = get_object_or_404(Language, id=language_id)
    for attr, value in payload.dict().items():
        setattr(language, attr, value)
    language.save()
    return {"success": True}

@api.delete("/languages/{language_id}")
def delete_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    language.delete()
    return {"success": True}
