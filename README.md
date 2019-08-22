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

NOTE: Test cases for JS frameworks have to be built and bundled in order to work. If you use Docker, everything is automated. However, if you don't, you will have to build the projects manually.

The primary goal was to be able to run and deploy the app easily in any
environment. Therefore, we provide a Dockerfile which enables you to deploy it
to any cloud that is run by a provider of your choice. For local development or
testing you can also make the app up and running quickly either in a local
container or as a Python Flask app. Please, find the instructions below.

### Run locally in a container

1.  pull the project and enter the project's directory
2.  build the docker image `docker build -t crawlmaze .`
3.  run the image and expose port 80 `docker run -p 80:8080 --name crawlmaze
    crawlmaze`
4.  to remove the container `docker rm -f crawlmaze`

### Run locally as a Flask app (Does not support JS frameworks)

1.  pull the project and enter the project's directory
2.  install pip dependencies `pip install -r requirements.txt`
3.  run app `python app.py`

### Deploy to Google Cloud/AWS/Azure

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/google/security-crawl-maze)
or use the Dockerfile in the root directory to build a container image and deploy it to any other cloud of your choice.

### Use public version

There is a publicly available instance of the application running at [http(s)://security-crawl-maze.app](https://security-crawl-maze.app).

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
*   Files without extensions under the `test-cases/` directory are required so
    that links to API endpoints are generated.

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

Implemented test cases (resources to be found) are available in the
  `blueprints/utils/resources/expected-results.json` file.

### Adding a test case

1.  Create a file for your test case and place it in an appropriate directory.
    *   If your test content is generated dynamically by an API endpoint, add a
        file without an extension (e.g. `test-cases/headers/link`). This is to
        make sure the link to the test case is generated and is discoverable by
        crawlers.
    *   If you're NOT creating any new child folder in the `test-cases/`
        directory go to point 2.
    *   Otherwise you have to add a new blueprint directory with all the
        relevant components. You can reuse the structure of already existing
        blueprints.
2.  Add record which is to be found to the
    `blueprints/utils/resources/expected_results.json` file.
3.  Test your crawler with the new test case!
4.  Before creating a PR, make sure your code follows the
    [Google Python Language Rules](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#2-python-language-rules)

### Credits

Many of the test cases were borrowed from a document by cure53
[HTTPLeaks](https://github.com/cure53/HTTPLeaks/blob/master/leak.html).

## License information

See the LICENSE file.
