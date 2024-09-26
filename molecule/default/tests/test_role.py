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
