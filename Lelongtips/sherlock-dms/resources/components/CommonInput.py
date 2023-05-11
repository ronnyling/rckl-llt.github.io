from resources.components import TextField, Calendar, Checkbox, DrpSingleSelection, DrpMultipleSelection, RadioButton, \
    Toggle

class CommonInput:

    def input_by_dict(self, **dict):
        for key, value in dict.items():
            label = key
            v = value.split('(')
            field_data = v[0]
            v = v[1].replace(')', '')
            field_att = v.split(',')
            field_name = field_att[0]
            field_cond = field_att[1]
            if field_name == 'textfield':
                field_length = field_att[2]
                if field_cond == 'withlength':
                    TextField.insert_into_field_with_length(label, field_data, field_length)
                else:
                    TextField.insert_into_field(label, field_data)
            elif field_name == 'calendar':
                Calendar.select_date_from_calendar(label, field_data)
            elif field_name == 'checkbox':
                true_or_false = field_att[2]
                Checkbox.select_checkbox(label, field_cond, field_data, true_or_false)
            elif field_name == 'singledropdown':
                DrpSingleSelection.selects_from_single_selection_dropdown(label, field_data)
            elif field_name == 'multidropdown':
                DrpMultipleSelection.select_from_multi_selection_dropdown(label, field_data)
            elif field_name == 'radiobutton':
                RadioButton.select_from_radio_button(label, field_data)
            elif field_name == 'toggle':
                Toggle.switch_toggle(label, field_data)
            else:
                print("Invalid Component")
