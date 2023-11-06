
function addFilter(property) {
    const isEnabled = document.body.classList.contains(property);

    let filters = [
        'grayscale',
        'deuteranopia',
        'protanopia',
        'tritanopia',
        'blur'
    ]

    // Remove each class from the filters array
    for (let filter of filters) {
        document.body.classList.remove(filter);
    }

    if (!isEnabled) {
        document.body.classList.add(property);
    }
}