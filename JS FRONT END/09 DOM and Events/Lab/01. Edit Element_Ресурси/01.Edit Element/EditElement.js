function editElement(HtmlElement, match, replacer) {
    while (HtmlElement.textContent.includes(match)) {
        HtmlElement.textContent = HtmlElement.textContent.replace(match, replacer)
    }
}