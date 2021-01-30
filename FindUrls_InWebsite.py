from requests_html import HTMLSession

session = HTMLSession()


Links = session.get(input("[!] ENTER WEBSITE (URL) : ").strip()).html.links
link = [ print (link) for link in Links ]
