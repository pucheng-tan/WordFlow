import pytest
from pytest_jsonreport.plugin import JSONReport, json_metadata
from datetime import datetime, timezone

from services.challenge_service import ChallengeService

service = ChallengeService()

METADATA_ID = "ChallengeService"

# test that we get the right mode count
@pytest.mark.api_call
def test_get_mode_count(json_metadata):
    json_metadata["id"] = "UT " + METADATA_ID + ".1"
    json_metadata["description"] = "Verify that the get_mode_count returns the correct data"

    # the mode "7" is not a real mode, it is only used for testing purposes
    # the data is static
    mode_count = service.get_mode_count(7)

    # there are 2 documents in the collection- so index should == 1
    assert mode_count == 1

    assert isinstance(mode_count, int) == True

# test that we retrieve the right content based on the passed-in mode and index
@pytest.mark.api_call
def test_get_challenge_content(json_metadata):
    json_metadata["id"] = "UT " + METADATA_ID + ".2"
    json_metadata["description"] = "Verify that the correct attribute/data is returned"

    text_content = service.get_challenge_content(7, 1)

    assert text_content == "test1"


# saving the results!
@pytest.mark.api_call
def test_save_challenge_results(json_metadata):
    json_metadata["id"] = "UT " + METADATA_ID + ".3"
    json_metadata["description"] = "Verify that data comes is saved as expected with additional fields included"

    school_id = "test_school"
    user_id = "test_user"
    challenge = {
        "date_completed": datetime(2020, 1, 1, 1, 1, 1, 1, tzinfo=timezone.utc),
        "mode": 7,
        "duration": 120,
        "wpm": 16,
        "accuracy": 12
    }
    # perform the post operation
    post_result_document = service.save_challenge_results(school_id, user_id, challenge)
    
    # test that the path is what is expected, as well as the id exists
    assert "id" in post_result_document
    expected_path = "Schools/" + school_id + "/UserProfiles/" + user_id + "/History/" + post_result_document["id"]
    assert post_result_document["path"] == expected_path    

    # get the data that was just posted
    get_path = post_result_document["path"]
    get_result = service.api.get(path=get_path)

    # the user_profile attribute should be created
    expected_user_profile = "Schools/" + school_id + "/UserProfiles/" + user_id
    assert get_result["user_profile"] == expected_user_profile

    # set the user_profile attribute in our "post" challenge, and compare for equality
    for attribute in ["mode", "duration", "wpm", "accuracy"]:
        assert challenge[attribute] == get_result[attribute]

    # the date is fussy because different datatypes. Compare them as timestamps instead.
    expected_timestamp = (challenge["date_completed"]).timestamp()
    actual_timestamp = (get_result["date_completed"]).timestamp()
    assert expected_timestamp == actual_timestamp



