import aws_cdk as core
import aws_cdk.assertions as assertions

from cfdb.storage_stack import StorageStack


def test_raw_data_bucket_created():
    app = core.App()
    stack = StorageStack(app, "storage")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        "AWS::S3::Bucket", {"VersioningConfiguration": {"Status": "Enabled"}}
    )

    # Verify RemovalPolicy and AutoDeleteObjects indirectly
    template.resource_count_is("AWS::S3::Bucket", 1)
    template.has_resource(
        "AWS::S3::Bucket", {"DeletionPolicy": "Delete", "UpdateReplacePolicy": "Delete"}
    )
