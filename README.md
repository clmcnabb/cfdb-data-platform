# Sports Data Platform CDK Project

This project defines an AWS Cloud Development Kit (CDK) application for a sports data platform. The platform includes:

* An S3 bucket for raw JSON data.
* An S3 bucket for processed Parquet data.
* A DynamoDB table to log API calls per month.
* A Lambda function to ingest data via API calls.
* An AWS Glue crawler to infer schemas and convert JSON to Parquet.
* An Athena workgroup for SQL querying of Parquet data.

The project uses Python and `uv` for dependency management. The `cdk.json` file configures the CDK Toolkit to execute the app.

## Prerequisites

* **Python 3.12+** : Ensure `python3` is installed and accessible in your PATH.
* **uv** : Install `uv` for dependency and environment management. See [uv documentation](https://docs.astral.sh/uv/) for installation instructions.
* **AWS CLI** : Configure with valid credentials and a default region (e.g., `us-east-1`).
* **AWS CDK CLI** : Install globally with `npm install -g aws-cdk`.

## Setting up the project

Navigate to the project root directory and initialize the `uv` environment:

```bash
$ uv sync
```

This command creates a virtual environment (in `.venv`) and installs dependencies listed in `pyproject.toml`, locking versions in `uv.lock` for reproducibility.

To activate the virtual environment on MacOS or Linux:

```bash
$ source .venv/bin/activate
```

On Windows:

```bash
> .venv\Scripts\activate.bat
```

Alternatively, use `uv run` to execute commands within the `uv`-managed environment without activating the virtual environment.

## Synthesizing the CloudFormation template

To synthesize the CloudFormation templates for the stacks:

```bash
$ uv run cdk synth
```

This generates templates in the `cdk.out/` directory.

## Deploying the stacks

To deploy all stacks to your AWS account:

```bash
$ uv run cdk deploy --all
```

Use `--require-approval never` for automated deployments (e.g., in CI/CD pipelines).

## Adding dependencies

To add dependencies (e.g., additional CDK libraries):

```bash
$ uv add aws-cdk-lib
```

For development dependencies (e.g., `pytest`, `flake8`):

```bash
$ uv add --group dev pytest
```

After adding dependencies, sync the environment:

```bash
$ uv sync
```

## Running tests

Unit tests are located in `cfdb/tests/` and `tests/unit/`. To run tests:

```bash
$ uv run pytest
```

To run linters for code quality:

```bash
$ uv run flake8 .
```

## Project structure

* `app.py`: Entry point for the CDK application.
* `cfdb/`: Contains stack definitions (e.g., `storage_stack.py`) and tests.
* `tests/`: Contains unit tests (e.g., `tests/unit/test_storage_stack.py`).
* `pyproject.toml`: Defines project dependencies and configuration.
* `uv.lock`: Locks dependency versions.
* `cdk.json`: Configures the CDK Toolkit.

## Useful commands

* `uv run cdk ls`          List all stacks in the app.
* `uv run cdk synth`       Emit the synthesized CloudFormation templates.
* `uv run cdk deploy`      Deploy stacks to your AWS account/region.
* `uv run cdk diff`        Compare deployed stacks with current state.
* `uv run cdk docs`        Open CDK documentation.

## Troubleshooting

* Ensure `uv` is installed (`uv --version`).
* Verify AWS credentials (`aws sts get-caller-identity`).
* Check `pyproject.toml` for correct dependencies.
* If tests fail, ensure the `uv`-managed environment is active and dependencies are installed (`uv sync`).

Enjoy building your sports data platform!
