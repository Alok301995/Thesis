import os
debug = True
# secret_key = ''  # import os; os.urandom(24)
secret_key = 'dshfhwf'
public = False
epoched = False
epoch_days = 45
sentry_dsn = None  # change if you're using sentry exception handler

# database settings
# db_host = 'localhost'
# db_username = 'coveryourtracks'
# db_password = 'changeme'
# db_database = 'coveryourtracks'
# db_port = 3306

# My Db settings
db_host = 'localhost'
db_username = 'root'
db_password = 'Alok.1995'
db_database = 'coveryourtracks'
db_port = 3306


# # Heroku DB Setting
# db_host = 'us-cdbr-east-06.cleardb.net'
# db_username = 'bd3e365e151be0'
# db_password = 'e56ce314'
# db_database = 'heroku_d60c4f1c8f914da'
# db_port = 3306


# file for key material to use with hmac'ing ip addresses. 16 bytes
# keyfile = '/path/to/some/keyfile'
keyfile = 'key.txt'

# a password which authorizes various administrative tasks
admin_password = 'changeme'

# if your site wishes to use Matomo for analytics
use_matomo = False
matomo_url = 'anon-stats.eff.org'
matomo_site_id = '1111111'

# the domains for first-party trackers. order matters, only 3
first_party_trackers = [
    '127.0.0.1:5000',
    # 'coveryourtracks.eff.org',
    'firstpartysimulator.net',
    'firstpartysimulator.org'
]

third_party_trackers = {
    'ad_server': 'trackersimulator.org',
    'tracker_server': 'eviltracker.net',
    'dnt_server': 'do-not-tracker.org'
}
