#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -sLX PUT "0.0.0.0:5000/catch_me" -d "user_id=98" -H "Origin: You got me!"