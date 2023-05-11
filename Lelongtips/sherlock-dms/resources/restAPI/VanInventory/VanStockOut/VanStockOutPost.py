import secrets
from datetime import datetime

from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Config.ReferenceData.ReasonType.ReasonGet import ReasonGet
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route.RouteGet import RouteGet
from resources.restAPI.WarehouseInventory.InventoryList.InventoryListGet import InventoryListGet
from setup.hanaDB.HanaDB import HanaDB

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL


class VanStockOutPost(object):
    @keyword("user pump db to generate van stock out data with open status")
    def user_pumps_to_db_for_van_stock_out(self):

        payload = self.pump_data()


    def pump_data(self):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        # HanaDB().connect_database_to_environment()
        tenant_id = "5B4FEB776C454F9E9F28A6E3D1780EE8"

        InventoryListGet().user_retrieves_inventory_summary_for_all_warehouse()
        whs_list = BuiltIn().get_variable_value("${whs_list}")
        # whs_with_codes =
        # van_whs_with_qty = [whs for whs in whs_list if (whs.get('WAREHOUSE_CODE', 'xx')[-2:] == "-G" or (whs.get('WAREHOUSE_CODE', 'xx')[-2:] == "-B")) and int(float(whs['QTY_AVAILABLE_BASE'])) > 5]
        van_whs_with_qty_ids_type = [[whs['WAREHOUSE_ID'], whs.get('WAREHOUSE_CODE', 'xx')[-2:]]
                                     for whs in whs_list if (whs.get('WAREHOUSE_CODE', 'xx')[-2:] == "-G" or
                                                             (whs.get('WAREHOUSE_CODE', 'xx')[-2:] == "-B")) and
                                     int(float(whs['QTY_AVAILABLE_BASE'])) > 5 ] #and whs['DIST_ID'] == distributor_id]
        van_whs_with_qty_ids = [i[0] for i in van_whs_with_qty_ids_type]
        RouteGet().user_gets_all_route_data()
        route_rs_body = BuiltIn().get_variable_value("${route_rs_body}")
        routes_with_van_whs = [route for route in route_rs_body if ('VAN_WHS' in route.keys() and route['SALES_PERSON'] is not None and
                                                                    (route['VAN_WHS']['GOOD']['ID'] in van_whs_with_qty_ids or
                                                                     route['VAN_WHS']['BAD']['ID'] in van_whs_with_qty_ids))]

        # rand_route = secrets.randbelow(len(routes_with_van_whs))
        # rand_route_details = routes_with_van_whs[rand_route]
        whs_id = None
        van_whs_type_ss = None
        route_details = None
        for route in routes_with_van_whs:
            if route['VAN_WHS']['GOOD']['ID'] in van_whs_with_qty_ids:
                whs_id = route['VAN_WHS']['GOOD']['ID']
                van_whs_type_ss = "GOOD"
                route_details = route
                break
            elif route['VAN_WHS']['BAD']['ID'] in van_whs_with_qty_ids:
                whs_id = route['VAN_WHS']['BAD']['ID']
                van_whs_type_ss = "BAD"
                route_details = route
                break
        assert route_details is not None, "Please setup data, no suitable route and whs with available inventory found"



        # rand_whs = secrets.randbelow(len(van_whs_with_qty_ids))
        # rand_whs_id = van_whs_with_qty_ids[rand_whs]
        # van_whs_type = None
        # rand_route = None
        stk_type = None

        # for i in van_whs_with_qty_ids_type:
        #     if i[0] == rand_whs_id:
        #         van_whs_type_ss = i[1]
        #         break

        if van_whs_type_ss == "GOOD":
            van_whs_type = "GOOD"
            rsn_type = "OG"
            stk_type = "G"
        elif van_whs_type_ss == "BAD":
            van_whs_type = "BAD"
            rsn_type = "OB"
            stk_type = "B"

        # for route in routes_with_van_whs:
        #     if route['VAN_WHS'][van_whs_type]['ID'] == rand_whs_id:
        #         rand_route = route
        #         print("randroute0 " + str(route))
        #         break
        # print("randroute1 " + str(rand_route))
        # print("randroute2 " + str(whs_id))
        rand_sp_id = route_details['SALES_PERSON']
        rand_route_id = route_details['ID']
        # rand_van_whs_with_qty_ids_type = next((i for i in van_whs_with_qty_ids_type if i[0]['ID'] == rand_whs_id), None)
        # rout
        # route_details = next((route for route in van_whs_routes if route['ID'] == rand_sp_route_id), None)
        # print("chosen6 " + str(route_details))

        # rand_sp_whs_details_id = [i for i in routes_with_van_whs['ID'] == rand_sp_route_id]

        # rand_sp_whs_details = next(van_whs for van_whs in route_details['VAN_WHS'] if van_whs['ID'] in van_whs_routes_whs)
        # rand_sp_whs_details = next((route['ID'] for whs in van_whs_routes_whs if route['ID'] == rand_sp_route_id), None)
        # rand_sp_whs_id = rand_sp_whs_details['ID']
        other_whs_id = next((whs['WAREHOUSE_ID'] for whs in whs_list if whs['WAREHOUSE_ID'] != whs_id),None)

        ReasonGet().user_retrieves_all_reasons_for_all_operations()
        rsn_all_ops_ls = BuiltIn().get_variable_value("${rsn_all_ops_ls}")

        # whs_type = rand_sp_whs_details['WAREHOUSE_CODE'][-2:]

        rsn_for_vso_id = next((rsn['ID'] for rsn in rsn_all_ops_ls if rsn['REASON_TYPE_CD'] == rsn_type), None)
        BuiltIn().set_test_variable("${res_bd_reason_type_id}", rsn_for_vso_id)
        ReasonGet().user_retrieves_all_reasons()
        rsn_ls = BuiltIn().get_variable_value("${rsn_ls}")
        rand_rsn = secrets.choice(rsn_ls)
        rsn_id = rand_rsn['ID']

        now = datetime.today().strftime('%Y-%m-%d')
        query = "INSERT INTO TXN_VANTRFOUTHDR(ID,TENANT_ID,DIST_ID," \
                "ROUTE_ID,TXN_NO,TXN_DT,WHS_ID_FROM,WHS_ID_TO,STOCK_TYPE,REASON_ID,STATUS," \
                "REMARK,PRN_NO,PRIME_FLAG,HHT_SUBMIT_DT,HHT_CREATED_BY,TXN_CREATED_DT," \
                "IS_DELETED,CREATED_DATE,CREATED_BY,MODIFIED_DATE,MODIFIED_BY,VERSION) VALUES(hex('{0}'),'{1}','{2}','{3}'," \
                "'{4}','{5}','{6}','{7}','{8}'," \
                "'{9}','{10}','{11}',{12},'{13}','{14}','{15}','{16}',{17}" \
                ",'{18}','{19}','{20}','{21}',{22})".format(''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(20)),
                                                    tenant_id, dist_id, rand_route_id,
                                                    'TFONFVS' + ''.join(secrets.choice('0123456789') for _ in range(12)),
                                                    now, whs_id, other_whs_id, stk_type, rsn_id, "P", "null", 0, 'PRIME',
                                                    now, rand_sp_id, now, "false", now, rand_sp_id,
                                                    now, rand_sp_id, 1)
        data = [
            # ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(15)),
                                                    tenant_id, dist_id, rand_route_id,
                                                    'TFONFVS' + ''.join(secrets.choice('0123456789') for _ in range(12)),
                                                    now, whs_id, other_whs_id, stk_type, rsn_id, "P", "null", 0, 'PRIME',
                                                    now, rand_sp_id, now, False, now, rand_sp_id,
                                                    now, rand_sp_id, 1]

        # query = "INSERT INTO TXN_VANTRFOUTHDR VALUES(" \
        #     "/*ID <VARBINARY>*/,"\  #''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(40))
        #     "/*TENANT_ID <VARBINARY>*/,"\ #tenant_id
        #     "/*DIST_ID <VARBINARY>*/,"\ #dist_id
        #     "/*ROUTE_ID <VARBINARY>*/,"\ #sp_van_route['ID']
        #     "/*TXN_NO <NVARCHAR(30)>*/,"\ #TFONFVS + ''.join(secrets.choice('0123456789') for _ in range(12))
        #     "/*TXN_DT <DATE>*/,"\  #now
        #     "/*WHS_ID_FROM <VARBINARY>*/,"\ #sp_van_whs['ID']
        #     "/*WHS_ID_TO <VARBINARY>*/,"\ # random_whs
        #     "/*STOCK_TYPE <NCHAR(1)>*/,"\ # stk_type
        #     "/*REASON_ID <VARBINARY>*/,"\ #rsn_id
        #     "/*STATUS <NCHAR(1)>*/,"\ #P/S
        #     "/*REMARK <NVARCHAR(50)>*/,"\ #null
        #     "/*PRN_NO <INTEGER>*/,"\ #0
        #     "/*PRIME_FLAG <NVARCHAR(20)>*/,"\ # PRIME
        #     "/*HHT_SUBMIT_DT <TIMESTAMP>*/,"\ # TXN_DT
        #     "/*HHT_CREATED_BY <NVARCHAR(100)>*/,"\ #salesperson_id
        #     "/*TXN_CREATED_DT <TIMESTAMP>*/,"\ #HHT_SUBMIT_DT
        #     "/*IS_DELETED <BOOLEAN>*/,"\ # false
        #     "/*CREATED_DATE <TIMESTAMP>*/,"\ #HHT_SUBMIT_DT
        #     "/*CREATED_BY <NVARCHAR(100)>*/,"\ #random_sp['ID']
        #     "/*MODIFIED_DATE <TIMESTAMP>*/,"\ #HHT_SUBMIT_DT
        #     "/*MODIFIED_BY <NVARCHAR(100)>*/,"\ #salesperson_id
        #     "/*VERSION <INTEGER>*/"\ #1
        # ")".format(dist_id)

        print("QUERY:", query)
        # print("modified", json.dumps(query))
        HanaDB().connect_database_to_environment()

        # HanaDB().insert_listdata_into_table(conn, "TXN_VANTRFOUTHDR", data)

        HanaDB().disconnect_from_database()
