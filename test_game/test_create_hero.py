import pytest

from game.hero_management import HeroManagement


@pytest.mark.parametrize("name", ["jinx"], ids=["姓名_success"])
def test_create_hero_name_success(name):
    hero_management = HeroManagement()
    hero_management.create_hero(name, 20, 20)
    res = hero_management.find_hero(name)
    assert res.get("name") == "jinx"


@pytest.mark.parametrize("name", [",,"], ids=["姓名_fail"])
def test_create_hero_name_fail(name):
    hero_management = HeroManagement()
    hero_management.create_hero(name, 20, 20)
    res = hero_management.find_hero(name)
    assert res == False


@pytest.mark.parametrize("volume", [1, 2, 98, 99], ids=["血量_success_1", "血量_success_2", "血量_success_98", "血量_success_99"])
def test_create_hero_volume_success(volume):
    hero_management = HeroManagement()
    hero_management.create_hero("volume_success", volume, 20)
    res = hero_management.find_hero("volume_success")
    assert res.get("volume") == volume


@pytest.mark.parametrize("volume", [0, 100, -1], ids=["血量_fail_0", "血量_fail_100", "血量_fail_-1"])
def test_create_hero_volume_fail(volume):
    hero_management = HeroManagement()
    hero_management.create_hero("volume_fail", volume, 20)
    res = hero_management.find_hero("volume_fail")
    assert res == False


@pytest.mark.parametrize("power", [22], ids=["战斗力_success"])
def test_create_hero_power_success(power):
    hero_management = HeroManagement()
    hero_management.create_hero("power_success", 20, power)
    res = hero_management.find_hero("power_success")
    assert res.get("power") == power


@pytest.mark.parametrize("power", [0, -1, 0.001, "e"], ids=["战斗力_fail_0", "战斗力_fail_-1", "战斗力_fail_0.001", "战斗力_fail_e"])
def test_create_hero_power_fail(power):
    hero_management = HeroManagement()
    hero_management.create_hero("power_fail", 20, power)
    res = hero_management.find_hero("power_fail")
    assert res == False
