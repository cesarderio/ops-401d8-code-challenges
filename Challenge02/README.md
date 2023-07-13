# Ops Challenge: Uptime Sensor Tool Part 2 of 2

## Overview

Overview
Oftentimes, security operations and general systems administration duties overlap. One such example is the need to monitor events taking place on infrastructure throughout the day.

Today you will finish writing an uptime sensor tool that checks systems are responding by adding a feature that notifies you of interesting status changes.

## Resources

[How to Easily Automate Emails with Python](https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151)

## Requirements

In Python, add the below features to your uptime sensor tool.

## Objectives

The script must:

* Ask the user for an email address and password to use for sending notifications.

* Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).

* Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.

### ***Important Notes***

* **DO NOT** commit your email password in plain text within your script to GitHub as this easily becomes public.

* Create a new “burner” account for this exercise. Do not use an existing email account.

<br>

## Stretch Goals (Optional Objectives)

In Python, add the below features to your uptime sensor tool.

* Append all status changes to an event log. Each event must include a timestamp, event code, any host IP addresses involved, and a human readable description.

* Check for **BURNER_EMAIL_ADDRESS** and **BURNER_EMAIL_PASSWORD** environment variables (eg: loaded from **.profile**). If found, the script skips requesting credentials via user input.

* Alternatively, send the notification email from a cloud mailer service (like Mailgun, or AWS SES), instead of SMTP through your burner address.
