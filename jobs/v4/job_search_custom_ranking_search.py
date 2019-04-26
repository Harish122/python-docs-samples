# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT EDIT! This is a generated sample ("RequestPagedAll",  "job_search_custom_ranking_search")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-talent

import sys

# [START job_search_custom_ranking_search]

from google.cloud import talent_v4beta1
from google.cloud.talent_v4beta1 import enums
import six


def sample_search_jobs(project_id, tenant_id):
    """Search Jobs using custom rankings"""
    # [START job_search_custom_ranking_search_core]

    client = talent_v4beta1.JobServiceClient()

    # project_id = 'Your Google Cloud Project ID'
    # tenant_id = 'Your Tenant ID (using tenancy is optional)'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    if isinstance(tenant_id, six.binary_type):
        tenant_id = tenant_id.decode('utf-8')
    parent = client.tenant_path(project_id, tenant_id)
    domain = 'www.example.com'
    session_id = 'Hashed session identifier'
    user_id = 'Hashed user identifier'
    request_metadata = {
        'domain': domain,
        'session_id': session_id,
        'user_id': user_id
    }
    importance_level = enums.SearchJobsRequest.CustomRankingInfo.ImportanceLevel.EXTREME
    ranking_expression = '(someFieldLong + 25) * 0.25'
    custom_ranking_info = {
        'importance_level': importance_level,
        'ranking_expression': ranking_expression
    }
    order_by = 'custom_ranking desc'

    # Iterate over all results
    for response_item in client.search_jobs(
            parent,
            request_metadata,
            custom_ranking_info=custom_ranking_info,
            order_by=order_by):
        print('Job summary: {}'.format(response_item.job_summary))
        print('Job title snippet: {}'.format(response_item.job_title_snippet))
        job = response_item.job
        print('Job name: {}'.format(job.name))
        print('Job title: {}'.format(job.title))

    # [END job_search_custom_ranking_search_core]


# [END job_search_custom_ranking_search]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--project_id',
                        type=str,
                        default='Your Google Cloud Project ID')
    parser.add_argument('--tenant_id',
                        type=str,
                        default='Your Tenant ID (using tenancy is optional)')
    args = parser.parse_args()

    sample_search_jobs(args.project_id, args.tenant_id)


if __name__ == '__main__':
    main()