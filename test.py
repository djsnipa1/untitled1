import json

with open('json.json') as f:
  jsonObject = json.load(f)

def main():

    # create a simple JSON array
    # jsonString = '{"key1":"value1","key2":"value2","key3":"value3"}'

    # change the JSON string into a JSON object
    # jsonObject = json.loads(jsonString)

    # print the keys and values
    for key in jsonObject:
        value = jsonObject[key]
        print("The key and value are ({}) = ({})".format(key, value))

    pass

print(jsonObject.items())


if __name__ == '__main__':
    main()