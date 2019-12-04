//  on document ready
$( document ).ready(function() {
    setSearchValue(); // set value of search bar
    setPagination()
    setActivePage(current_page)

});

// set value of search bar input
function setSearchValue(){
    var query_param = get_url().searchParams.get('q') // get query param from url string
    document.getElementById('search-bar').value = query_param // set value to <input>
}


function setPagination() {

    $('#pagination').twbsPagination({
        totalPages: total_pages,
        visiblePages: 10,
        initiateStartPageClick: false,
        onPageClick: function (event, page) {
            $('#page-content').text('Page ' + page);
            reload_new_page(page)
        }
    });

}

function get_url() {
    var url_string = window.location.href // get url string
    var url = new URL(url_string);
    return url
}

function reload_new_page(page) {
    var url = get_url()
    url.searchParams.set('page', page)
    window.location.replace(url)
}

function setActivePage(page) {
    $('#page-content').text('Page ' + page);
    $('li').click(function() {
        $(this).addClass('active').siblings().removeClass('active');
    });
}