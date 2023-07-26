#!/usr/bin/node
// print total task complete
const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, function(error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    for (const userId in completed) {
      console.log(`User ${userId} completed ${completed[userId]} tasks.`);
    }
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
