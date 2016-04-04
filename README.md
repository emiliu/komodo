## Komodo

An IRL achievement system for reading books

### Creation

This project was created during [HackBCA III](http://hackbca.com/),
using [Flask](http://flask.pocoo.org/) and [Twilio](https://www.twilio.com/).
Our project followed the "Code for Good" path, sponsored by [Intel](http://www.intel.com/)
and the [Institute for Wellness Education](https://www.instituteforwellness.com/),
which prompted us to use persuasive technology to encourage change. Inspired by
video game achievements, we created a tool for helping people to read more.

### Setup

We used a free trial account of Twilio, so our credentials are no longer valid. You'll want to
create a Twilio account and use your own credentials to try out this project.

We used Flask and Twilio's Python libary for its REST API. You can install these via:

```
$ pip install flask twilio
```

Alternatively, you can install the exact versions of the libraries that we used:

```
$ pip install -r requirements.txt
```

Clone the git repository and change the sending phone number and Twilio credentials in ``app.py``.
Set up a webhook with [https://ngrok.com/](ngrok) by downloading and running:

```
$ ./ngrok http 5000
```

Update your Twilio app with the ngrok public URL that forwards to ``localhost:5000``.

To run the app, make sure you are in the top-level directory (``komodo``). From the command line, run:

```
$ python app.py
```

The website will be live at [http://localhost:5000/](http://localhost:5000).
To clear your session, point your browser at [http://localhost:5000/reset](http://localhost:5000/reset).
