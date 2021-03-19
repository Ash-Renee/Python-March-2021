# need our 4 locations
# only 2 routes
# only 1 html
# HTML 
#     gold counter
#     4 locations with stuff
#         farm, cave, house, casino
            #EACH ONE WILL HAVE HIDDEN INPUT
            # <INPUT TYPLE=HIDDEN NAME="WHICH_FORM" VALUE="LOCATION NAME">
            # <INPUT TYPLE=HIDDEN NAME="WHICH_FORM" VALUE="LOCATION NAME">
            # <INPUT TYPLE=HIDDEN NAME="WHICH_FORM" VALUE="LOCATION NAME">
            # <INPUT TYPLE=HIDDEN NAME="WHICH_FORM" VALUE="LOCATION NAME">
#     activity log



# # URLS.PY

# # path ''
# INITALIZE GOLD TO 0 IN SESSION FOR FIRST TIMEM 
    # REQUEST.SESSION['GOLD] = 0
# INITALIZE ACTIVITES TO [] IF FIRST TIME 
#

# path'porocess_money", this lets us run the money earned into the base

# # def process(request):
# if request.post[form] == farm:
#     choose random amopunt from 10-20(farm) and add to gold in session 
#     create a log string and append to activity log in session 
        # x4 for all 4 locations (elif)
    # string = f" earned gold from (location)!"

# return redircet("/")


# ACT LOG 
# gold earned/lost 
# date/time/location (bonus only)
#list of actions that occured.  also need to show restarts/clears
# USE A FOR LOOP {% for something in reqwust.session.activites %}

# COUNTER 
# start at 0 and add/lose per process 

# WAY TO RESET GAME