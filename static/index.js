var searchbar = document.getElementById("searchbar")

function Find()
{
    window.location = "/problem/" + searchbar.value;
}
function GoTo(link) {
    window.location = link;
}