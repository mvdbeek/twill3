#!/usr/bin/env expect -f

spawn nosetests

expect "Enter your (weird) secret identity:"
send "hey\r"
expect eof
