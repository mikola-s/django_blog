from django.db import models
from django.db.models import Q, F, CheckConstraint
from django.contrib.auth.models import AbstractUser


def short_comment(text: str):
    """ short comment for verbose __str__() """
    return text if len(text) < 40 else f"{text[:21]}..."


def make_end_str(article, comment):
    """ for comments & expression __str__()"""
    if comment is not None:
        comment_to_comment = f"TO COMMENT {comment.id} " \
                             f"({comment.author}/{short_comment(comment.text)}) "
    else:
        comment_to_comment = ""
    comment_to_article = f"TO ARTICLE {article.id} ({article.author}/{article.title})"
    return f"{comment_to_comment}{comment_to_article}"


class Author(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    create_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.get_username()


class Article(models.Model):
    text = models.TextField(max_length=2048)
    title = models.CharField(max_length=256)
    post_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}/{self.title}"


class Comment(models.Model):
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    post_time = models.DateTimeField(auto_now_add=True)
    target = models.ForeignKey(to=Article, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        to='blog.Comment',
        on_delete=models.CASCADE,
        related_name='comments',
        null=True,
        blank=True,
    )

    def __str__(self):
        comment_from = f"COMMENT {self.id} ({self.author}/{short_comment(self.text)}) "
        return f"{comment_from}{make_end_str(self.target, self.comment)}"

    # class Meta: # пока не работает
    #     constraints = [
    #         CheckConstraint(
    #             check=Q(comment__isnull=False) & Q(comment__target__id__exact=F('target__id')),
    #             name='comments_to_right_articles')
    #     ]


class ExpressionType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Expression(models.Model):
    expression_type = models.ForeignKey(
        to=ExpressionType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    expressed = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
    )
    post_time = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(
        to=Comment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    article = models.ForeignKey(
        to=Article,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        expression_from = f"EXPRESSION {self.id} ({self.expression_type.name}/{self.expressed.username}) "
        return f"{expression_from}{make_end_str(self.article, self.comment)}"

    class Meta:
        unique_together = [('expressed', 'comment', 'article'), ]
