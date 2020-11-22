from services.api_service import API

class ChallengeService:

    api = None

    def __init__(self):
        if not ChallengeService.api:
            ChallengeService.api = API.get_api()

    def save_challenge_results(self, school_id, user_id, challenge):
        """ Saves the challenge results belonging to the specific school/user.
        Does not do any kind of validation on the challenge, that should be completed before getting to this point.
        """
        challenge["user_profile"] = "Schools/" + school_id + "/UserProfiles/" + user_id
        path = challenge["user_profile"] + "/History"
        
        response = ChallengeService.api.post(path=path, data=challenge)
        return response["document"]

    def get_mode_count(self, mode):
        """Counts how many documents are in a particular mode collection.
        All of those documents are expected to have a incrementing index field.
        Just finds the document with the highest index and returns the index.
        Index is 0-based, so it's technically the count - 1.
        """
        path = "ChallengeContent/Modes/" + str(mode)
        order_by = [{"index": False}]
        limit = 1
        result = ChallengeService.api.get(path=path, order_by=order_by, limit=limit)
        return list(result.values())[0]["index"]

    def get_challenge_content(self, mode, request_index):
        """Returns a specific challenge's text content for typing.
        """
        path = "ChallengeContent/Modes/" + str(mode)
        where_clause = [["index", "==", request_index]]
        result = ChallengeService.api.get(path=path, where_clauses=where_clause)
        text_content = list(result.values())[0]["text_content"]
        return text_content