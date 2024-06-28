$(document).ready(function () {
  // Event delegation for the delete button click
  $('DIV#task-list').on('click', '.delete', function () {
    // Delete note-card from database and then from screen
    const $noteCard = $(this).closest('.note-card');
    const $taskId = $noteCard.data('task-id');
    $.ajax({
      type: 'DELETE',
      url: `http://127.0.0.1:5000/api/v1/tasks/${$taskId}`,
      success: function(response) {
        // Remove note-card from screen
        $noteCard.remove();
      },
      error: function(error) {
        console.log(error.responseText);
      }
    });
  });
});
