function showCreate(){
    document.getElementById('showCreateButton').style.display="none"
    document.getElementById('cityTable').style.display="none"
    document.getElementById('createUpdateForm').style.display="block"

    document.getElementById('createLabel').style.display="inline"
    document.getElementById('updateLabel').style.display="none"

    document.getElementById('doCreateButton').style.display="block"
    document.getElementById('doUpdateButton').style.display="none"
}

function showViewAll(){
    document.getElementById('showCreateButton').style.display="block"
    document.getElementById('cityTable').style.display="block"
    document.getElementById('createUpdateForm').style.display="none"
    getAllAjax();
}

function showUpdate(buttonElement){
    document.getElementById('showCreateButton').style.display="none"
    document.getElementById('cityTable').style.display="none"
    document.getElementById('createUpdateForm').style.display="block"

    document.getElementById('createLabel').style.display="none"
    document.getElementById('updateLabel').style.display="inline"

    document.getElementById('doCreateButton').style.display="none"
    document.getElementById('doUpdateButton').style.display="block"


    var rowElement = buttonElement.parentNode.parentNode
    // these is a way of finding the closest <tr> which would safer, closest()

    var city = getCityFromRow(rowElement)
    populateFormWithCity(city)
}

function doCreate(){
    var form = document.getElementById('createUpdateForm')

    var city = {}

    city.Name = form.querySelector('input[name="Name"]').value
    city.CountryCode = document.getElementById('countriesList').value
    city.District = form.querySelector('input[name="District"]').value
    city.Population = form.querySelector('input[name="Population"]').value
    createCityAjax(city)
    clearForm();
}

function doUpdate(){
    var city = getCityFromForm();
    var rowElement = document.getElementById(city.ID);
    updateCityAjax(city);

    clearForm();
}

function doDelete(r){
    var tableElement = document.getElementById('cityTable');
    var rowElement = r.parentNode.parentNode;
    var index = rowElement.rowIndex;
    deleteCityAjax(rowElement.getAttribute("ID"));
    tableElement.deleteRow(index);
}

function deleteCityAjax(id){
    $.ajax({
        "url": "/cities/"+encodeURI(id),
        "method":"DELETE",
        "data":"",
        "dataType": "JSON",
        contentType: "application/json; charset=utf-8",
        "success":function(result){

        },
        "error":function(xhr,status,error){
            console.log("error: "+status+" msg:"+error);
        }
    });
}

function doCancel() {
    document.getElementById('showCreateButton').style.display="block"
    document.getElementById('cityTable').style.display="block"
    document.getElementById('createUpdateForm').style.display="none"
}
function addCountryToList(country){
    var countriesList = document.getElementById('countriesList')
    var option = document.createElement("option");
    option.text = country.Name;
    option.value = country.Code;
    countriesList.add(option);
}

function clearForm(){
    var form = document.getElementById('createUpdateForm')

    form.querySelector('input[name="Name"]').value=''
    document.getElementById('countriesList').options[0].selected = true;
    form.querySelector('input[name="District"]').value=''
    form.querySelector('input[name="Population"]').value=''
}

function addCityToTable(city){
    var tableElement = document.getElementById('cityTable')
    var rowElement = tableElement.insertRow(-1)
    rowElement.setAttribute('ID',city.ID);
    var cell0 = rowElement.insertCell(0);
    cell0.innerHTML = '<a href="https://www.google.com/maps/search/?api=1&query=' + city.Name + '" target="_blank">' + city.Name + '</a>';
    var cell1 = rowElement.insertCell(1);
    cell1.innerHTML = city.CountryName
    var cell2 = rowElement.insertCell(2);
    cell2.innerHTML = city.District
    var cell3 = rowElement.insertCell(3);
    cell3.innerHTML = city.Population
    var cell4 = rowElement.insertCell(4);
    cell4.innerHTML = '<button onclick="showUpdate(this)">Update</button>'
    var cell5 = rowElement.insertCell(5);
    cell5.innerHTML = '<button onclick=doDelete(this)>Delete</button>'
    // hidden CountryCode
    var cell6 = rowElement.insertCell(6);
    cell6.innerHTML = city.CountryCode
    cell6.hidden = 'true';
}

function getAllAjax(){
    $.ajax({
        "url": "/cities",
        "method":"GET",
        "data":"",
        "dataType": "JSON",
        "success":function(result){
            var tableElement = document.getElementById('cityTable');
            tableElement.innerHTML='<tr><th align="left">Name<br> (click to see city on the map)</th>' +
                    '<th align="left">Country</th>' +
                    '<th align="left">District</th>' +
                    '<th align="left">Population</th>' +
                    '<th align="left"> </th><th> </th><tn> </tn></tr>';
            for (city of result){
                addCityToTable(city);
            }

        },
        "error":function(xhr,status,error){
            console.log("error: "+status+" msg:"+error);
        }
    });

}

function getCityFromRow(rowElement){
    var car ={}
    city.ID  = rowElement.getAttribute('ID')
    city.Name = rowElement.cells[0].firstChild.textContent
    city.CountryCode = rowElement.cells[6].firstChild.textContent
    city.District = rowElement.cells[2].firstChild.textContent
    city.Population = parseInt(rowElement.cells[3].firstChild.textContent,10)
    return city
}

function setCityInRow(rowElement, city){
    rowElement.cells[0].firstChild.textContent= city.Name 
    rowElement.cells[1].firstChild.textContent= city.CountryName
    rowElement.cells[2].firstChild.textContent= city.District
    rowElement.cells[3].firstChild.textContent= city.Population 
}

function populateFormWithCity(city){
    var form = document.getElementById('createUpdateForm')
    form.querySelector('input[name="ID"]').disabled = true

    form.querySelector('input[name="ID"]').value  = city.ID
    form.querySelector('input[name="Name"]').value= city.Name
    countriesList = document.getElementById('countriesList')
    for(var i = 0;i < countriesList.options.length;i++){
        if(countriesList.options[i].value == city.CountryCode ) { countriesList.options[i].selected = true; }
    }
    form.querySelector('input[name="District"]').value= city.District
    form.querySelector('input[name="Population"]').value= city.Population
    return city
}
function getCityFromForm(){
    var form = document.getElementById('createUpdateForm')
    var city = {}
    city.ID = form.querySelector('input[name="ID"]').value
    city.Name = form.querySelector('input[name="Name"]').value
    countriesList = document.getElementById('countriesList')
    city.CountryCode = countriesList.value
    city.CountryName = countriesList.options[countriesList.selectedIndex].text
    city.District = form.querySelector('input[name="District"]').value
    city.Population = parseInt(form.querySelector('input[name="Population"]').value,10)
    return city
}
function createCityAjax(city){
    $.ajax({
        "url": "/cities",
        "method":"POST",
        "data":JSON.stringify(city),
        "dataType": "JSON",
        contentType: "application/json; charset=utf-8",
        "success":function(result){
            showViewAll();
        },
        "error":function(xhr,status,error){
            console.log("error: "+status+" msg:"+error);
        }
    });
}
function updateCityAjax(city){
    $.ajax({
        "url": "/cities/"+encodeURI(city.ID),
        "method":"PUT",
        "data":JSON.stringify(city),
        "dataType": "JSON",
        contentType: "application/json; charset=utf-8",
        "success":function(result){
            showViewAll()
        },
        "error":function(xhr,status,error){
            console.log("error: "+status+" msg:"+error);
        }
    });
}
function deleteCityAjax(id){
    $.ajax({
        "url": "/cities/"+encodeURI(id),
        "method":"DELETE",
        "data":"",
        "dataType": "JSON",
        contentType: "application/json; charset=utf-8",
        "success":function(result){
        },
        "error":function(xhr,status,error){
            console.log("error: "+status+" msg:"+error);
        }
    });
}

//countries loaded for dropdown menu
function loadCountriesAjax(){
    $.ajax({
        "url": "/countries",
        "method":"GET",
        "data":"",
        "dataType": "JSON",
        "success":function(result){
            for (country of result){
                addCountryToList(country);
            }
            // Load main table after all countries are loaded
            getAllAjax();
        },
        "error":function(xhr,status,error){
            console.log("error: "+status+" msg:"+error);
        }
    });

}

loadCountriesAjax();