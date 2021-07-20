<link rel="stylesheet" href="https://casual-effects.com/markdeep/latest/journal.css?">
# Module `akasia` 

This is main module web browser Akasia. 
- Function [get_request](#Function-akasia.get_request)
- Function [print_site](#Function-akasia.print_site)
- Function [save_site_in_html](#Function-akasia.save_site_in_html)
- Function [save_site_in_markdown](#Function-akasia.save_site_in_markdown)
- Function [wikipedia_request](#Function-akasia.wikipedia_request)
- Function [printer](#Function-akasia.printer)
- Function [main](#Function-akasia.main)
#### Function `akasia.get_request` 

**Arguments**

- `url` -> `builtins.str`: 


**Return Type:** `builtins.str`




This function receives a request from the site.

Args:
    url (str): A variable that stores the URL that will open in the browser Akasia.

Returns:
    site_content (str): The variable contains the content of the site in html format.
    response (str): This variable stores the request from the site.






<details><summary>Source</summary>

```python
@dock()
def get_request(url: str) -> str:
    """

    This function receives a request from the site.

    Args:
        url (str): A variable that stores the URL that will open in the browser Akasia.

    Returns:
        site_content (str): The variable contains the content of the site in html format.
        response (str): This variable stores the request from the site.

    """

    try:
        response = requests.get(url)
    except requests.exceptions.MissingSchema:
        choosing_the_right_url = input(
            f"Invalid URL '{url}': No schema supplied. Perhaps you meant http://{url}? (y/n) "
        )
        if (
            choosing_the_right_url.lower() == "y"
            or choosing_the_right_url.lower() == "yes"
        ):
            response = requests.get(f"http://{url}")
        else:
            sys.exit()
    except requests.exceptions.ConnectionError:
        print(f'Site server "{url}" not found.')
        sys.exit()

    site_content = str(response.content, response.encoding)
    return site_content, response

```

</details>

#### Function `akasia.print_site` 

**Arguments**

- `site_content` -> `builtins.str`: 
- `response` -> `builtins.str`: 


**Return Type:** `builtins.str`




This function prints the site in format markdown.

Args:
    site_content (str): The variable contains the content of the site in html format.
    response (str): This variable stores the request from the site.
Returns:
    site (str): The variable stores the text of the site in markdown format.





<details><summary>Source</summary>

```python
@dock()
def print_site(site_content: str, response: str) -> str:
    """

    This function prints the site in format markdown.

    Args:
        site_content (str): The variable contains the content of the site in html format.
        response (str): This variable stores the request from the site.
    Returns:
        site (str): The variable stores the text of the site in markdown format.
    """
    if len(site_content) == 0:

        if response.status_code == requests.codes.ok:
            site = html2text.html2text(site_content)
        if response.status_code == 404:
            site = "Error 404, Not Found!"
        if response.status_code == 500:
            site = "Error 500, Internal server error!"

        site = html2text.html2text(site_content)

    # If non-empty content is detected, print it.
    # This is to allow customised html error messages.

    site = html2text.html2text(site_content)
    return site

```

</details>

#### Function `akasia.save_site_in_html` 

**Arguments**

- `site_content` -> `builtins.str`: 
- `path` -> `builtins.str`: 


**Return Type:** `?`




This function is needed to save the site in html format.

Args:
    site_content (str): This variable stores the site in html format.
    path (str): This variable stores path which will saved site in format html.

Returns:
    None: The function returns nothing.






<details><summary>Source</summary>

```python
@dock()
def save_site_in_html(site_content: str, path: str) -> None:
    """

    This function is needed to save the site in html format.

    Args:
        site_content (str): This variable stores the site in html format.
        path (str): This variable stores path which will saved site in format html.

    Returns:
        None: The function returns nothing.

    """
    with open(path, "w") as file:
        file.write(site_content)

```

</details>

#### Function `akasia.save_site_in_markdown` 

**Arguments**

- `site_content` -> `builtins.str`: 
- `path` -> `builtins.str`: 


**Return Type:** `?`




This function is needed to save the site in markdown format.

Args:
    site_content (str): This variable stores the site in html format.
    path (str): This variable stores path which will saved site in format markdown.

Returns:
    None: The function returns nothing.






<details><summary>Source</summary>

```python
@dock()
def save_site_in_markdown(site_content: str, path: str) -> None:
    """

    This function is needed to save the site in markdown format.

    Args:
        site_content (str): This variable stores the site in html format.
        path (str): This variable stores path which will saved site in format markdown.

    Returns:
        None: The function returns nothing.

    """
    with open(path, "w") as file:
        file.write(html2text.html2text(site_content))

```

</details>

#### Function `akasia.wikipedia_request` 

**Arguments**



**Return Type:** `?`


Function gets and finds wikipedia pages




<details><summary>Source</summary>

```python
@dock()
def wikipedia_request() -> None:
    """Function gets and finds wikipedia pages"""
    try:
        request = input("Request: ")
        language = input("Language on search in Wikipedia: ")
        wikipedia.set_lang(language)
        wiki_page = wikipedia.page(request)
        type_text = input("Full text(y/n) ")
        if type_text.lower() == "y":
            printer(wiki_page.content)
        elif type_text.lower() == "n":
            printer(wikipedia.summary(request))
        print("\nPage URL: " + wiki_page.url)
    except wikipedia.exceptions.PageError:
        print("Request page not found")
    except requests.exceptions.ConnectionError:
        print("Please type language by first two letters in language name.")

```

</details>

#### Function `akasia.printer` 

**Arguments**



**Return Type:** `builtins.int`


This is a print function that enters text on an live screen. 




<details><summary>Source</summary>

```python
@dock()
def printer(text) -> int:
    """This is a print function that enters text on an live screen. """
    array_text = text.splitlines()
    for i in enumerate(array_text):
        array_text[i[0]] = Markdown(array_text[i[0]])
    with Live(refresh_per_second=4, console=console):
        for i in enumerate(array_text):
            if getkey() == "q":
                break
            if getkey() == "n":
                console.print(i[1])

```

</details>

#### Function `akasia.main` 

**Arguments**



**Return Type:** `?`


This is main function, what initializing web browser Akasia.




<details><summary>Source</summary>

```python
@dock()
def main() -> None:
    """This is main function, what initializing web browser Akasia."""

    print(
        """
          d8888 888                        d8b
         d88888 888                        Y8P
        d88P888 888
       d88P 888 888  888  8888b.  .d8888b  888  8888b.
      d88P  888 888 .88P     "88b 88K      888     "88b
     d88P   888 888888K  .d888888 "Y8888b. 888 .d888888
    d8888888888 888 "88b 888  888      X88 888 888  888
   d88P     888 888  888 "Y888888  88888P' 888 "Y888888\n\n\n"""
    )
    print(f"Version - {VERSION}\n".center(58))
    print("Akasia - A fork tiny python text-based web browser Asiakas.\n".center(58))
    print('Type "quit" or "q" to shut down the browser.'.center(58))
    print('Type "google" or "g" to search information in Google.'.center(58))
    print('Type "wikipedia" or "w" to search information in Wikipedia.'.center(58))
    print('Type "save_html" or "sh" to save site in format html.'.center(58))
    print('Type "save_markdown" or "smd" to save site in format markdown.'.center(58))

    while True:
        link = input("URL: ")
        if link.lower() == "quit" or link.lower() == "q":

            break
        if link.lower() == "google" or link.lower() == "g":
            request = input("Request: ")
            link = "https://google.com/search?q=" + request.replace(" ", "+")
            cont, req_get = get_request(link)
            printer(print_site(cont, req_get))
        elif link.lower() == "wikipedia" or link.lower() == "w":
            wikipedia_request()
        elif link.lower() == "save_html" or link.lower() == "sh":
            link = input("URL: ")
            path = input("Path: ")
            cont, req_get = get_request(link)
            save_site_in_html(cont, path)
        elif link.lower() == "save_markdown" or link.lower() == "smd":
            link = input("URL: ")
            path = input("Path: ")
            cont, req_get = get_request(link)
            save_site_in_markdown(cont, path)
        else:
            cont, req_get = get_request(link)
            printer(print_site(cont, req_get))

```

</details>
