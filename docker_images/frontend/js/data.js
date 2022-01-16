// globalne spremenjivke za inpute
let pointer_return_num = document.getElementById("return_num")
let pointer_return_name = document.getElementById("return_name")
let pointer_return_desc = document.getElementById("return_desc")
let pointer_name = document.getElementById("name")
let pointer_description = document.getElementById("description")
let pointer_number_id = document.getElementById("number_id")
let pointer_search_num = document.getElementById("search_num")
let pointer_search_name = document.getElementById("search_name")
let pointer_search_desc = document.getElementById("search_desc")
let pointer_posting_points = document.getElementById("posting_points")
let pointer_getting_points = document.getElementById("getting_points")

window.onload = function (){
    pointer_posting_points.addEventListener("submit", writing_point);
    pointer_getting_points.addEventListener("submit", getting_point);
}

function writing_point(){
    event.preventDefault();
    // console.log(event);

    let url = "http://localhost:5000/write_points";
    //console.log(url);
    let js_res = null;

    fetch(url, {method: 'POST', 
        headers: {
            'Access-Control-Allow-Origin' : '*',
            'Content-Type' : 'application/json;charset=utf-8' },
        body: JSON.stringify({
            bname : pointer_name.value,
            desc : pointer_description.value
    })})
    .then(response => response.text())
    //.then(commits => alert(commits[0].author.login))
    .then(data => {
        let d = JSON.parse(data);
        let num = "Number of posted point: ";
        let name = "Name of posted point: ";
        let desc = "Description of posted point: ";
        pointer_return_num.innerHTML = num + d.return_num; 
        pointer_return_name.innerHTML = name + d.return_name; 
        pointer_return_desc.innerHTML = desc + d.return_desc;

        // se pobrisemo oddane vrednosti
        pointer_name.value = ""; 
        pointer_description.value = ""; 

    }).catch(error => console.log(error));

    
    return false;

}

function getting_point(){
    event.preventDefault();
    // console.log(event);

    let url = "http://localhost:5000/get_points";
    // console.log(url);

    fetch(url, {method: 'POST', 
        headers: {
            'Access-Control-Allow-Origin' : '*',
            'Content-Type' : 'application/json;charset=utf-8' },
        body: JSON.stringify({
            num_id : document.getElementById("number_id").value
    })})
    .then(response => response.text())
    //.then(commits => alert(commits[0].author.login))
    .then(data => {
        let d = JSON.parse(data);
        let num = "Number of searched point: ";
        let name = "Name of searched point: ";
        let desc = "Description of searched point: ";
        pointer_search_num.innerHTML = num + d.return_num; 
        pointer_search_name.innerHTML = name + d.return_name; 
        pointer_search_desc.innerHTML = desc + d.return_desc;

        // se pobrisemo oddane vrednosti
        pointer_number_id.value = ""; 

    }).catch(error => console.log(error));

    
    return false;
}
