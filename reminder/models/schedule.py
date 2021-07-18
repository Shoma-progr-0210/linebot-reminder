from datetime import datetime, timedelta

from reminder.database import db, ma
from reminder.models.base import Base

class Schedule(Base):
    __tablename__ = 'schedule'

    user_id = db.Column(db.String(50))
    name = db.Column(db.String(30))
    message = db.Column(db.String(255))
    time = db.Column(db.DateTime, nullable=False)
    label = db.Column(db.String(30))

    @classmethod
    def create(cls, user_id, name, message, time, label):
        """
        リマインドスケジュールを作成する
        :param user_id:
        :param name:
        :param message:
        :param time:
        :param label:
        :return: Schedule
        """
        obj = cls(user_id=user_id, name=name, message=message, time=time, label=label)
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def get_by_user_id(cls, user_id):
        """
        user_idを指定して登録済みスケジュールを取得
        :param user_id:
        :return: ユーザScheduleリスト
        """
        return db.session.query(cls).filter(cls.user_id == user_id).order_by(cls.time.asc()).all()
    
    @classmethod
    def get_by_time(cls, time):
        """
        時間を指定して登録済みスケジュールを取得
        :param time:
        :return: Scheduleリスト
        """
        return db.session.query(cls).filter(cls.time == time).all()

    # @classmethod
    # def get_all(cls):
    #     """
    #     全スケジュールを取得
    #     :return: 全Scheduleリスト
    #     """
    #     return db.session.query(cls).all()

    @classmethod
    def delete_by_id(cls, user_id):
        """
        user_idを指定してスケジュール削除
        :param user_id:
        :return: なし
        """
        obj = db.session.query(cls).filter(cls.user_id == user_id).first()
        db.session.delete(obj)
        db.session.commit()

    @classmethod
    def delete_by_time(cls, time):
        """
        時間を指定してスケジュール削除
        :param time:
        :return: 削除したスケジュール数
        """
        delete_count = db.session.query(cls).filter(cls.time < time).delete()
        db.session.commit()
        return delete_count


    def __init__(self, user_id, name, message, time, label):
        self.user_id = user_id
        self.name = name
        self.message = message
        self.time = time
        self.label = label

    def __repr__(self):
        return 'Schedule(id={0}, user_id={1}, name={2}, message={3}, time={4}, label={5})'.format(
            self.id, self.user_id, self.name, self.message, self.time, self.label
        )

class ScheduleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Schedule
        fields = ('id', 'user_id', 'name', 'message', 'time', 'label')
