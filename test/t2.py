# coding:utf-8

def _calculate_overdue_level(repay_time, today=None):
    if not today:
        today = datetime.date.today()
    if not isinstance(repay_time, datetime.date):
        repay_date = datetime.date.fromtimestamp(repay_time)
    else:
        repay_date = repay_time

    month_delta = 12 * (today.year - repay_date.year) + (today.month - repay_date.month)
    if month_delta == 0:
        return 1

    day = repay_date.day
    last_day = calendar.monthrange(today.year, today.month)[1]
    if day > last_day:
        day = last_day
    d = datetime.date(today.year, today.month, day)
    if (today - d).days > 0:
        month_delta += 1
    return month_delta


def get_overdue_level_change_time(sub_bill_id, overdue_level):
    sub_bill_value = base_model.redis_pool_get().hget('loan_ID', sub_bill_id)
    t = time.strftime('%Y-%m-%d', time.localtime(int(time.time())))
    if sub_bill_value:
        if str(sub_bill_value).split('|')[1] == str(overdue_level):
            return str(sub_bill_value).split('|')[0]
    base_model.redis_pool_get().hset('loan_ID', sub_bill_id, '|'.join([t, str(overdue_level)]))
    return t


v = hashlib.md5(str(bill.bill_id) + str(overdue_level) + overdue_level_change_time)