CREATE OR REPLACE DATABASE <Database Name>;

CREATE OR REPLACE NETWORK RULE <google_apis_network_rule_name>
    MODE = EGRESS
    TYPE = HOST_PORT
    VALUE_LIST = ('sheets.googleapis.com');

CREATE OR REPLACE SECURITY INTEGRATION google_sheets_oauth
    TYPE = API_AUTHENTICATION
    AUTH_TYPE = OAUTH2
    OAUTH_CLIENT_ID = 'Client ID'
    OAUTH_CLIENT_SECRET = 'Client Secret'
    OAUTH_TOKEN_ENDPOINT = 'https://oauth2.googleapis.com/token'
    OAUTH_AUTHORIZATION_ENDPOINT = 'https://accounts.google.com/o/oauth2/auth'
    OAUTH_ALLOWED_SCOPES = ('https://www.googleapis.com/auth/cloud-platform')
    ENABLED = TRUE;

CREATE OR REPLACE SECRET oauth_token
    TYPE = OAUTH2
    API_AUTHENTICATION = google_sheets_oauth
    OAUTH_REFRESH_TOKEN = 'Refresh Token from OAUTH Playground';

GRANT READ ON SECRET oauth_token TO ROLE <Developer Role>;

CREATE OR REPLACE EXTERNAL ACCESS INTEGRATION google_apis_access_integration
    ALLOWED_NETWORK_RULES = (< your google_apis_network_rule_name>)
    ALLOWED_AUTHENTICATION_SECRETS = (oauth_token)
    ENABLED = TRUE;

GRANT USAGE ON INTEGRATION google_apis_access_integration TO ROLE <Developer Role>;