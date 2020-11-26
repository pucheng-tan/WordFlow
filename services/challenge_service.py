from services.api_service import API

class ChallengeService:

    api = None
    _CHALLENGE_CONTENT_PATH = "ChallengeContent/Modes/"

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
        path = ChallengeService._CHALLENGE_CONTENT_PATH + str(mode)
        order_by = [{"index": False}]
        limit = 1
        result = ChallengeService.api.get(path=path, order_by=order_by, limit=limit)
        return list(result.values())[0]["index"]

    def get_challenge_content(self, mode, request_index):
        """Returns a specific challenge's text content for typing.
        """
        path = ChallengeService._CHALLENGE_CONTENT_PATH + str(mode)
        where_clause = [["index", "==", request_index]]
        result = ChallengeService.api.get(path=path, where_clauses=where_clause)
        text_content = list(result.values())[0]["text_content"]
        return text_content

    def get_challenge_results_by_user(self, school_id, user_uid, sort={"date_completed": False}, limit=10, start_at=None):
        """Returns challenge results belonging to a specific user.
        This is built for pagination. The start_at refers to the sort field value to start at,
        either False for descending or True for ascending
        """
        where_clauses = []
        if start_at:
            sort_field = list(sort.keys())[0]
            # if sorting descending like sort={field:False}, we want values smaller than start_at value
            operator = ">" if sort[sort_field] else "<"
            clause = [sort_field, operator, start_at]
            where_clauses.append(clause)

        path = "Schools/" + school_id + "/UserProfiles/" + user_uid + "/History"
        return ChallengeService.api.get(path=path, limit=limit, order_by=[sort], where_clauses=where_clauses)
