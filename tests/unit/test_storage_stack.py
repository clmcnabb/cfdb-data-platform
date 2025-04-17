import aws_cdk as core
import aws_cdk.assertions as assertions

from cfdb.storage_stack import StorageStack


def test_raw_data_bucket_created():
    app = core.App()
    stack = StorageStack(app, "storage")
    template = assertions.Template.from_stack(stack)

    # Test basic bucket configuration
    template.has_resource_properties(
        "AWS::S3::Bucket",
        {
            "VersioningConfiguration": {"Status": "Enabled"},
            "LifecycleConfiguration": {
                "Rules": [
                    {
                        "Status": "Enabled",
                        "Transitions": [
                            {
                                "StorageClass": "INTELLIGENT_TIERING",
                                "TransitionInDays": 90,
                            },
                            {"StorageClass": "DEEP_ARCHIVE", "TransitionInDays": 180},
                        ],
                    }
                ]
            },
        },
    )

    # Verify we have two buckets (raw and processed)
    template.resource_count_is("AWS::S3::Bucket", 2)

    # Verify both buckets have the same lifecycle rules
    template.all_resources_properties(
        "AWS::S3::Bucket",
        {
            "LifecycleConfiguration": {
                "Rules": [
                    {
                        "Status": "Enabled",
                        "Transitions": [
                            {
                                "StorageClass": "INTELLIGENT_TIERING",
                                "TransitionInDays": 90,
                            },
                            {"StorageClass": "DEEP_ARCHIVE", "TransitionInDays": 180},
                        ],
                    }
                ]
            }
        },
    )

    # Verify RemovalPolicy and AutoDeleteObjects
    template.has_resource(
        "AWS::S3::Bucket", {"DeletionPolicy": "Delete", "UpdateReplacePolicy": "Delete"}
    )
