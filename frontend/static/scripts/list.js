$(document).ready(function () {
  $.get('http://127.0.0.1:5000/api/v1/tasks', function (data) {
    $(window).on('load', function () {
      $.each(data, function (key, value) {
        const taskCard = 
        `
        <div class="note-card" data-task-id=${value.id}>
          <h3>${value.title}</h3>
          <p>${value.description}</p>
          <div class="meta">
            <span class="status">${value.status}</span>
            <span class="due-date">${value.due_date}</span>
            <span class="priority">${value.priority}</span>
          </div>
          <div class="actions">
            <button class="edit">Edit</button>
            <button class="delete">Delete</button>
          </div>
        </div>
        `
        $('DIV#task-list').append(taskCard);
      });
    });
  });
});

