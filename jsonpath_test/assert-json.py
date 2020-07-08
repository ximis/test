from jsonpath import jsonpath

data = { "store": {
    "book": [
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}


def assert_equals(data, expr, expected):
    actual = jsonpath(data, expr)
    if len(actual) == 1 and actual[0] != expected:
        raise AssertionError("expected " + str(expected) + " but get " + str(actual))
    return True


def assert_contains(data, expr, expected):
    actual = jsonpath(data, expr)
    if expected not in actual:
        raise AssertionError(str(actual) + " not contains " + str(expected))
    return True


def assert_not_equals(data, expr, expected):
    actual = jsonpath(data, expr)
    if len(actual) == 1 and actual[0] == expected:
        raise AssertionError("not expected " + str(expected) + " but get " + str(actual))
    return True


def assert_not_contains(data, expr, expected):
    actual = jsonpath(data, expr)
    if expected in actual:
        raise AssertionError(str(actual) + " contains " + str(expected))
    return True


def assert_equals(data, expr, expected):
    actual = jsonpath(data, expr)
    if len(actual) == 1 and actual[0] != expected:
        raise AssertionError("expected " + str(expected) + " but get " + str(actual))
    return True


assert_equals(data, "$..book[(@.length -1)].title", 'The Lord of the Rings')



