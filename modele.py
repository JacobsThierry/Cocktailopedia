from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy_mixins import AllFeaturesMixin
from flask_admin.contrib.sqla import ModelView
from database import Base, db
from flask_admin.model import BaseModelView
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method


class Utilisateur(Base, AllFeaturesMixin):
   __tablename__ = 'utilisateur'
   id_utilisateur = db.Column(db.String(255), primary_key=True)
   nom_utilisateur = db.Column(db.String(255))
   prenom_utilisateur = db.Column(db.String(255))
   email_utilisateur = db.Column(db.String(255))


class Role(Base, AllFeaturesMixin):
   __tablename__ = 'role'
   id_role = db.Column(db.Integer, primary_key=True)
   nom_role = db.Column(db.String(255))
   
   
class A_role(Base, AllFeaturesMixin):
   __tablename__ = 'a_role'
   id_role = db.Column(db.Integer, db.ForeignKey('role.id_role'), primary_key=True)
   id_utilisateur = db.Column(db.String(255), db.ForeignKey('utilisateur.id_utilisateur'), primary_key=True)
   
class Ingredient(Base, AllFeaturesMixin):
   id_ingredient = db.Column(db.Integer, primary_key=True)
   nom_ingredient = db.Column(db.String(255))
   description_ingredient = db.Column(db.String(255))
   prix_cl_ingredient = db.Column(db.Float)
   
class A_ingredient(Base, AllFeaturesMixin):
   __tablename__ = 'a_ingredient'
   id_ingredient = db.Column(db.Integer, db.ForeignKey('ingredient.id_ingredient'), primary_key=True)
   id_cocktail = db.Column(db.Integer, db.ForeignKey('cocktail.id_recette'), primary_key=True)
   quantite_ingredient_cl = db.Column(db.Float)

class Cocktail(Base, AllFeaturesMixin):
   __tablename__ = 'cocktail'
   id_cocktail = db.Column(db.Integer, primary_key=True)
   nom_cocktail = db.Column(db.String(255))
   description_cocktail = db.Column(db.String(255))
   image_cocktail = db.Column(db.String(255))
   est_accepte_cocktail = db.Column(db.Boolean)
   auteur_cocktail = db.Column(db.Integer, db.ForeignKey('utilisateur.id_utilisateur'))
   date_creation_cocktail = db.Column(db.DateTime)


class A_vote(Base, AllFeaturesMixin):
   __tablename__ = "a_vote"
   id_utilisateur = db.Column(db.String(255), db.ForeignKey('utilisateur.id_utilisateur'), primary_key=True)
   id_cocktail = db.Column(db.Integer, db.ForeignKey('cocktail.id_cocktail'), primary_key=True)
   date_vote = db.Column(db.DateTime)
   pour_contre_vote = db.Column(db.Boolean)