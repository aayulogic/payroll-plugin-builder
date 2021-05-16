''' Criteria to sign
1. Must expose one init function with employee, 
   package_heading, from_date and to_date arguments respectively
1. Must return a tuple with vaule and sources list
2. Code should be harmful
'''

def init(employee, package_heading, from_date, to_date):
    print('START_____________OUTPUT FROM TEST PLUGIN_____________')

    print(employee, package_heading, from_date, to_date)

    print('END_____________OUTPUT FROM TEST PLUGIN_____________')

    return 100, [
        dict(
            model_name="XYZ",
            instance_id=2,
            url=""
        )
    ]