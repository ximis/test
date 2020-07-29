from mitmproxy import http

f = open("log.txt", "w+")


def request(flow: http.HTTPFlow):
    print("urls is :", flow.request.url)
    print("path is :", flow.request.path)
    print("method is :", flow.request.method.lower())
    print("check method :", flow.request.method.lower() == "get")
    print("url check :", "http" in flow.request.url)
    if "order" in flow.request.url and flow.request.method.lower() == "post":
        # print(flow.request.data)
        # f.writelines(flow.request.data)
        # f.writelines("\n")

        print("the path is: ", flow.request.path)
        print("the url is: ", flow.request.url)
        print("form data is: ", dict(flow.request.multipart_form))
        print("form data is source: ", flow.request.multipart_form)
        f.writelines("the path is: " + flow.request.path)
        f.writelines("\n")
        f.writelines("the url is: " + flow.request.url)
        f.writelines("\n")
        f.writelines("form data is: " + str(dict(flow.request.multipart_form)))
        f.writelines("\n")
        f.writelines("form data is source: " + str(flow.request.multipart_form))
        f.writelines("\n")
        f.flush()
