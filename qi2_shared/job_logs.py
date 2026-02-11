import asyncio
import time
from typing import List, Optional

from compute_api_client import JobLogPage, JobsApi


async def poll_job_logs(
    jobs_api: JobsApi,
    job_id: int,
    expected_logs: Optional[int] = None,
    poll_interval: float = 5.0,
    timeout: float = 30.0,
) -> List[str]:
    """Poll job logs until expected_logs is reached or timeout expires."""
    total_logs: List[str] = []
    seen_timestamps: set[int] = set()
    next_start: Optional[int] = None

    start_time = time.monotonic()

    while time.monotonic() - start_time < timeout:
        log_page: JobLogPage = await jobs_api.get_job_logs_jobs_id_logs_get(
            job_id,
            start=next_start,
        )

        for logline in log_page.logs:
            if logline.timestamp not in seen_timestamps:
                seen_timestamps.add(logline.timestamp)
                total_logs.append(logline.line)

        if expected_logs is not None and len(total_logs) >= expected_logs:
            return total_logs

        if log_page.next_start:
            next_start = log_page.next_start

        await asyncio.sleep(poll_interval)

    return total_logs
