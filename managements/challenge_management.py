from managements.application_management import ApplicationManagement
from services.challenge_service import ChallengeService
from random import randint
import datetime

class ChallengeManagement(ApplicationManagement):

    _service = ChallengeService()

    def save_challenge_results(self, correct_words, incorrect_words, total_words, duration, mode):

        wpm = round((correct_words / duration)*60,1)
        accuracy = round((correct_words / total_words) * 100,1)

        challenge_results = {
            "wpm": wpm,
            "accuracy": accuracy,
            "date_completed": datetime.datetime.utcnow(),
            "duration": duration,
            "mode": mode,
        }

        # get context data
        school_id = ChallengeManagement._context.get_school_id()
        user_id = ChallengeManagement._context.get_user_uid()

        # TODO: Validate the challenge results in any way? Not sure if necessary as no user input

        response = self._service.save_challenge_results(school_id, user_id, challenge_results)
        challenge_results["response"] = response
        return challenge_results

    def get_my_challenge_history(self, limit=10, start_time=None):
        """Returns the challenge history of the current user.
        Limit is mandatory to avoid excessive reads.
        """
        # get context data
        school_id = ChallengeManagement._context.get_school_id()
        user_id = ChallengeManagement._context.get_user_uid()

        # ask the service to get the challenges
        return ChallengeManagement._service.get_challenge_results_by_user(school_id, user_id, limit=limit, start_at=start_time)

    def get_random_challenge_content(self, mode=0):
        """Gets a challenge content text belonging to a particular challenge mode.
        Will pick a random one.
        """
        # first, check if we've already counted the documents in that collection this session        
        # if so, grab that number. If not, calculate it and save it for next time.
        attribute_name = "mode_" + str(mode) + "_count"
        if hasattr(self._context, attribute_name):
            # max_index here is *ZERO-BASED*
            max_index = getattr(self._context, attribute_name)
        else:
            max_index = self._service.get_mode_count(mode)
            setattr(self._context, attribute_name, max_index)

        # calculate a random number less/equal to the max_index
        request_index = randint(0, max_index)

        # then, make our call to get the challenge
        challenge_content = self._service.get_challenge_content(mode, request_index)
        return challenge_content
