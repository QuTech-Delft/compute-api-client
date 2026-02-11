import time
from unittest.mock import AsyncMock

import pytest

from compute_api_client import JobLogLine, JobLogPage, JobsApi
from qi2_shared.job_logs import poll_job_logs


@pytest.fixture
def jobs_api() -> AsyncMock:
    return AsyncMock(spec=JobsApi)


async def test_polling_stops_when_expected_logs_arrived(jobs_api: AsyncMock) -> None:
    # Arrange
    jobs_api.get_job_logs_jobs_id_logs_get.side_effect = [
        JobLogPage(
            logs=[
                JobLogLine(timestamp=1, line="log-1"),
                JobLogLine(timestamp=2, line="log-2"),
            ],
            next_start=3,
        ),
        JobLogPage(
            logs=[
                JobLogLine(timestamp=3, line="log-3"),
            ],
            next_start=None,
        ),
    ]

    # Act
    logs = await poll_job_logs(
        jobs_api=jobs_api,
        job_id=123,
        expected_logs=3,
        poll_interval=0.01,
        timeout=1.0,
    )

    # Assert
    assert logs == ["log-1", "log-2", "log-3"]
    assert jobs_api.get_job_logs_jobs_id_logs_get.call_count == 2


async def test_polling_exits_after_timeout(
    jobs_api: AsyncMock,
) -> None:
    # Arrange
    jobs_api.get_job_logs_jobs_id_logs_get.return_value = JobLogPage(
        logs=[],
        next_start=None,
    )

    start = time.monotonic()

    # Act
    logs = await poll_job_logs(
        jobs_api=jobs_api,
        job_id=123,
        expected_logs=None,
        poll_interval=0.01,
        timeout=0.05,
    )

    elapsed = time.monotonic() - start

    # Assert
    assert not logs
    assert elapsed >= 0.05
    assert jobs_api.get_job_logs_jobs_id_logs_get.call_count >= 1
