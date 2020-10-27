from api_service import APIService

class ChallengeService(APIService):

    CONTENT_COLLECTION = "ChallengeContent"
    SCHOOL_ID = 'o2lTSAI6X4yGdIZ0huB9'

    def get_matching_challenge_results(self, params):
        # temp_params = {'assigned': True, 'user_id': 'BMSoKUzVnRYn103t2Oi6Nacv9X03'}
        # Look in Schools collection with reference o2, look in UserProfiles collection for reference BM, 
        # look in History collection for all records where AssignmentID exists and is non empty
        # query = {'Schools': {'reference': 'o2lTSAI6X4yGdIZ0huB9', 'UserProfiles': {'reference': 'BMSoKUzVnRYn103t2Oi6Nacv9X03', 'History': {'AssignmentID': True}}} }
        
        # school = self.get_db().collection('Schools').document(self.SCHOOL_ID)
        # user = school.collection('UserProfiles').document('BMSoKUzVnRYn103t2Oi6Nacv9X03')
        # not in filters out where field does not exist
        # history = user.collection('History').where('AssignmentID', '>', '').stream()

        history = self.get_db().collection('Schools').document(self.SCHOOL_ID).collection('UserProfiles').document('BMSoKUzVnRYn103t2Oi6Nacv9X03').collection('History').order_by('AssignmentID').stream()

        
        # for doc in history:
        #     print(f'{doc.id} => {doc.to_dict()}')

        # collections = self._db.collection(collection).document(document).collections()
        # for collection in collections:
        #     for doc in collection.stream():
        #         print(f'{doc.id} => {doc.to_dict()}')
        # query = self.get_db().collection('Schools').document('o2lTSAI6X4yGdIZ0huB9').collections()
        return history
