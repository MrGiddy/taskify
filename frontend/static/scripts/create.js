$(document).ready(function() {
  // When create task button is clicked
  $('BUTTON#create-task-button').on('click', function () {
    $('DIV#task-form-modal').css({'display':'block'})
  });
  // When the task form is submitted
  $('FORM.task-form-create').on('submit', function (event) {
    event.preventDefault();
    const formData = $(this).serialize();
    sendPostRequest('POST', '/api/v1/create', formData);
  });
  // Exit the form modal display when X is clicked
  $('SPAN.close').on('click', function () {
    $('DIV#task-form-modal').css({'display':'none'})
  });

  // Sends POST request to api
  function sendPostRequest(reqType, endPoint, formData) {
    $.ajax({
      type: reqType,
      url: `http://127.0.0.1:5000${endPoint}`, // backend API endpoint
      contentType: 'application/x-www-form-urlencoded',
      data: formData,
      success: function(response) {
        // Update the task list
        // Obtain the task-list container from HTML code
        const $taskList = $('DIV#task-list');

        // Construct the HTML content for the note-card
        $noteCard = $('<div>', {class: 'note-card', 'data-task-id': response.id});
        $title = $('<h3>').text(response.title);
        $description = $('<p>').text(response.description);
        $meta = $('<div>', {class: 'meta'});
        $status = $('<span>', {class: 'status'}).text(response.status);
        $dueDate = $('<span>', {class: 'due-date'}).text(response.due_date);
        $priority = $('<span>', {class: 'priority'}).text(response.priority);
        $actions = $('<div>', {class: 'actions'});
        $editButton = $('<button>', {class: 'edit'}).text('Edit');
        $deleteButton = $('<button>', {class: 'delete'}).text('Delete');

        $meta.append($status).append($dueDate).append($priority);
        $actions.append($editButton).append($deleteButton);
        $noteCard.append($title).append($description).append($meta).append($actions);
        $taskList.append($noteCard);

        // Reset the form and hide the create form modal display
        $('#task-form')[0].reset();
        $('DIV#task-form-modal').css({'display':'none'});
      },
      error: function(error) {
        console.log(error.responseText);
      }
    });
  }
});
