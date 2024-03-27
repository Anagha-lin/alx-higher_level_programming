#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    return;
  }

  const todos = JSON.parse(body);

  // Object to store completed tasks count by user id
  const completedTasksByUser = {};

  // Loop through each todo
  todos.forEach(todo => {
    // Check if the todo is completed
    if (todo.completed) {
      // Increment completed tasks count for the user id
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  console.log(completedTasksByUser);
});

