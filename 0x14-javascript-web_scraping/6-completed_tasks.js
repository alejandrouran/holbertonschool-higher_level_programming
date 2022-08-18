#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const all = JSON.parse(body);
    const completed = {};
    all.forEach((all) => {
      if (all.completed && completed[all.userId] === undefined) {
        completed[all.userId] = 1;
      } else if (all.completed) {
        completed[all.userId] += 1;
      }
    });
    console.log(completed);
  }
});
