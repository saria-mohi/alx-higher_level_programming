#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
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
