udemy_url = 'https://udemy.com'
udemy_url_without_prefix = "url_without_prefix: " + udemy_url.removeprefix("https://")
print(udemy_url_without_prefix)

udemy_url_without_suffix = "url_without_suffix: " + udemy_url.removesuffix("udemy.com")
print(udemy_url_without_suffix)