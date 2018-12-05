
argonne_office_status_dict = { "cnerg"  : ('anl', "at ANL, but available here!"),
                               "openmc" : ('desktop_computer', "at desk") }

uw_nat_status_dict = { "cnerg"  : ('sweat', "exercising"),
                       "openmc" : ('uw', "in Madison") }

uw_office_status_dict = { "cnerg"  : ('desktop_computer', "at desk"),
                          "openmc" : ('uw', "at Madison office") }

mbg_status_dict = { "cnerg"  : ('sweat', "exercising"),
                    "openmc" : ('uw', "in Madison") }

home_status_dict = { "cnerg"  : ('house', "at home"),
                     "openmc" : ('house', "at home") }

lakeside_coffee_status_dict = { "cnerg" : ('coffee', "lakeside coffee"),
                                "openmc" :('uw', "in Madison") }

locations = { "argonne_office"  : argonne_office_status_dict,
              "uw_nat"          : uw_nat_status_dict,
              "uw_office"       : uw_office_status_dict,
              "mbg"             : mbg_status_dict,
              "home"            : home_status_dict,
              "lakeside_coffee" : lakeside_coffee_status_dict }
              

aliases = {'exasmr' : 'openmc'}
