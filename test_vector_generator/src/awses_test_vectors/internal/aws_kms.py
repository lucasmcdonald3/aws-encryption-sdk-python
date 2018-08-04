# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""
Helper utilities for interacting with AWS KMS.
"""
from aws_encryption_sdk.identifiers import AlgorithmSuite
from aws_encryption_sdk.key_providers.kms import KMSMasterKeyProvider

from awses_test_vectors.internal.defaults import ENCODING

# This lets us easily use a single boto3 client per region for all KMS master keys.
KMS_MASTER_KEY_PROVIDER = KMSMasterKeyProvider()


def arn_from_key_id(key_id):
    # type: (str) -> str
    """"""
    encrypted_data_key = KMS_MASTER_KEY_PROVIDER.master_key(key_id.encode(ENCODING)).generate_data_key(
        algorithm=AlgorithmSuite.AES_256_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384,
        encryption_context={}
    )
    return encrypted_data_key.key_provider.key_info.decode(ENCODING)
