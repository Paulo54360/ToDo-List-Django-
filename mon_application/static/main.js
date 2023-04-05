const todoForm = document.getElementById('todoForm');
const todoInput = document.getElementById('todoInput');
const todoList = document.getElementById('todoList');

todoForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const todoText = todoInput.value.trim();

    if (todoText) {
        try {
            const response = await fetch('/api/tasks/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ title: todoText })
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.status} - ${response.statusText}`);
            }

            const data = await response.json();
            const newTodo = createTodoElement(data.title);
            todoList.appendChild(newTodo);
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
