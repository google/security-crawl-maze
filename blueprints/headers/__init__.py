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
"""Module serving all the traffic for response headers test cases."""
import os
from flask import abort
from flask import Blueprint
from flask import make_response
from flask import render_template
from flask import Response
from flask import send_from_directory

headers_module = Blueprint(
    "headers_module", __name__, template_folder="templates")

# Global app.instance_path is not accessible from blueprints ¯\_(ツ)_/¯.
TEST_CASES_PATH = os.path.abspath(__file__ + "/../../../test-cases/headers/")


@headers_module.route("/content-location/")
def content_location():
  r = make_response(render_template("content-location-header.html"), 201)
  r.headers["Content-Location"] = "/test/headers/content-location.found"
  return r


@headers_module.route("/link/")
def link():
  r = make_response(render_template("link-header.html"), 200)
  r.headers["Link"] = "</test/headers/link.found>; rel=\"preload\""
  return r


@headers_module.route("/location/")
def location():
  # Not rendering a response because it will be redirected anyway.
  r = Response(status=301)
  r.headers["Location"] = "/test/headers/location.found"
  return r


@headers_module.route("/refresh/")
def refresh():
  r = make_response(render_template("refresh-header.html"), 200)
  r.headers["Refresh"] = "999; url=/test/headers/refresh.found"
  return r


@headers_module.route("/", defaults={"path": ""})
@headers_module.route("/<path:path>")
def html_dir(path):
  """Lists contents of requested directory."""
  requested_path = os.path.join(TEST_CASES_PATH, path)
  if not os.path.exists(requested_path):
    return abort(404)

  if os.path.isdir(requested_path):
    files = os.listdir(requested_path)
    return render_template("list-headers-dir.html", files=files, path=path)

  if os.path.isfile(requested_path):
    return send_from_directory("test-cases/headers", path)
