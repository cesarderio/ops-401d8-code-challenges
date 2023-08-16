# Ops Challenge: Event Logging Tool Part 3 of 3

## Overview

Logging system events for response and/or analysis is a major part of security operations. Logs create accountability and also provide signals to build automation systems around. With proper logging and monitoring, a SOC team can respond quickly and appropriately as events unfold.

Today you will apply finishing touches to your logging feature.

## Resources

[Python Logging: Using Handlers](https://realpython.com/python-logging/#using-handlers)

## Requirements

In your Python tool:

* Use StreamHandler and FileHandler in your Python script.

  * FileHandler should write to a local file.

  * StreamHandler should output to the terminal.

<br>

## Stretch Goals (Optional Objectives)

Have your script also email you the event details.

* Your handler must distinguish by event type. For example, in [DEMO.md](https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/class-28/challenges/DEMO.html) the handler only emails `ERROR` and not `WARNING` types.

* See if you can include all features this week in one script, e.g. log rotation with FileHandler.
