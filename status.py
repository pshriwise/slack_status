
argonne_office_status_dict = { "cnerg"  : ('anl', "at ANL, but available here!"),
                               "openmc" : ('desktop_computer', "at desk") }

uw_nat_status_dict = { "cnerg"  : ('sweat', "exercising"),
                       "openmc" : ('uw', "in Madison") }

uw_office_status_dict = { "cnerg"  : ('desktop_computer', "at desk"),
                          "openmc" : ('uw', "at Madison office") }

tac_status_dict = { "cnerg"  : ('sweat', "exercising"),
                    "openmc" : ('uw', "in Madison") }

mbg_status_dict = { "cnerg"  : ('sweat', "exercising"),
                    "openmc" : ('uw', "in Madison") }

home_status_dict = { "cnerg"  : ('house', "at home"),
                     "openmc" : ('house', "at home") }

lakeside_coffee_status_dict = { "cnerg" : ('coffee', "lakeside coffee"),
                                "openmc" :('uw', "in Madison") }

uchicago_status_dict = {"cnerg" : ('uchicago', "C++/Python"),
            "openmc" : ('uchicago', "C++/Python")}


locations = { "argonne_office"  : argonne_office_status_dict,
              "uw_nat"          : uw_nat_status_dict,
              "uw_office"       : uw_office_status_dict,
              "mbg"             : mbg_status_dict,
              "home"            : home_status_dict,
              "lakeside_coffee" : lakeside_coffee_status_dict,
              "uchicago"        : uchicago_status_dict,
              "tac"             : tac_status_dict }
              
aliases = {'exasmr' : 'openmc', 
           'uw-ne' : 'cnerg',  
           'mpcs-python-s19' : 'openmc' }
