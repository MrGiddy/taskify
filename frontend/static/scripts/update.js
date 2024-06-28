$(document).ready(function () {
  // Exit the form modal display when X is clicked
  $('SPAN.close').on('click', function () {
    $('DIV#update-task-form-modal').css({'display':'none'})
  });
  // Event delegation for edit button
  $('DIV#task-list').on('click', '.edit', function () {
    // Display the task form modal
    $('DIV#update-task-form-modal').css({'display': 'block'});

    // Pre-fill the task form with the note-card's data
    const $noteCard = $(this).closest('.note-card');
    $('INPUT#update-task-title').val($noteCard.find('h3').text());
    $('TEXTAREA#update-task-desc').val($noteCard.find('p').text());
    $('SELECT#update-task-status').val($noteCard.find('.status').text());
    $('INPUT#update-task-due-date').val($noteCard.find('.due-date').text());
    $('SELECT#update-priority').val($noteCard.find('.priority').text());

    // Bind the submit event handler to the update form
    // $('#task-form').off('submit');
    $('FORM#update-task-form').off('submit').on('submit', function (event) {
      event.preventDefault();
      // Obtain the updated data for the task
      const updated = {
        id: $noteCard.data('task-id'),
        title: $('INPUT#update-task-title').val(),
        description: $('TEXTAREA#update-task-desc').val(),
        status: $('SELECT#update-task-status').val(),
        due_date: $('INPUT#update-task-due-date').val(),
        priority: $('SELECT#update-priority').val()
      }
      // Update the task in the database
      sendPutRequest('PUT', updated, $noteCard);
    });
  });

  // Sends a put request of the form data to backend
  function sendPutRequest(reqType, updated, $noteCard) {
    $.ajax({
      type: reqType,
      url: `http://127.0.0.1:5000/api/v1/tasks/${updated.id}`,
      contentType: 'application/x-www-form-urlencoded',
      data: $.param(updated),
      success: function(response) {
        // Update the task-card display on browser
        $noteCard.find('h3').text(response.title);
        $noteCard.find('p').text(response.description);
        $noteCard.find('.status').text(response.status);
        $noteCard.find('.due-date').text(response.due_date);
        $noteCard.find('.priority').text(response.priority);

        // Reset the form and hide the modal
        $('#update-task-form')[0].reset();
        $('DIV#update-task-form-modal').css({'display':'none'});;
      },
      error: function(error) {
        console.log(error.responseText);
      }
    });
  }
});
