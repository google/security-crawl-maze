# Security Crawl Maze

Security Crawl Maze is a comprehensive testbed for web security crawlers. It contains
pages representing many (hopefully all) ways in which one can link resources
from a valid HTML document. List of all the cases covered by Security Crawl Maze can be
found [below](#test-cases).

## Crawling vs Security Crawling

Security crawlers are interested in different findings than regular web
crawlers. They are not interested in maximizing content coverage but in
maximizing code coverage. This application is supposed to provide a unified and
extensive way of testing efficiency of web security crawlers. First release
contains only static linking of resources from html documents but future
development will focus on adding more complex cases such as: Single Page
Applications (Angular, Polymer), dynamically generated content (Blogs,
e-commerce systems) and many other.

## Run / deploy the application

The primary goal was to be able to run and deploy the app easily in any
environment. Therefore, we provide a Dockerfile which enables you to deploy it
to any cloud that is run by a provider of your choice. For local development or
testing you can also make the app up and running quickly either in a local
container or as a Python Flask app. Please, find the instructions below.

### Run locally in a container

1.  pull the project and enter the project's directory
2.  build the docker image `docker build -t crawlmaze .`
3.  run the image and expose port 80 `docker run -p 80:5000 --name crawlmaze
    crawlmaze`
4.  to remove the container `docker rm -f crawlmaze`

### Run locally as a Flask app

1.  pull the project and enter the project's directory
2.  install pip dependencies `pip install -r requirements.txt`
3.  run app `python app.py`

### Deploy to Google Cloud

1.  The Dockerfile is in the root directory and you can use it to deploy your
    application to Google Cloud
2.  Follow
    [these](https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app)
    instructions

### Conventions

#### Naming

*   HTML folder contains directories named after tag names. e.g. `html/body/a`
    will contain tests for an `<a>` tag which is located in the HTML's body
    element,
*   HTML files are usually named after the attribute that links a resource. e.g.
    `html/body/a/href.html` will contain one test case for an `href` attribute
    inside an `<a>` tag,
*   Nested tags are placed in nested folders. e.g. `html/body/form/button` will
    contain tests for a `<button>` tag placed inside a `<form>` tag,
*   Resources that are expected to be found by crawlers end with '.found' suffix
    e.g. `html/body/a/href.html` will contain a link to
    `http://<HOST>/html/body/a/href.found`. This way it's easy to identify a
    test case that is not found by your crawler.

#### Expected results API endpoint

The application exposes an API endpoint that you can use to fetch a set of URLs
that are expected to be found by crawlers. It is located under:

```
http://<HOST>/fetch-expected-results?path=<PATH>
```

where <PATH> is a starting url of the crawl e.g.

```
http://<HOST>/fetch-expected-results?path=/html/body/form
```

returns:

```
[
    "/html/body/form/action.found",
    "/html/body/form/button/formaction.found"
]
```

## Test cases

Implemented test cases (resources to be found) are available in the `expected-results.json` file.

### Adding a test case

1.  Add your test case
    *   If you're adding a file to already existing folder go to point 2.
    *   If you're creating a new folder you have to add an endpoint in `app.py`
        that serves files from your directory. You also have to remember to add
        a rule in `Dockerfile` to include your files in the container image.
2.  Link your test case from corresponding `index.html` file
3.  Add record to expected_results.json.
4.  Test your crawler with the new test case!
5.  Before creating a PR, make sure your code follows the
    [Google Python Language Rules](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#2-python-language-rules)

### Credits

Many of the test cases were borrowed from a document by cure53
[HTTPLeaks](https://github.com/cure53/HTTPLeaks/blob/master/leak.html).

## License information

See the LICENSE file.
