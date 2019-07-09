# The builder image is used to install all the tools required to build one page applications.
# All the tools are abandoned after the production image is built. It lets us
# create a very lightweight container with bundled files without any node tools.
FROM node:10-alpine AS builder

# Allows npm to run within the context of the running script.
# Needed to install Angular CLI.
RUN npm config set unsafe-perm true

# Install JavaScript framework tools.
RUN npm install -g @angular/cli

# Build Angular app.
COPY test-cases/javascript/frameworks/angular /tmp/angular
WORKDIR /tmp/angular
RUN npm install
RUN ng build --prod --baseHref=/javascript/frameworks/angular/

##########################
# Build production image.#
##########################
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

# Copy all the files.
COPY app.py /usr/src/app/
COPY blueprints /usr/src/app/blueprints
COPY templates /usr/src/app/templates
COPY test-cases /usr/src/app/test-cases

# Remove source files and copy single page app bundles from the builder image.
RUN rm -rf /usr/src/app/test-cases/javascript/frameworks/angular/*
COPY --from=builder /tmp/angular/dist/angular /usr/src/app/test-cases/javascript/frameworks/angular


# Run the application. Default port is 8080.
# If you want to change it, pass a $PORT env variable.
CMD ["python", "/usr/src/app/app.py"]
