import pytest
import pymysql


def get_mysql_connection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="mysql",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


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


def test_convert_tz_query():
    connection = get_mysql_connection()
    try:
        with connection.cursor() as cursor:
            query = "SELECT CONVERT_TZ('2004-01-01 12:00:00','GMT','MET');"
            cursor.execute(query)
            result = cursor.fetchone()
            assert result is not None, "CONVERT_TZ query returned NULL"
    finally:
        connection.close()


def test_time_zone_name_rows():
    connection = get_mysql_connection()
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM mysql.time_zone_name;"
            cursor.execute(query)
            rows = cursor.fetchall()
            assert len(rows) > 0, "time_zone_name table has no rows"
    finally:
        connection.close()
