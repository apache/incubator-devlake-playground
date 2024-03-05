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

from dataclasses import dataclass
from typing import Optional

import pandas as pd


@dataclass
class IssueFilter:
    project_key: Optional[str] = None
    from_date: Optional[pd.Timestamp] = None
    to_date: Optional[pd.Timestamp] = None
    issue_type: Optional[str] = None

    def apply(self, issue_df: pd.DataFrame):
        df = issue_df.copy()
        if self.project_key:
            df = df[df["issue_key"].str.startswith(self.project_key)]
        if self.from_date:
            df = df[df["changed_date"] >= self.from_date]
        if self.to_date:
            df = df[df["changed_date"] <= self.to_date]
        if self.issue_type:
            df = df[df["issue_type"] == self.issue_type]
        return df
