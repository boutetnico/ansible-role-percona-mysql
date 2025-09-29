[![tests](https://github.com/boutetnico/ansible-role-percona-mysql/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-percona-mysql/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.percona_mysql-blue.svg)](https://galaxy.ansible.com/boutetnico/percona_mysql)

ansible-role-percona-mysql
==========================

This role installs [Percona Server for MySQL](https://www.percona.com/mysql/software/percona-server-for-mysql).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                                  | Required | Default                  | Choices   | Comments                              |
|-------------------------------------------|----------|--------------------------|-----------|---------------------------------------|
| mysql_package_version                     | true     |                          | string    | See `defaults/main.yml`.              |
| mysql_packages                            | true     |                          | list      | See `defaults/main.yml`.              |
| mysql_extra_packages                      | true     |                          | list      | See `defaults/main.yml`.              |
| mysql_packages_state                      | true     | `present`                | string    |                                       |
| mysql_pip_packages                        | true     |                          | list      | See `defaults/main.yml`.              |
| mysql_user                                | true     | `mysql`                  | string    |                                       |
| mysql_group                               | true     | `mysql`                  | string    |                                       |
| mysql_installdir                          | true     | `/usr/sbin`              | string    |                                       |
| mysql_datadir                             | true     | `/var/lib/mysql`         | string    |                                       |
| mysql_tmpdir                              | true     | `/tmp`                   | string    |                                       |
| mysql_logdir                              | true     | `/var/log/mysql`         | string    |                                       |
| mysql_plugindir                           | true     | `/usr/lib/mysql/plugin`  | string    |                                       |
| mysql_keyringdir                          | true     | `/var/lib/mysql-keyring` | string    |                                       |
| mysql_sql_mode                            | true     | `''`                     | string    |                                       |
| mysql_charset                             | true     | `utf8mb4`                | string    |                                       |
| mysql_collation                           | true     | `utf8mb4_general_ci`     | string    |                                       |
| mysql_performance_schema                  | true     | `1`                      | int       |                                       |
| mysql_authentication_policy               | true     | `*,,`                    | string    |                                       |
| mysql_root_user                           | true     | `root`                   | string    |                                       |
| mysql_root_authentication_plugin          | true     | `caching_sha2_password`  | string    |                                       |
| mysql_root_password                       | true     | `root`                   | string    |                                       |
| mysql_root_salt                           | true     | `1234567890abcdefghij`   | string    |                                       |
| mysql_root_privileges                     | true     | `*.*:ALL,GRANT`          | string    |                                       |
| mysql_server_id                           | true     | `1`                      | int       |                                       |
| mysql_replication_role                    | true     | `''`                     | string    | `master`, `slave` or `''`             |
| mysql_replication_master_host             | true     | `''`                     | string    |                                       |
| mysql_replication_master_user             | true     | `repl`                   | string    |                                       |
| mysql_replication_master_password         | true     | `repl`                   | string    |                                       |
| mysql_replication_options                 | true     | `{}`                     | dict      |                                       |
| mysql_relay_log_recovery                  | true     | `0`                      | int       |                                       |
| mysql_read_only                           | true     | `OFF`                    | string    |                                       |
| mysql_super_read_only                     | true     | `OFF`                    | string    |                                       |
| mysql_binlog_do_db                        | true     | `[]`                     | list      |                                       |
| mysql_binlog_expire_logs_seconds          | true     | `2592000`                | int       | Default to 30 days.                   |
| mysql_enable_bin_logs                     | true     | `true`                   | boolean   |                                       |
| mysql_databases                           | true     | `[]`                     | list      | Databases to create.                  |
| mysql_remove_databases                    | true     | `[]`                     | list      | Databases to remove.                  |
| mysql_users                               | true     | `[]`                     | list      | Users to create.                      |
| mysql_users_default_authentication_plugin | true     | `caching_sha2_password`  | string    |                                       |
| mysql_remove_users                        | true     | `[]`                     | list      | Users to remove.                      |
| mysql_innodb_buffer_pool_size             | true     | `128M`                   | string    |                                       |
| mysql_innodb_flush_log_at_trx_commit      | true     | `1`                      | int       |                                       |
| mysql_innodb_flush_method                 | true     | `O_DIRECT`               | string    |                                       |
| mysql_innodb_io_capacity                  | true     | `10000`                  | int       |                                       |
| mysql_innodb_numa_interleave              | true     | `ON`                     | string    |                                       |
| mysql_innodb_print_all_deadlocks          | true     | `0`                      | int       |                                       |
| mysql_innodb_read_io_threads              | true     |                          | int       | See `defaults/main.yml`.              |
| mysql_innodb_write_io_threads             | true     | `4`                      | int       |                                       |
| mysql_max_allowed_packet                  | true     | `64M`                    | string    |                                       |
| mysql_max_connections                     | true     | `151`                    | int       |                                       |
| mysql_open_files_limit                    | true     | `5000`                   | int       |                                       |
| mysql_table_open_cache                    | true     | `4000`                   | int       |                                       |
| mysql_log_queries_not_using_indexes       | true     | `0`                      | int       |                                       |
| mysql_long_query_time                     | true     | `10`                     | int       |                                       |
| mysql_slow_query_log                      | true     | `OFF`                    | string    |                                       |
| mysql_slow_query_log_file                 | true     |                          | string    | See `defaults/main.yml`.              |
| mysql_log_output                          | true     | `FILE`                   | string    |                                       |
| mysql_log_error                           | true     |                          | string    | See `defaults/main.yml`.              |
| mysql_log_error_suppression_list          | true     | `[]`                     | list      |                                       |
| mysql_log_error_verbosity                 | true     | `2`                      | int       |                                       |
| mysql_log_slow_admin_statements           | true     | `OFF`                    | string    |                                       |
| mysql_log_slow_replica_statements         | true     | `OFF`                    | string    |                                       |
| mysql_log_slow_rate_type                  | true     | `session`                | string    |                                       |
| mysql_log_slow_rate_limit                 | true     | `1`                      | int       |                                       |
| mysql_slow_query_log_always_write_time    | true     | `10`                     | int       |                                       |
| mysql_log_slow_verbosity                  | true     | `''`                     | string    |                                       |
| mysql_slow_query_log_use_global_control   | true     | `''`                     | string    |                                       |
| mysql_tls_version                         | true     | `''`                     | string    |                                       |
| mysql_x_plugin                            | true     | `ON`                     | string    |                                       |
| mysql_systemd_override                    | true     | `{}`                     | dict      |                                       |
| mysql_load_tz_tables                      | true     | `false`                  | boolean   |                                       |
| mysql_disable_percona_telemetry           | true     | `true`                   | boolean   | Privacy by default.                   |

Dependencies
------------

- [percona-release role](https://github.com/boutetnico/ansible-role-percona-release/)

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-percona-mysql

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
