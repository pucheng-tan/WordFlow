
import pytest
from pytest_jsonreport.plugin import JSONReport, json_metadata
from datetime import datetime, timezone

import challenge_management
from services import context_service

# constant values, use a test user
USER_UID = "T1b5iP7q96YBnaPDRuEN8c5Arwh1"
SCHOOL_ID = "3p1U6xAvKic1RvXMl5nJ"
EMAIL = "1123@gmail.com"
METADATA_ID = "ChallengeService"

# initialize things
CM = challenge_management.ChallengeManagement()
cxt = context_service.ContextService.get_instance()
cxt.set_user(0, USER_UID, SCHOOL_ID, email=EMAIL)
CM._context = cxt

@pytest.mark.api_call
def test_get_my_challenges(json_metadata):
    json_metadata["id"] = "UT " + METADATA_ID + ".1"
    json_metadata["description"] = "Get the first 2 pages of challenge results and verify that they are as expected"
    limit = 2
    # get the first page of challenges
    results_1 = CM.get_my_challenge_history(limit=limit)

    # we should get the number of results we asked for
    assert len(results_1.values()) == limit

    # then, get the second page of results
    # pass in the oldest time from the first page so it knows where to start
    oldest_result = list(results_1.values())[limit - 1]

    # stop here if we don't have a date_completed in the result!
    assert "date_completed" in oldest_result
    start_at = oldest_result["date_completed"]

    # then use that to paginate
    results_2 = CM.get_my_challenge_history(limit=limit, start_time=start_at)

    # all of the dates in the first page should be > than those of the second
    for key, newer_result in results_1.items():
        for old_key, older_result in results_2.items():
            assert newer_result["date_completed"].timestamp() > older_result["date_completed"].timestamp()


@pytest.mark.api_call
def test_get_my_challenges_last_page(json_metadata):
    json_metadata["id"] = "UT " + METADATA_ID + ".2"
    json_metadata["description"] = "See what happens when we make calls to paginate when there's no more data"

    # there will never be any data before the beginning of time.
    beginning_of_time = datetime.min

    # make the call
    results = CM.get_my_challenge_history(start_time=beginning_of_time)

    # should get an empty object, not any type of exception.
    assert results == {}