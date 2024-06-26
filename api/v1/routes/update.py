from api.v1 import db
from api.v1.models import Task
from api.v1.routes import bp
from datetime import datetime
from flask import jsonify
from flask import request


@bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    "Update an existing task"
    # Retrieve the task from database
    task = Task.query.filter_by(id=id).first()
    if not task:
        return jsonify({'error': f'Task with id {id} was not found.'})
    # Validate title and status from incoming data
    if not request.form.get('description'):
        return jsonify({'error': 'title field cannot be empty.'}), 400
    if not request.form.get('status'):
        return jsonify({'error': 'status field cannot be empty.'}), 400
    # Parse due_date string to a datetime object
    due_date = request.form.get('due_date')
    if due_date:
        try:
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            return jsonify({'error': 'Incorrect date format, should be YY-MM-DD.'}), 400
    # Update the task information in the database
    task.title = request.form.get('title')
    task.description = request.form.get('description')
    task.due_date = due_date
    task.status =  request.form.get('status')
    task.priority = request.form.get('priority')
    db.session.commit()
    # Retrieve the updated task from the database
    updated = Task.query.filter_by(id=id).first()
    if not updated:
        return jsonify({'error': 'Failed to retrieve the updated task.'})
    # Convert the task to a dictionary
    updated = updated.to_dict()
    # Return the dictionary as a JSON response
    return jsonify(updated), 200
