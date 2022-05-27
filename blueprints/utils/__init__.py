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
"""Module containing all utility functions used in the application."""
import json
import os
import random
import re
import string
from flask import abort
from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Response

utils_module = Blueprint("utils_module", __name__)

ROOT_DIR = os.path.dirname(__file__)
EXPECTED_RESULTS_FILE = open(
    os.path.join(ROOT_DIR, "resources/expected-results.json"), "r")
EXPECTED_RESULTS = json.load(EXPECTED_RESULTS_FILE)
# Remove trailing slash, join expexted paths with "|" and escape dots.
PATHS_REGEX_STRING = "|".join(
    [re.sub(r"^/", "", item) for item in EXPECTED_RESULTS]).replace(".", r"\.")
PATH_REGEX = re.compile("^(" + PATHS_REGEX_STRING + ")$")


@utils_module.route("/fetch-expected-results")
def fetch_expected_results():
  """Returns a list of expected findings from a starting path."""
  response_results = []
  path = request.args.get("path", "")

  if not path:
    return Response("Please, provide the path parameter.", 400)

  for result in EXPECTED_RESULTS:
    if result.startswith(path):
      response_results.append(result)

  return jsonify(response_results)


@utils_module.route("/test/<path:path>")
def valid_resource(path):
  """Returns a 200 response for files that are supposed to be found by crawlers."""
  if re.match(PATH_REGEX, path):
    return Response(random_response(), 200)

  abort(404)


def random_response():
  letters = string.ascii_letters + "\n "
  return "\n".join(random.choice(letters) for i in range(1000))
