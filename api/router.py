from fastapi import APIRouter
from api.schemas import TodoCreate, Todo
from core.todos import todos, todo_id_counter
from fastapi import HTTPException

router = APIRouter(prefix="/todos")


@router.post("/todos")
async def add_todo(todo_data: TodoCreate):
    current_id = todo_id_counter
    todo = Todo(id=current_id, title=todo_data.title, createdAt=todo_data.createdAt)
    todo_id_counter += 1
    todos.append(todo)
    return todo


@router.get("/todos")
async def get_todos():
    try:
        return todos
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/todos/{id}")
async def get_todo(id: int):
    for todo in todos:
        if todo.id == id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@router.put("/todos/{id}")
async def update_todo(id: int, todo_data: TodoCreate):
    for todo in todos:
        if todo.id == id:
            todo.title = todo_data.title
            todo.createdAt = todo_data.createdAt
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@router.delete("/todos/{id}")
async def delete_todo(id: int):
    for todo in todos:
        if todo.id == id:
            todos.remove(todo)
            return {"detail": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
