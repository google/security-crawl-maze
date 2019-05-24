# Base image.
FROM alpine:3.9

# Install python and pip.
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    # Make sure that pip3 is being referred when calling just pip command
    # by doing a symbolic link on python and system binaries' directories.
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi

# Install all Python requirements for our app to run.
COPY requirements.txt /usr/src/app/
RUN pip install -r /usr/src/app/requirements.txt

# Copy all the other files.
COPY app.py /usr/src/app/
COPY templates /usr/src/app/templates
COPY resources /usr/src/app/resources
COPY test-cases /usr/src/app/test-cases

# Expose the Flask app's port.
EXPOSE 5000

# Run the application.
CMD ["python", "/usr/src/app/app.py"]
