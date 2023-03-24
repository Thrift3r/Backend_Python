# Import the necessary modules
from selenium import webdriver


def selenium(url):
    # Import the necessary modules
    from selenium import webdriver

    # Open the web page using the Chrome driver
    driver = webdriver.Chrome()

    # Open the web page
    driver.get(url)

    # Find all elements with the specified class name
    # Encuentra todos los elementos con la clase "web_ui__ItemBox__owner"
    elements = driver.find_elements_by_class_name("web_ui__ItemBox__owner")

    # Find all elements with the specified class name
    # Encuentra todos los elementos con la clase "web_ui__ItemBox__overlay"
    texto = driver.find_elements_by_class_name("web_ui__ItemBox__overlay")

    # Iterate through the elements
    for element in elements:
        # Find the link element within the element with the specified class name
        link = element.find_element_by_tag_name("a")

        # Extract the href attribute from the link element
        href = link.get_attribute("href")

        # Print the href
        print(href)

    # Iterate through the elements
    for text in texto:
        # Extract the title attribute from the element
        title = text.get_attribute("title")

        # Print the title
        print(title)

    # Close the web page
    driver.close()



