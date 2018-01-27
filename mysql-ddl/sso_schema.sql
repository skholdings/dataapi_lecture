CREATE TABLE user (
  user_id VARCHAR(100) PRIMARY KEY,
  user_name VARCHAR(256) CHARACTER SET UTF8 NOT NULL,
  password VARCHAR(256) NOT NULL,
  scope VARCHAR(256)
);

CREATE TABLE scope (
  id INT(100) PRIMARY KEY AUTO_INCREMENT,
  category VARCHAR(256) NOT NULL,
  role VARCHAR(256) NOT NULL,
  detail_role VARCHAR(256),
  description VARCHAR(4096) CHARACTER SET UTF8
);

-- used in tests that use HSQL
CREATE TABLE oauth_client_details (
  client_id VARCHAR(100) PRIMARY KEY,
  resource_ids VARCHAR(256),
  client_secret VARCHAR(256),
  scope VARCHAR(256),
  authorized_grant_types VARCHAR(256),
  web_server_redirect_uri VARCHAR(256),
  authorities VARCHAR(256),
  access_token_validity INTEGER,
  refresh_token_validity INTEGER,
  additional_information VARCHAR(4096),
  autoapprove VARCHAR(256)
);
