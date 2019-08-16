from flask import jsonify
from database_setup import Chores 
from populate_db import session
from datetime import datetime, timedelta

def get_chores():
    chores = session.query(Chores).all()
    return jsonify([c.serialize for c in chores])

def get_chore(chore_id):
    try:
        chore = session.query(Chores).filter_by(chore_title=chore_id).one()
        if chore:
            return jsonify(chore.serialize)
    except:
        return "No such chores exist\n"

def makeANewChore(chore):
    title, task = chore.items()[0]
    addedchore = Chores(chore_title=title, chore=task)
    existing_titles = [ elem.chore_title for elem in session.query(Chores).all() ]
    if addedchore.chore_title not in existing_titles:
        session.add(addedchore)
        session.commit()
        return jsonify(addedchore.serialize)
    else:
        return "Chore title already exist.\n"

def updateChore(title, task):
    try:
        tobeUpdatedChore = session.query(Chores).filter_by(chore_title=title).one()
        tobeUpdatedChore.chore = task
        session.merge(tobeUpdatedChore)
    except:
        tobeUpdatedChore = Chores(chore_title=title, chore=task)
        session.add(tobeUpdatedChore)
    session.commit()
    return "Updated the chore with id %s\n" % title

def deleteAChore(choreid):
   try:
       choreToDelete = session.query(Chores).filter_by(chore_title=choreid).one()
   except:
       return "No such chores exist\n"

   session.delete(choreToDelete)
   session.commit()
   return "Removed Chore with id %s\n" % choreid

def deleteAllChores():
    try:
        num_rows_deleted = session.query(Chores).delete()
        session.commit()
        return "{} records deleted\n".format(num_rows_deleted)
    except:
        session.rollback()
