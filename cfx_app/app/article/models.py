from app.article import db2
from app.authentication.models import UserDetails
from wtforms import DateField


class ArticleType(db2.Model):

    __tablename__ = 'article_type'

    id = db2.Column(db2.Integer, primary_key=True)
    name = db2.Column(db2.String(80), nullable=False)
    created_at = DateField('created_at', format='%m/%d/%Y')
    updated_at = DateField('updated_at', format='%m/%d/%Y')


class ArticleList(db2.Model):

    __tablename__ = 'article_list'

    id = db2.Column(db2.Integer, primary_key=True)
    article_type_id = db2.Column(db2.Integer, db2.ForeignKey(
        'article_type.id'), nullable=False)

    # foreign key from authentication app
    user_detail_id = db2.Column(db2.Integer, db2.ForeignKey(UserDetails.id), nullable=False)

    name = db2.Column(db2.String(80), nullable=False)
    title = db2.Column(db2.String(180), nullable=False)
    description = db2.Column(db2.String(280), nullable=False)
    image = db2.Column(db2.String(80), nullable=False)
    article_write_by = db2.Column(db2.String(180), nullable=False)
    article_writer_image = db2.Column(db2.String(80), nullable=False)
    active = db2.Column(db2.Boolean)
    created_at = DateField('created_at', format='%m/%d/%Y')
    updated_at = DateField('updated_at', format='%m/%d/%Y')
