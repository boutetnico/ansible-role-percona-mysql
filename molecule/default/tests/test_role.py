import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("percona-server-client"),
        ("percona-server-common"),
        ("percona-server-server"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "path,username,groupname,mode",
    [
        ("/etc/mysql/my.cnf", "root", "root", 0o644),
    ],
)
def test_config_files_are_installed(host, path, username, groupname, mode):
    path = host.file(path)
    assert path.exists
    assert path.is_file
    assert path.user == username
    assert path.group == groupname
    assert path.mode == mode


@pytest.mark.parametrize(
    "name",
    [
        ("mysql"),
    ],
)
def test_service_is_running_and_enabled(host, name):
    service = host.service(name)
    assert service.is_enabled
    assert service.is_running


def test_convert_tz_query(host):
    query = "SELECT CONVERT_TZ('2004-01-01 12:00:00','GMT','MET');"
    result = host.run(f'mysql -e "{query}"')
    assert result.stdout.strip() != "NULL", "CONVERT_TZ query returned NULL"


def test_time_zone_name_rows(host):
    query = "SELECT * FROM mysql.time_zone_name;"
    result = host.run(f'mysql -e "{query}"')
    rows = result.stdout.strip().split("\n")
    assert len(rows) > 1, "time_zone_name table has no rows"


@pytest.mark.parametrize(
    "job,user",
    [
        (
            "@weekly /usr/bin/mysql_tzinfo_to_sql /usr/share/zoneinfo 2> /dev/null | /usr/bin/mysql mysql",
            "root",
        ),
    ],
)
def test_time_zone_update_cron_jobs_exist(host, job, user):
    jobs = host.check_output(f"crontab -u {user} -l")
    assert job in jobs


def test_encrypted_table_creation(host):
    create_table_query = "CREATE TABLE mysql.test_encryption (c1 INT) ENCRYPTION = 'Y';"
    create_result = host.run(f'mysql -e "{create_table_query}"')
    assert create_result.rc == 0, "Failed to create encrypted table test_encryption"

    check_encryption_query = """
    SELECT SPACE, NAME, SPACE_TYPE, ENCRYPTION
    FROM INFORMATION_SCHEMA.INNODB_TABLESPACES
    WHERE NAME = 'mysql/test_encryption' AND ENCRYPTION = 'Y';
    """
    check_result = host.run(f'mysql -e "{check_encryption_query}"')
    rows = check_result.stdout.strip().split("\n")
    assert (
        len(rows) > 1
    ), "Encrypted table test_encryption does not exist or is not encrypted"


@pytest.mark.parametrize(
    "username,expected_plugin",
    [
        ("test_sha2", "caching_sha2_password"),
        ("test_native", "mysql_native_password"),
    ],
)
def test_mysql_users_created_with_correct_auth_plugin(host, username, expected_plugin):
    query = f"SELECT plugin FROM mysql.user WHERE user = '{username}';"
    result = host.run(f'mysql -e "{query}"')
    plugin = result.stdout.strip().split("\n")[-1]
    assert (
        plugin == expected_plugin
    ), f"User {username}@{host} has incorrect plugin {plugin}, expected {expected_plugin}"
