#!/usr/bin/env expect

spawn nosetests

expect "Enter your (weird) secret identity:"
send "hey\r"
expect eof
