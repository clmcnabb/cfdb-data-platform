from aws_cdk import (
    RemovalPolicy,
    # Duration,
    Stack,
)
from aws_cdk import (
    aws_s3 as s3,
)
from constructs import Construct


class StorageStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, *, test: bool = False, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Set removal policy and auto-delete based on test parameter
        removal_policy = RemovalPolicy.DESTROY if test else RemovalPolicy.RETAIN
        auto_delete = True if test else False

        # Raw landing zone s3 bucket
        raw_bucket = s3.Bucket(
            self,
            "RawDataBucket",
            versioned=True,
            removal_policy=removal_policy,
            auto_delete_objects=auto_delete,
        )

        # Processed data s3 bucket
        processed_bucket = s3.Bucket(
            self,
            "ProcessedDataBucket",
            versioned=True,
            removal_policy=removal_policy,
            auto_delete_objects=auto_delete,
        )

        self.raw_data_bucket = raw_bucket
        self.processed_data_bucket = processed_bucket
