var apiUrl = 'http://localhost:5000/tasks';

// Toggles the completed property of the task
function toggleComplete(taskId) {
  var completed = eval($('*[data-taskid="' + taskId +'"]')
    .attr('data-completed'));

  axios.put(apiUrl + '/' + taskId, {completed: !completed}).then(function(res) {
    getAllTasks();
  });
}

// Fetches all tasks from the API
function getAllTasks() {
  // Clear previous tasks
  $('.todolist').empty();

  axios.get(apiUrl).then(function(res) {
    var tasks = res.data;
    addTasksToPage(tasks);
  });
}

// Adds a new task to the API
function addTask(task) {
  var text = $('#text').val();
  var data = {
    text: text,
    completed: false
  };
  axios.post(apiUrl, data).then(function (res) {
    $('#text').val('');
    getAllTasks();
    toastr.info('New todo task added!');
  });
}

// Create the LI that is used to display a task
function createListItem(task) {
  var btnText;
  if (task.completed) {
    btnText = 'Mark Uncomplete';
    btnClass = 'btn-success'
  } else {
    btnText = 'Mark Complete';
    btnClass = 'btn-danger'
  }

  var html = '<li data-text="' + task.text + '" data-taskid="' + task._id + '"';
  html += ' data-completed="' + task.completed + '">'
  html += '<div class="card"><div class="card-block">';
  html += '<button type="button" onclick="toggleComplete(\'' + task._id + '\')"';
  html += 'class="btn ' + btnClass + ' btn-sm">' + btnText + '</button>';
  html += task.text;
  html += '</div></div>'
  html += '</li>'
  return html;
}

// Adds a task to the DOM
function addTasksToPage(tasks) {
  tasks.forEach(function (task) {
    $('.todolist').append(createListItem(task));
  });
}

// Main Entry
$(document).ready(function() {
  getAllTasks();
});
