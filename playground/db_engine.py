# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Database engine utility.
"""

from urllib.parse import parse_qsl, urlparse

from sqlalchemy.engine import Engine, create_engine


def create_db_engine(db_url: str) -> Engine:
    """
    Create a SQLAlchemy engine for the given database URL.
    """

    # SQLAlchemy doesn't understand postgres:// scheme
    db_url = db_url.replace("postgres://", "postgresql://")
    # Use MySQL connector for mysql:// scheme
    db_url = db_url.replace("mysql://", "mysql+mysqlconnector://")
    # Remove query args
    base_url = db_url.split("?")[0]
    # `parseTime` parameter is not understood by MySQL driver,
    # so we have to parse query args to remove it
    connect_args = dict(parse_qsl(urlparse(db_url).query))
    if "parseTime" in connect_args:
        del connect_args["parseTime"]
    if "loc" in connect_args:
        del connect_args["loc"]
    if "tls" in connect_args:
        del connect_args["tls"]
        connect_args["ssl"] = {"verify_cert": "False"}
    try:
        return create_engine(base_url, connect_args=connect_args)
    except Exception as e:
        raise IOError("Unable to make a database connection") from e
