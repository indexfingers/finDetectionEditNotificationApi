from flask_restful import Resource, reqparse
from models.finDetectionEditNotification import FinDetectionEditNotificationModel


class FinDetectionEditNotification(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('encounterId',
        type=str,
        required=True,
        help = 'this field cannot be left blank'
    )
    parser.add_argument('detectionUrl',
        type=str,
        required=True,
        help = 'this field cannot be left blank'
    )
    # parser.add_argument('detectionData',
    #     type=str,
    #     required=True,
    #     help = 'this field cannot be left blank'
    # )

    # @jwt_required()
    def get(self,mediaAssetUuid):
        finDetectionEditNotification = FinDetectionEditNotificationModel.find_by_mediaAssetUuid(mediaAssetUuid)
        if finDetectionEditNotification:
            return finDetectionEditNotification.json()
        else:
            return {'message': 'finDetectionEditNotification not found'},404


    def delete(self,mediaAssetUuid):
        finDetectionEditNotification = FinDetectionEditNotificationModel.find_by_mediaAssetUuid(mediaAssetUuid)
        if finDetectionEditNotification:
            finDetectionEditNotification.delete_from_db()
            return {'message': 'finDetectionEditNotification deleted'}


    def post(self, mediaAssetUuid):
        if FinDetectionEditNotificationModel.find_by_mediaAssetUuid(mediaAssetUuid):
            return {'message': 'A finDetectionEditNotification with mediaAssetUuid {} already exists.'.format(mediaAssetUuid)}, 400
        data = FinDetectionEditNotification.parser.parse_args()
        finDetectionEditNotification  = FinDetectionEditNotificationModel(mediaAssetUuid, **data)

        try:
            finDetectionEditNotification.save_to_db()
        except:
            return {'message': 'an error occurred inserting the finDetectionEditNotification'}, 500 # internal server error

        return finDetectionEditNotification.json(), 201





    def put(self, mediaAssetUuid):
        data = FinDetectionEditNotification.parser.parse_args()
        finDetectionEditNotification = FinDetectionEditNotificationModel.find_by_mediaAssetUuid(mediaAssetUuid)
        if finDetectionEditNotification is None:
            finDetectionEditNotification = FinDetectionEditNotificationModel(mediaAssetUuid,**data)
        else:
            finDetectionEditNotification.encounterId = data['encounterId']
            finDetectionEditNotification.detectionUrl = data['detectionUrl']
        try:
            finDetectionEditNotification.save_to_db()
        except:
            return {'message': 'an error occurred inserting the finDetectionEditNotification'}, 500 # internal server error
        return finDetectionEditNotification.json()



class FinDetectionEditNotifications(Resource):
    def get(self):
        finDetectionEditNotifications = FinDetectionEditNotificationModel.query.all()
        finDetectionEditNotificationsJson = [finDetectionEditNotification.json() for finDetectionEditNotification in finDetectionEditNotifications]

        return {'finDetectionEditNotifications':finDetectionEditNotificationsJson}
