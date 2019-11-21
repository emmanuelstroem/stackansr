//  on document ready
$( document ).ready(function() {
    setSearchValue(); // set value of search bar
});

// set value of search bar input
function setSearchValue(){
    var url_string = window.location.href // get url string
    var url = new URL(url_string);
    var query_param = url.searchParams.get('q') // get query param from url string
    document.getElementById('search-bar').value = query_param // set value to <input>
}