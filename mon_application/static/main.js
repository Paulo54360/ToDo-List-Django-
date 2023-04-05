document.getElementById('todoForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const todoInput = document.getElementById('todoInput');
    const todoText = todoInput.value.trim();

    if (todoText) {
        try {
            const newTodo = createTodoElement(todoText);
            document.getElementById('todoList').appendChild(newTodo);
            todoInput.value = '';
        } catch (error) {
            console.error('Error creating todo element:', error);
        }
    }
});

function createTodoElement(text) {
    const li = document.createElement('li');
    li.textContent = text;

    li.addEventListener('click', () => {
        li.classList.toggle('line-through');
        li.classList.toggle('text-gray-500');
    });

    li.addEventListener('dblclick', () => {
        li.remove();
    });

    return li;
}
