from api.v1 import db
from api.v1.models import Task
from api.v1.routes import bp
from flask import jsonify


@bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    """Delete a task if it exists"""
    # Retrieve the task from the database
    task = Task.query.filter_by(id=id).first()
    if not task:
        return jsonify({'error': f'Task with id {id} was not found.'})
    # Delete the task from the database
    db.session.delete(task)
    db.session.commit()
    # Return a success message as JSON response
    return jsonify({'message': f'Task with id {id} was deleted successfully.'})
