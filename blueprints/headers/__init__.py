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
from flask import Blueprint
from flask import Response
from flask import send_from_directory

headers_module = Blueprint("headers_module", __name__)


@headers_module.route("/content-location")
def content_location():
  r = Response(status=201)
  r.headers["Content-Location"] = "/test/headers/content-location.found"
  return r


@headers_module.route("/link")
def link():
  r = Response(status=200)
  r.headers["Link"] = "</test/headers/link.found>; rel=\"preload\""
  return r


@headers_module.route("/location")
def location():
  r = Response(status=301)
  r.headers["Location"] = "/test/headers/location.found"
  return r


@headers_module.route("/refresh")
def refresh():
  r = Response(status=200)
  r.headers["Refresh"] = "0; url=/test/headers/refresh.found"
  return r


@headers_module.route("/<path:path>")
def html_dir(path):
  return send_from_directory("test-cases/headers", path)
