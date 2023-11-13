# # Solution 1. Simple if/elif/else using endswith function.
# file = input("File name: ").strip().lower()

# if file.endswith(".gif"):
#     print("image/gif")
# elif file.endswith(".jpg"):
#     print("image/jpeg")
# elif file.endswith(".jpeg"):
#     print("image/jpeg")
# elif file.endswith(".png"):
#     print("image/png")
# elif file.endswith(".pdf"):
#     print("application/pdf")
# elif file.endswith(".txt"):
#     print("text/plain")
# elif file.endswith(".zip"):
#     print("application/zip")
# else:
#     print("application/octet-stream")

# Solution 2 using rpartition with if/elif/else. rsplit also works here.
file = input("File name: ").strip().lower()

mime = file.rpartition(".")[-1]
#mime = file.rsplit(".")[-1] #also works

match mime:
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png" | "gif":
        print(f"image/{mime}")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")