from flask import Blueprint, flash, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get('note')
        
        if len(note) < 2 :
            flash("Note is too short! at least 2 characters needed", category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category="success")
    
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=["POST"])
@login_required
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})

@views.route('/toggle-note', methods=["POST"])
@login_required
def toggle_note():
    note_data = json.loads(request.data)
    noteId = note_data['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            note.completed = not note.completed
            db.session.commit()
    
    return jsonify({})
