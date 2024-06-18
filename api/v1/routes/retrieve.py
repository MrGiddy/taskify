from api.v1.routes import bp
from api.v1.models import Task
from flask import jsonify


@bp.route('/tasks', methods=['GET'])
def get_tasks():
    """Retrieve a list of all the tasks available"""
    tasks = Task.query.all()
    if not tasks:
        return jsonify({'error': 'No tasks were found.'}), 404
    return jsonify([task.to_dict() for task in tasks]), 200 # Retun tasks if available


@bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    """Retrieve a single task by its id if available"""
    task = Task.query.filter_by(id=id).first()
    if not task:
        return jsonify({'error': f'Task with id {id} was not found.'}), 404
    return jsonify(task.to_dict()), 200 # Return task if found
