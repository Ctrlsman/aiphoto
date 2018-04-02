# coding:utf-8
import datetime
import calendar



class UserModel:
    __tablename__ = 'user'

    repay_day = 8

    @classmethod
    def repay_date(cls, date=None):
        '''
        计算下月还款日
        :return:
        '''
        if not date:
            date = datetime.datetime.now()
        month = 1 if date.month == 12 else date.month + 1
        year = date.year + 1 if date.month == 12 else date.year
        if date.day > 29 and month in [2, 4, 6, 9, 11]:
            repay_day = calendar.monthrange(year, month)[1]
        else:
            repay_day = date.day if not cls.repay_day else cls.repay_day
        return datetime.datetime.strptime(
            '%s-%s-%s %s:%s:%s' % (year, month, repay_day, date.hour, date.minute, date.second), '%Y-%m-%d %H:%M:%S')

    @classmethod
    def bill_date(cls, date=None):
        '''
        计算下月账单日
        :return:
        '''
        if not date:
            date = datetime.datetime.now()
        repay_day = cls.repay_date(date)
        return repay_day + datetime.timedelta(days=-10)

    def current_month_repay_date(self, date=None):
        '''
        返回下单日对应的还款日和账单日
        :param date:下单日
        :return:
        '''
        if not date:
            date = datetime.datetime.now()
        if not self.repay_day:
            repay_date = UserModel.repay_date(date)
            bill_date = UserModel.bill_date(date)
            return repay_date, bill_date

        day = self.repay_day
        month = date.month
        year = date.year
        loan_date = date
        if day == 31 and month in [4, 6, 9, 11]:
            day = 30
        if day > 28 and month == 2:
            day = calendar.monthrange(year, month)[1]
        if month == 1:
            month = 12
            year -= 1
        tmp_date = datetime.datetime.strptime(
            '%s-%s-%s %s:%s:%s' % (year, month - 1, day, date.hour, date.minute, date.second), '%Y-%m-%d %H:%M:%S')
        while True:
            start_bill_date = tmp_date + datetime.timedelta(days=-10)
            next_repay_date = UserModel.repay_date(tmp_date)
            next_bill_date = UserModel.bill_date(tmp_date)
            tmp_date = next_repay_date
            if start_bill_date < loan_date <= next_bill_date:
                return next_repay_date, next_bill_date


def create_bill(now_time=None, stage=3):
    now_time = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S') if now_time else datetime.datetime.now()
    tmp_repay_date = None
    user = UserModel()
    try:
        for i in range(int(stage)):
            if i == 0:
                repay_date = tmp_repay_date = user.current_month_repay_date(now_time)[0]
                statement_date = user.current_month_repay_date(now_time)[1]
            else:
                repay_date = UserModel.repay_date(tmp_repay_date)
                statement_date = UserModel.bill_date(tmp_repay_date)
                tmp_repay_date = UserModel.repay_date(tmp_repay_date)
            print(repay_date, statement_date)
    except Exception as e:
        print(e)
        pass


create_bill()