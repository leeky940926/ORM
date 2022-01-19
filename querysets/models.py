from django.db import models

class User(models.Model) :
    email = models.EmailField(max_length=50, unique=True)
    
    class Meta :
        db_table = 'users'

class Author(models.Model) :
    name = models.CharField(max_length=50)
    
    class Meta :
        db_table = 'authors'

class Book(models.Model) :
    name         = models.CharField(max_length=50)
    publish_date = models.DateField()
    author       = models.ManyToManyField(Author,related_name='author', through='querysets.BookAuthor')
    
    class Meta :
        db_table = 'books'

class BookAuthor(models.Model) :
    book   = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    class Meta :
        db_table = 'books_authors'

class Reply(models.Model) :
    email      = models.OneToOneField(User, db_column='email', on_delete=models.CASCADE)
    book       = models.ForeignKey(Book, on_delete=models.CASCADE)
    contets    = models.TextField()
    write_time = models.DateTimeField()
    
    class Meta :
        db_table = 'replies'

class Rating(models.Model) :
    book   = models.ForeignKey(Book, on_delete=models.CASCADE)
    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    
    class Meta : 
        db_table = 'ratings'