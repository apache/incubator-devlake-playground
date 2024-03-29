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

import pandas as pd
from datetime import datetime

from playground.process_analysis.issue_filter import IssueFilter

def test_no_filter():
    df = data_frame()
    issue_filter = IssueFilter()
    
    filtered = issue_filter.apply(df)

    pd.testing.assert_frame_equal(filtered, df)


def test_project_filter():
    df = data_frame()
    issue_filter = IssueFilter(project_key="PROJ")

    filtered = issue_filter.apply(df)

    assert len(filtered) == 1
    assert filtered['issue_key'].unique() == ['PROJ-3']


def test_from_date_filter():
    df = data_frame()
    issue_filter = IssueFilter(from_date=_pd_timestamp_from("2021-01-03 00:00:00"))

    filtered = issue_filter.apply(df)

    assert len(filtered) == 1
    assert filtered['issue_key'].unique() == ['PROJ-3']


def test_to_date_filter():
    df = data_frame()
    issue_filter = IssueFilter(to_date=_pd_timestamp_from("2021-01-03 00:00:00"))

    filtered = issue_filter.apply(df)

    assert len(filtered) == 1
    assert filtered['issue_key'].unique() == ['OTHER-1']


def test_type_filter():
    df = data_frame()
    issue_filter = IssueFilter(issue_type="Bug")

    filtered = issue_filter.apply(df)

    assert len(filtered) == 1
    assert filtered['issue_key'].unique() == ['OTHER-1']


def test_filter_doesnt_mutate_original():
    df = data_frame()
    issue_filter = IssueFilter(project_key="PROJ")

    issue_filter.apply(df)

    assert len(df) == 2


def test_filter_everything():
    df = data_frame()
    issue_filter = IssueFilter(project_key="PROJ", issue_type="Bug")

    filtered = issue_filter.apply(df)

    assert len(filtered) == 0


def _pd_timestamp_from(datetime_str: str) -> pd.Timestamp:
    return pd.Timestamp(datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S"))


def data_frame():
    return pd.DataFrame([
        {
            "issue_key": "PROJ-3",
            "issue_type": "Story",
            "changed_date": _pd_timestamp_from("2021-01-07 00:00:00")
        },
        {
            "issue_key": "OTHER-1", 
            "issue_type": "Bug",
            "changed_date": _pd_timestamp_from("2021-01-02 00:00:00")
        }
    ])
