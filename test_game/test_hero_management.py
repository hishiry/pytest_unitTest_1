import pytest

from game.hero_management import HeroManagement

hero_management = HeroManagement()


def setup():
    hero_management.create_hero("jinx", 20, 20)


@pytest.mark.parametrize("name", ["jinx"], ids=["创建用户"])
def test_create_hero(name):
    res = hero_management.find_hero(name)
    assert res != False
    assert res.get("name") == "jinx"
    assert res.get("volume") == 20
    assert res.get("power") == 20


@pytest.mark.parametrize("name", ["jinx"], ids=["查找用户"])
def test_find_hero(name):
    res_jinx = hero_management.find_hero(name)
    res_ez = hero_management.find_hero("ez")
    assert res_jinx.get("name") == "jinx"
    assert res_ez == False


@pytest.mark.parametrize("name, volume", [("jinx", 30)], ids=["更新用户"])
def test_update_hero(name, volume):
    hero_management.update_hero(name, volume)
    res_jinx = hero_management.find_hero("jinx")
    assert res_jinx.get("volume") == 30


@pytest.mark.parametrize("name", ["jinx"], ids=["删除用户"])
def test_delete_hero(name):
    hero_management.delete_hero(name)
    res_jinx = hero_management.find_hero("jinx")
    assert res_jinx == False
