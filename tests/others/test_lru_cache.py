import pytest

from grind75.others.lru_cache import LRUCache


@pytest.fixture(scope="function")
def cache_cap3():
    return LRUCache(3)


def test_can_put_element_in_cache(cache_cap3):
    key_1, value_1 = "A", 1

    cache_cap3.put(key_1, value_1)

    assert len(cache_cap3) == 1
    assert key_1 in cache_cap3


def test_can_put_multiple_elements_in_cache(cache_cap3):
    key_1, value_1 = "A", 1
    key_2, value_2 = "B", 2
    key_3, value_3 = "C", 3

    cache_cap3.put(key_1, value_1)
    cache_cap3.put(key_2, value_2)
    cache_cap3.put(key_3, value_3)

    assert len(cache_cap3) == 3
    assert key_1 in cache_cap3
    assert key_2 in cache_cap3
    assert key_3 in cache_cap3


def test_cache_adheres_to_capacity_constraint(cache_cap3):
    key_1, value_1 = "A", 1
    key_2, value_2 = "B", 2
    key_3, value_3 = "C", 3
    key_4, value_4 = "D", 4

    cache_cap3.put(key_1, value_1)
    cache_cap3.put(key_2, value_2)
    cache_cap3.put(key_3, value_3)
    cache_cap3.put(key_4, value_4)

    assert len(cache_cap3) == 3
    assert key_2 in cache_cap3
    assert key_3 in cache_cap3
    assert key_4 in cache_cap3


def test_can_get_single_elements_value_in_cache(cache_cap3):
    key_1, value_1 = "A", 1
    cache_cap3.put(key_1, value_1)

    assert cache_cap3.get(key_1) == value_1


def test_can_get_elements_value_with_multiple_elements_in_cache(cache_cap3):
    key_1, value_1 = "A", 1
    key_2, value_2 = "B", 2
    key_3, value_3 = "C", 3

    cache_cap3.put(key_1, value_1)
    cache_cap3.put(key_2, value_2)
    cache_cap3.put(key_3, value_3)

    assert len(cache_cap3) == 3
    assert key_1 in cache_cap3
    assert key_2 in cache_cap3
    assert key_3 in cache_cap3


def test_returns_minus_one_if_element_not_in_cache(cache_cap3):
    assert cache_cap3.get("A") == -1


def test_cache_evicts_lru_element(cache_cap3):
    key_1, value_1 = "A", 1
    key_2, value_2 = "B", 2
    key_3, value_3 = "C", 3
    key_4, value_4 = "D", 4

    cache_cap3.put(key_1, value_1)
    cache_cap3.put(key_2, value_2)
    cache_cap3.put(key_3, value_3)
    cache_cap3.get(key_1)
    cache_cap3.put(key_4, value_4)

    assert len(cache_cap3) == 3
    assert key_3 in cache_cap3
    assert key_1 in cache_cap3
    assert key_4 in cache_cap3
