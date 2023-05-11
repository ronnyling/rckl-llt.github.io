from resources.restAPI.Config.AppSetup import AppSetupGet
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import math
from resources.restAPI.MasterDataMgmt.Promo import PromoBuyTypeGet


class PromoDealCalculation(object):
    FE_FACTOR = "${fe_factor}"
    DISC_PERCENT = "Discount by %"
    DISC_VALUE = "Discount by Value"
    FOC = "Free Product"

    def calculate_forever_factor(self, forevery, gross, prorata):
        # Function which use to calculate forevery factor
        if prorata:
            fe_factor = float(gross) / float(forevery)
        else:
            foc_flag = BuiltIn().get_variable_value("${foc_flag}")
            if isinstance(gross, str) is True:
                gross = int(gross.split('.')[0])
            forevery = int(forevery.split('.')[0])
            if foc_flag:
                fe_factor = math.floor(gross / forevery)
            else:
                fe_factor = math.floor(gross / forevery) * forevery
        BuiltIn().set_test_variable(self.FE_FACTOR, fe_factor)


    def calculate_promo_disc_percentage(self):
        disc = 0
        prd_info = BuiltIn().get_variable_value("${prd_info}")
        gross = 0
        total_qty = 0
        for item in prd_info:
            total_qty += item['BUY_QTY']
            gross = gross + float(item['GROSS_AMT'])

        promo_payload = BuiltIn().get_variable_value("${promo_response}")
        apply_on = PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_apply_on_by_id(promo_payload["PROMO_SLABS"][0]['APPLY_ON'], 'id')
        promo_buy_type = \
            PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_buy_type(promo_payload['BUY_TYPE'], 'id')['REF_DESC']
        promo_type = PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_type(promo_payload['TYPE'], 'id')[
            'REF_DESC']
        prorata_flag = promo_payload['SCHEME_PRORATA']
        mech_type = promo_payload['PROMO_SLABS'][0]['MECHANIC_TYPE']
        mech_type = PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_mechanic_type(mech_type, 'id')['REF_DESC']
        if promo_type == 'Promo & Deal':
            if promo_buy_type == 'By Amount':
                # Promo discount buy type = amount
                disc = self.promo_disc_by_amt(mech_type, promo_payload, prd_info, prorata_flag, gross, apply_on)

            elif promo_buy_type == 'By Quantity':
                # Promo discount buy type = quantity
                disc = self.promo_disc_by_qty(mech_type, promo_payload, prd_info, prorata_flag, total_qty, apply_on)
        foc_flag = BuiltIn().get_variable_value("${foc_flag}")
        if foc_flag is False:
            promo_disc = disc[0]['PROMO_DISC']
        else:
            promo_disc = disc
        return promo_disc

    def check_forevery_and_calculate_for_every_factor(self, slab, gross, prorata_flag):
        if float(slab['FOR_EVERY']) > 0:
            self.calculate_forever_factor(slab['FOR_EVERY'], gross, prorata_flag)

    def promo_disc_by_amt(self, mech_type, promo_payload, prd_info, prorata_flag, gross, apply_on):
        if mech_type == self.DISC_PERCENT:
            ttb, disc_perc, slab = self.hitting_which_slab(promo_payload['PROMO_SLABS'], gross, 'TOTAL_BUY',
                                                           "percent")
            self.check_forevery_and_calculate_for_every_factor(slab, gross, prorata_flag)
            disc = self.discount_by_percentage(prd_info, prorata_flag, disc_perc, ttb, "amt")
        elif mech_type == self.DISC_VALUE:
            if apply_on['REF_DESC'] == "Per UOM":
                ttb, disc_amount, slab = self.hitting_which_slab(promo_payload['PROMO_SLABS'], gross,
                                                                 'TOTAL_BUY',
                                                                 "value")
                self.check_forevery_and_calculate_for_every_factor(slab, gross, prorata_flag)
                prd_info = self.cal_gross_and_qty_ratio(prd_info, ttb)
                disc = self.cal_discount_per_uom(ttb, prd_info, disc_amount, prorata_flag, "amt")
                BuiltIn().set_test_variable(self.FE_FACTOR, None)
            elif apply_on['REF_DESC'] == "Per Tier":
                ttb, disc_amount, slab = self.hitting_which_slab(promo_payload['PROMO_SLABS'], gross,
                                                                 'TOTAL_BUY',
                                                                 "value")
                prd_info = self.cal_gross_and_qty_ratio(prd_info, ttb)
                disc = self.calculate_discount_per_tier(prd_info, disc_amount, ttb, prorata_flag, "amt")
            elif apply_on['REF_DESC'] == "Per Product":
                ttb, disc_amount, slab = self.hitting_which_slab(promo_payload['PROMO_SLABS'], gross,
                                                                 'TOTAL_BUY',
                                                                 "value")
                prd_info = self.cal_gross_and_qty_ratio(prd_info, ttb)
                disc = self.calculate_discount_per_prod(prd_info, disc_amount, ttb)
        elif mech_type == self.FOC:
            ttb, disc_perc, slab = self.hitting_which_slab(promo_payload['PROMO_SLABS'], gross, "TOTAL_BUY", "")
            disc = self.calculate_foc_promotion(slab)
        return disc

    def calculate_foc_promotion(self, slab):
        FOC_LIST = []
        for item in slab['FOC']:
            if slab['FOR_EVERY'] != "0.000000":
                # if promo discount if Foc and Forevery = Yes
                fe = int(slab['FOR_EVERY'].split('.')[0])
                ttb = int(slab['TOTAL_BUY'].split('.')[0])
                foc_qty = ttb / fe * item['FOC_QTY']
            else:
                # if promo discount only foc without others condition, calculation will be straight forward
                # just directly follow foc in entitled slab
                foc_qty = item['FOC_QTY']
            payload = {
                "FOC_PRD_ID": item['PRDCAT_VALUE_ID'],
                "FOC_UOM_ID": item['FOC_UOM_ID'],
                "FOC_QTY": foc_qty,
            }
            FOC_LIST.append(payload)
        return FOC_LIST

    def promo_disc_by_qty(self, mech_type, promo_payload, prd_info, prorata_flag, total_qty, apply_on):

        if mech_type == self.DISC_PERCENT:
            # Promo discount by percentage
            ttb, disc_perc, slab = self.hitting_which_slab(promo_payload['PROMO_SLABS'], prd_info[0]['BUY_QTY'],
                                                           'TOTAL_BUY', "percent")
            self.check_forevery_and_calculate_for_every_factor(slab, total_qty, prorata_flag)
            prd_info = self.cal_gross_and_qty_ratio(prd_info, ttb)
            disc = self.discount_by_percentage(prd_info, prorata_flag, disc_perc, ttb, "qty")
        elif mech_type == self.DISC_VALUE:
            # Promo discount by value
            if apply_on['REF_DESC'] == "Per UOM":
                # Promo discount by value and apply on Per uom
                ttb, disc_amount, slab = self.hitting_which_slab(promo_payload['PROMO_SLABS'],
                                                                 prd_info[0]['BUY_QTY'],
                                                                 'TOTAL_BUY', "value")
                self.check_forevery_and_calculate_for_every_factor(slab, total_qty, prorata_flag)
                prd_info = self.cal_gross_and_qty_ratio(prd_info, ttb)
                disc = self.cal_discount_per_uom(ttb, prd_info, disc_amount, prorata_flag, "qty")
                BuiltIn().set_test_variable(self.FE_FACTOR, None)
            elif apply_on['REF_DESC'] == "Per Tier":
                # Promo discount by value and apply on Per Tier
                ttb, disc_amount, slab = self.hitting_which_slab(promo_payload['PROMO_SLABS'], prd_info[0]['BUY_QTY'],
                                                                 'TOTAL_BUY',
                                                                 "value")
                prd_info = self.cal_gross_and_qty_ratio(prd_info, ttb)
                disc = self.calculate_discount_per_tier(prd_info, disc_amount, ttb, prorata_flag, "qty")
        elif mech_type == self.FOC:
            # Promo discount by FOC
            ttb, disc_perc, slab = self.hitting_which_slab(promo_payload['PROMO_SLABS'], prd_info[0]['BUY_QTY'], "TOTAL_BUY", "")
            disc = self.calculate_foc_promotion(slab)
        return disc

    def calculate_discount_factor(self, total_gross, ttb, discount_per_tier):
        discount_factor = float(total_gross) / float(ttb) * float(discount_per_tier)
        return discount_factor

    def calculate_discount_per_tier(self, prd_info, disc_amt, ttb, prorata_flag, amt_or_qty):
        total = 0
        for item in prd_info:
            # Promo discount by value and apply on Per Tier(Discount factor will be different if buy type = amt or qty)
            if amt_or_qty == 'amt':
                discount_factor = self.calculate_discount_factor(float(item['GROSS_AMT']), ttb, disc_amt)
            else:
                discount_factor = self.calculate_discount_factor(float(item['BUY_QTY']), ttb, disc_amt)
            for uom in item['PRD_UOM']:
                if prorata_flag:
                    # Promo discount by value and apply on Per Tier(IF prorata yes)
                    uom['UOM_DISC_AMT'] = discount_factor * uom['QTY_RATIO']
                else:
                    # Promo discount by value and apply on Per Tier(IF prorata No)
                    uom['UOM_DISC_AMT'] = uom['GROSS_RATIO'] * float(disc_amt)
                total += uom['UOM_DISC_AMT']
            item['PROMO_DISC'] = total

        return prd_info

    def calculate_discount_per_prod(self, prd_info, disc_amt, ttb):
        total = 0
        print ("TTB: " ,ttb)
        print("DISC AMT: ", disc_amt)
        for item in prd_info:
            item['PROMO_DISC'] = disc_amt
        return prd_info

    def compare_python_calculation_with_api_return_promo_calculation(self):
        python_promo_calculation = BuiltIn().get_variable_value("${python_promo_calculation}")
        apply_promo_response = BuiltIn().get_variable_value("${apply_promo_response}")
        count = 0
        for item in apply_promo_response['TXN_PRODUCT']:
            BuiltIn().log_to_console("Calculated Discount Amount", python_promo_calculation[count]['PROMO_DISC'])
            BuiltIn().log_to_console("Returned Apply Promotion Discount Amount", item['PROMO_DISC'])
            assert item['PROMO_DISC'] == python_promo_calculation[count]['PROMO_DISC'], "Promo disc not match"

    def cal_discount_per_uom(self, ttb, transaction_prd_info, discount_per_uom, prorata_flag, amt_or_qty):
        fe_factor = BuiltIn().get_variable_value(self.FE_FACTOR)
        AppSetupGet.AppSetupGet().user_retrieves_details_of_application_setup()
        body_result = BuiltIn().get_variable_value('${body_result}')
        store_rounding = int(body_result['ROUND_OFF_DECIMAL']['ROUND_OFF_DECIMAL'])
        total = 0
        for item in transaction_prd_info:
            for uom in item['PRD_UOM']:
                if prorata_flag:
                    # Promo discount by value and apply on Per uom(IF prorata yes)
                    uom['UOM_DISC_AMT'] = round(float(uom['QTY']) * float(discount_per_uom), store_rounding)
                else:
                    # Promo discount by value and apply on Per uom(IF prorata No)
                    self.discount_uom_without_prorata(fe_factor, amt_or_qty, discount_per_uom, uom, ttb)
                total += uom['UOM_DISC_AMT']
            item['PROMO_DISC'] = total
        return transaction_prd_info

    def discount_uom_without_prorata(self, fe_factor, amt_or_qty, discount_per_uom, uom, ttb):
        if fe_factor is not None and amt_or_qty == 'amt':
            # Promo discount by value and apply on Per uom(If Forevery = Yes and buy type = amount)
            ratio = uom['GROSS_RATIO'] * fe_factor
            uom['UOM_DISC_AMT'] = ratio / uom['PRD_LISTPRC_UOM'] * float(discount_per_uom)
        elif fe_factor is not None and amt_or_qty == 'qty':
            # Promo discount by value and apply on Per uom(If Forevery = Yes and buy type = quantity)
            ratio = uom['QTY_RATIO'] * fe_factor
            uom['UOM_DISC_AMT'] = ratio * float(discount_per_uom)
        elif amt_or_qty == 'qty':
            # Promo discount by value and apply on Per uom(If Forevery = No and buy type = quantity)
            ratio = uom['QTY_RATIO']
            uom['UOM_DISC_AMT'] = ratio * float(ttb) * float(discount_per_uom)
        else:
            # Promo discount by value and apply on Per uom(If Forevery = No and buy type = amount)
            ratio = uom['GROSS_RATIO_AMT']
            uom['UOM_DISC_AMT'] = ratio / uom['PRD_LISTPRC_UOM'] * float(discount_per_uom)

    def cal_gross_and_qty_ratio(self, transaction_prd_info, ttb):
        """
        in order to calculate gross ratio and qty ratio
        total gross amount and total qty of the products have to be calculate first
        in first for loop

        :param transaction_prd_info:
        :return:
        """
        total_gross = 0
        total_qty = 0
        for item in transaction_prd_info:
            total_gross += float(item['GROSS_AMT'])
            total_qty += float(item['BUY_QTY'])
        for item in transaction_prd_info:
            for uom in item['PRD_UOM']:
                uom['GROSS_RATIO'] = float(uom['GROSS_PER_UOM']) / total_gross
                uom['GROSS_RATIO_AMT'] = float(uom['GROSS_PER_UOM']) / total_gross * float(ttb)
                uom['QTY_RATIO'] = float(uom['QTY']) / total_qty
        return transaction_prd_info

    def discount_by_percentage(self, transaction_prd_info, prorata_flag, percentage, ttb, amt_or_qty):
        fe_factor = BuiltIn().get_variable_value(self.FE_FACTOR)
        for item in transaction_prd_info:
            if fe_factor is not None:
                # Discount by percentage and with Forevery =Yes
                for uom in item['PRD_UOM']:
                    gross_amt_ratio = uom['GROSS_PER_UOM'] / item['GROSS_AMT'] * fe_factor
                    uom['disc_per_uom'] = gross_amt_ratio * float(percentage) / 100
            if amt_or_qty == "amt" and prorata_flag:
                # Discount by percentage with buy type = amount and prorata = yes
                gross = float(item['GROSS_AMT'])
            elif amt_or_qty == "amt" and not prorata_flag:
                # Discount by percentage with buy type = amount and prorata = No
                gross = float(ttb)
            elif amt_or_qty == "qty" and (prorata_flag or fe_factor is not None):
                # Discount by percentage with buy type = qty (prorata and forvery yes calcualtion is same)
                gross = float(item['PRD_UOM'][0]['QTY']) * float(item['UNIT_PRICE'])
            else:
                # Discount by percentage with buy type = qty (prorata and forvery are No)
                gross = float(ttb) * float(item['UNIT_PRICE'])
            promo_disc = float(gross) * float(percentage) / 100
            item['PROMO_DISC'] = promo_disc
        return transaction_prd_info

    def hitting_which_slab(self, promo_slab, gross_or_qty, dist_type, return_value):
        # This function will determine which slab will current sales invoice amount will allow to entitle and return information
        if promo_slab[0][dist_type] > promo_slab[1][dist_type]:
            promo_slab.reverse()
        slab = ""
        for item in promo_slab:
            if float(item[dist_type]) <= float(gross_or_qty) :
                BuiltIn().set_test_variable("${slab}", item)
                ttb = item[dist_type]
                slab = item
        if return_value == "percent":
            disc_value = slab['DISC_PERC']
        else:
            disc_value = slab['DISC_AMT']
        return ttb, disc_value, slab
