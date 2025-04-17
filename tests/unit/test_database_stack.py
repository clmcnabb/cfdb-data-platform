import aws_cdk as core
import aws_cdk.assertions as assertions

from cfdb.database_stack import DatabaseStack


def test_api_call_table_created():
    """Test the DynamoDB table creation in test environment (test=True)"""
    app = core.App()
    stack = DatabaseStack(app, "database", test=True)
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        "AWS::DynamoDB::Table",
        {
            "AttributeDefinitions": [
                {
                    "AttributeName": "id",
                    "AttributeType": "S",
                },
                {
                    "AttributeName": "timestamp",
                    "AttributeType": "S",
                },
            ],
            "KeySchema": [
                {
                    "AttributeName": "id",
                    "KeyType": "HASH",
                },
                {
                    "AttributeName": "timestamp",
                    "KeyType": "RANGE",
                },
            ],
            "BillingMode": "PAY_PER_REQUEST",
        },
    )

    # Verify removal policy is DESTROY in test environment
    template.has_resource(
        "AWS::DynamoDB::Table",
        {
            "DeletionPolicy": "Delete",
            "UpdateReplacePolicy": "Delete",
        },
    )
