# a11y

## Tech Stack

- Flask as the web framwork
- Flask for handling http requests
- Python as the programming language
- Vercel for deployment

## FAQ

### What?
Test out any website with tools to simulate the experience of visual, auditory, or mobility impairments

### Why?
People struggle with the poor website design everyday. By using this project, you could know what parts of your website needs improvement. Or at the very least, we can spread awareness about the stuggles people face.

### How does it work?
The idea is pretty simple, this website caches the website you are looking for, modify the page to add the options, and then serve it to you.

## Development

Install [python](https://www.python.org/downloads/)

```sh
# Install flask
python -m pip install flask

# If that doesn't work retry but replace `python` with `py`, then try `python3`, then try `py3`

# Clone the sources
git clone https://github.com/justindhillon/a11y

# Run the `index.py`

# Start the application at https://localhost:5000.
```

click [this link](https://realpython.com/run-python-scripts/) for a tutorial on how to run python scripts

## Alternative method

You can also append the url at the end of the link and it will also work. (e.g if your server is running at `http://127.0.0.1:5000` then you can go to `http://127.0.0.1:5000/https://example.com` and it will read out the contents of `https://example.com`)
This feature is possible thanks to [atcasanova](https://github.com/atcasanova)

## Credits
- [13 foot wall](https://github.com/wasi-master/13ft)
- [dragable button](https://github.com/livebloggerofficial/Draggable-Button)
- [color-blindness-emulation](https://github.com/hail2u/color-blindness-emulation)

## Resources
- [Vercel Documentation](https://vercel.com/docs)
- [Flask Docs](https://flask.palletsprojects.com/en/3.0.x/)
- [Python Docs](https://docs.python.org/3/)
