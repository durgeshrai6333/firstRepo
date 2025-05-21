from flask import Blueprint, request, jsonify
from todo_app.models.todo import Todo

todo_bp = Blueprint('todo_bp', __name__)

@todo_bp.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title:
        return jsonify({"error": "Title is required"}), 400

    new_todo = Todo(title=title, description=description)
    Todo.todos_list.append(new_todo)
    # Convert todo object to dict before jsonify
    return jsonify({
        "id": new_todo.id,
        "title": new_todo.title,
        "description": new_todo.description,
        "completed": new_todo.completed
    }), 201

@todo_bp.route('/todos', methods=['GET'])
def get_todos():
    # Convert list of todo objects to list of dicts
    todos_as_dicts = [{
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed
    } for todo in Todo.todos_list]
    return jsonify(todos_as_dicts), 200

@todo_bp.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((todo for todo in Todo.todos_list if todo.id == todo_id), None)
    if todo:
        return jsonify({
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "completed": todo.completed
        }), 200
    return jsonify({"error": "Todo not found"}), 404

@todo_bp.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((todo for todo in Todo.todos_list if todo.id == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    data = request.get_json()
    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    todo.completed = data.get('completed', todo.completed)
    
    return jsonify({
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed
    }), 200

@todo_bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos_list # Required if Todo.todos_list is not directly modifiable
    todo_to_delete = None
    for index, todo in enumerate(Todo.todos_list):
        if todo.id == todo_id:
            todo_to_delete = index
            break
            
    if todo_to_delete is not None:
        Todo.todos_list.pop(todo_to_delete)
        return jsonify({"message": "Todo deleted successfully"}), 200
    return jsonify({"error": "Todo not found"}), 404
