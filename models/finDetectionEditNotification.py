from db import db

class FinDetectionEditNotificationModel(db.Model):
    __tablename__ = 'finDetectionEditNotifications'

    id = db.Column(db.Integer, primary_key = True)
    mediaAssetUuid = db.Column(db.String(80))
    encounterId = db.Column(db.String(80))
    detectionUrl = db.Column(db.String(80))

    # store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # store = db.relationship('StoreModel')

    def __init__(self,mediaAssetUuid,encounterId,detectionUrl):
        self.mediaAssetUuid = mediaAssetUuid
        self.encounterId = encounterId
        self.detectionUrl = detectionUrl

    def json(self):
        return {'mediaAssetUuid': self.mediaAssetUuid, 'encounterId': self.encounterId, 'detectionUrl': self.detectionUrl }


    # useful for insertion and updating
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_mediaAssetUuid(cls,mediaAssetUuid):
        return cls.query.filter_by(mediaAssetUuid=mediaAssetUuid).first() # SELECT * FROM items WHERE name=name LIMIT 1 - returnsd first row only. also converts data to item model object
