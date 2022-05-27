# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Module serving all the traffic for javascript test cases."""
import os
from flask import abort
from flask import Blueprint
from flask import make_response
from flask import render_template
from flask import Response
from flask import send_from_directory
from flask import url_for

javascript_module = Blueprint(
    "javascript_module", __name__, template_folder="templates")

# Global app.instance_path is not accessible from blueprints ¯\_(ツ)_/¯.
TEST_CASES_PATH = os.path.abspath(__file__ + "/../../../test-cases/javascript/")


@javascript_module.route("/misc/comment.js")
def comment():
  content = "// " + url_for(
      "index", _external=True) + "test/javascript/misc/comment.found"
  r = make_response(content, 200)
  r.headers["Content-Type"] = "application/javascript"
  return r


@javascript_module.route("/misc/string-variable.js")
def string_variable():
  content = "var url = \"" + url_for(
      "index", _external=True) + "test/javascript/misc/string-variable.found\";"
  r = make_response(content, 200)
  r.headers["Content-Type"] = "application/javascript"
  return r


@javascript_module.route("/frameworks/angular/", defaults={"path": ""})
@javascript_module.route("/frameworks/angular/<path:path>")
def angular(path):
  return serve_framework_resource_or_root("angular", path)


@javascript_module.route("/frameworks/angularjs/", defaults={"path": ""})
@javascript_module.route("/frameworks/angularjs/<path:path>")
def angularjs(path):
  return serve_framework_resource_or_root("angularjs", path)


@javascript_module.route("/frameworks/polymer/", defaults={"path": ""})
@javascript_module.route("/frameworks/polymer/<path:path>")
def polymer(path):
  return serve_framework_resource_or_root("polymer", path)


@javascript_module.route("/frameworks/react/", defaults={"path": ""})
@javascript_module.route("/frameworks/react/<path:path>")
def react(path):
  return serve_framework_resource_or_root("react", path)


@javascript_module.route("/misc/string-concat-variable.js")
def string_concat_variable():
  content = "var domain = \"" + url_for(
      "index", _external=True
  ) + ("\";var path = \"test/javascript/misc/string-concat-variable.found\";var"
       " full = domain + path;")
  r = make_response(content, 200)
  r.headers["Content-Type"] = "application/javascript"
  return r


@javascript_module.route("/", defaults={"path": ""})
@javascript_module.route("/<path:path>")
def html_dir(path):
  """Lists contents of requested directory."""
  requested_path = os.path.join(TEST_CASES_PATH, path)
  if not os.path.exists(requested_path):
    return abort(404)

  if os.path.isdir(requested_path):
    files = os.listdir(requested_path)
    return render_template("list-javascript-dir.html", files=files, path=path)

  if os.path.isfile(requested_path):
    return send_from_directory("test-cases/javascript", path)


def serve_framework_resource_or_root(framework, path):
  directory = os.path.join(TEST_CASES_PATH, "frameworks", framework)
  requested_file = os.path.join(directory, path)
  if os.path.isfile(requested_file):
    return send_from_directory(directory, path)
  else:
    return serve_framework_root(framework)


def serve_framework_root(framework):
  root_path = os.path.join(TEST_CASES_PATH, "frameworks", framework)
  return send_from_directory(root_path, "index.html")
