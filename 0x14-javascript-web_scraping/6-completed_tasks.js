#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    throw new Error(err);
  } else {
    const userCompletedTasks = {};
    newBody = JSON.parse(body);

    for (let i = 0; i < newBody.length; i++) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed && !userCompletedTasks[userId]) {
        userCompletedTasks[userId] = 0;
      }
       if (completed) ++userCompletedTasks[userId];
    }
    console.log(userCompletedTasks);
  }
});
