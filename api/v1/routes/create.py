from api.v1 import db
from api.v1.routes import bp
from api.v1.models import Task
from datetime import datetime
from flask import jsonify
from flask import request


@bp.route('/create', methods=['POST'])
def create_task():
    "Create a new task in storage"
    # Retrieve form data
    description = request.form.get('description')
    due_date = request.form.get('due_date')
    status = request.form.get('status')
    priority = request.form.get('priority')
    # Validate description and status
    if not description:
        return jsonify({'error': 'description is a required field.'}), 400
    if not status:
        return jsonify({'error': 'status is a required field.'}), 400
    # Parse due_date string to a datetime object
    if due_date:
        try:
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            return jsonify({'error': 'Incorrect date format, should be YY-MM-DD.'}), 400

    new_task = {
        'description': description,
        'due_date': due_date,
        'status': status,
        'priority': priority
    }

    # Add the new task to database
    new_task = Task(**new_task)
    db.session.add(new_task)
    db.session.commit()
    # Retrieve the newly created task from storage
    new_task = Task.query.filter_by(id=new_task.id).first()
    if not new_task:
        return jsonify({'error': 'Failed to retrieve the new task.'}), 500
    # Convert the new task to a dictionary
    new_task_dict = new_task.to_dict()
    # Return the new task dictionary as a JSON response
    return jsonify(new_task_dict), 201
