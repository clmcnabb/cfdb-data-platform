from aws_cdk import (
    RemovalPolicy,
    Stack,
)
from aws_cdk import (
    aws_dynamodb as dynamodb,
)
from constructs import Construct


class DatabaseStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, *, test: bool = True, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a DynamoDB table
        api_call_table = dynamodb.Table(
            self,
            "ApiCallTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING,
            ),
            sort_key=dynamodb.Attribute(
                name="timestamp",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY if test else RemovalPolicy.RETAIN,
        )

        self.api_call_table = api_call_table
