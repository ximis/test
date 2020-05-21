from jsonpath import jsonpath

data = {"a":10, "b":20, "c":30}

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

print(jsonpath(data, "$.store.book[0:3:2].title"))
print(jsonpath(data, "$.store.book[0:2:2].title"))
print(jsonpath(data, "$.store.book[?(@.price < 10)].title"))
print(jsonpath(data, "$.store.book[(@.length -1)].title"))
print(jsonpath(data, "$..book[(@.length -1)].title"))
