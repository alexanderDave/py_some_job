# -*- coding: UTF-8 -*-

import mWeb.baseutils.DAO.DbHelper                              as DbHelper

# airent_new_2017
e_trade = ['id','id_user','sum','origin_contract_charge','installments_sum','first_installment_price','per_installment_price','mp_service_id','stock_origin_price','ahs_subsidies','lbf_price','price_per_installments_without_lbf_price','extra_price','trade_no','dt_updated','choose_installments_num','pre_installments_num','days_per_installments','min_installments_num','max_installments_num','price_per_installments_all','status','dt_created','pay_end_time','dt_take_effect','assurance_sum','origin_assurance_charge','dt_service_start_date','user_name','user_identi_card','is_free','lbf_terms','channel_id','utm_source','utm_medium','utm_campaign','dt_return','dt_signed','dt_end_date','total_installments_number','dt_service_end_date','residual_value','cash','freeze_cash','is_reduce','version','origin_first_month_amount','origin_per_month_amount','is_send_pay_success_mes','flag','contract_no']
e_trade_extend = ['id','trade_no','user_phone','dt_created','is_active','ab_test','return_amount','risk_control_approve_employee_id','is_auto_rent','rent_installments','rent_amount','buyout_fee','is_buyout','is_used_buyout','is_returnflow','consumer_id','manager_id','ka_id','store_id','imei_img','identi_front_img','identi_behand_img','identi_hand_img','flow_code','dt_updated','risk_status','can_refund_beyond_limitation','approve_reason','open_rent_date','fund_channel','delivery_type','pread_rent_price','trade_type','trade_product_type','trade_risk_channel','pay_status','trade_user_tran_id','trade_user_role','return_sign_show','late_rule']

# xhj_trade
e_trade_extend_sharding = ['id','trade_no','user_phone','dt_created','is_active','ab_test','return_amount','risk_control_approve_employee_id','is_auto_rent','rent_installments','rent_amount','buyout_fee','is_buyout','is_used_buyout','is_returnflow','consumer_id','manager_id','ka_id','store_id','imei_img','identi_front_img','identi_behand_img','identi_hand_img','flow_code','dt_updated','risk_status','can_refund_beyond_limitation','approve_reason','open_rent_date','fund_channel','delivery_type','pread_rent_price','trade_type']

# biz_contract
e_bill_sharding = []

class Tables(object):
    
    def __init__(self,trade_no):
        self.db = DbHelper.DB()
        self.tradeno =trade_no
        self.fenbiao = None
        self.odd = None
        self.contract_no = None
    
    # airent_new_2017.e_trade e_trade_extend
    def get_e_trade(self):
        
        self.db.connDb('airent_new_2017')
        mtuples = self.db.select_one("SELECT * FROM e_trade WHERE trade_no ='{0}' limit 1;".format(self.tradeno))
        self.db.closeDb()
        result = transform(e_trade,mtuples)
        if result:
            self.id_user = result['id_user']
            self.odd = 2 if(result['id_user']%2 == 0) else 1
            self.contract_no = result['contract_no']
            return result
        return False

    # airent_new_2017.e_trade e_trade_extend
    def get_e_trade_extend(self):

        self.db.connDb('airent_new_2017')
        mtuples = self.db.select_one('SELECT * FROM e_trade_extend WHERE trade_no = "{0}" limit 1;'.format(self.tradeno))
        print(mtuples)
        self.db.closeDb()
        return transform(e_trade_extend,mtuples)

    def get_e_trade_extend_sharding(self):
        
        self.db.connDb('xhj_trade')
        # mtuples = db.select_one('SELECT * FROM e_trade_extend_sharding_{1} WHERE trade_no = {0}'.format(self.tradeno),lambda if self.id_user%5 == 0: 5 else:self.id_user%5 ))
        mtuples = self.db.select_one('SELECT * FROM e_trade_extend_sharding_{1} WHERE trade_no = "{0}" limit 1;'.format(self.tradeno),self.id_user%5 )
        self.db.closeDb()
        return transform(e_trade_extend_sharding,mtuples)


    def updates(self,dbname,table,name,value,wherename,wherevalue):
        
        self.db.connDb(dbname)
        sql = "UPDATE {0} SET {1}={2} WHERE {3}={4};".format(table,name,value,wherename,wherevalue)
        self.db.update(sql)
        pass

def transform(lists,mtuples):
    if None == mtuples:
        print("通过sql获取数据的结果为空")
        return False
    if (len(lists)!= len(mtuples)):
        print("表结构拼接失败，原因list的长度为{0}和数据长度：{1}不一致。".format(str(len(lists)),str(len(mtuples))))
        return False
    i = 0
    result = {}
    for names in lists:
        result[names] = mtuples[i]
        i = i + 1
    return result

if __name__ == "__main__":
    print("test gose here:")
    