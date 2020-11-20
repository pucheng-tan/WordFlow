from managements.application_management import ApplicationManagement
from services.challenge_service import ChallengeService
from random import randint

class ChallengeManagement(ApplicationManagement):

    _service = ChallengeService()

    def get_random_challenge_content(self, mode=0, min_char_count=None):
        # first, check if we've already counted the documents in that collection this session
        
        # if so, grab that number. If not, calculate it
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
