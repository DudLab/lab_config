// Submit form.
function submit_form()
{
    var data_elements = document.querySelectorAll("#form_id input[type=text]");
    var data_obj = {};
    for (var i = 0; i < data_elements.length; i++)
    {
        data_obj[data_elements[i].name] = data_elements[i].value;
    }
    if (validate_data(data_obj)) // Calling validation function
    {
        var textToSave = JSON.stringify(data_obj, null, 4);
        var textToSaveAsBlob = new Blob([textToSave], {type:"text/plain"});
        var textToSaveAsURL = window.URL.createObjectURL(textToSaveAsBlob);
        var fileNameToSaveAs = document.getElementById("inputFileNameToSaveAs").value;

        var downloadLink = document.createElement("a");
        downloadLink.download = fileNameToSaveAs;
        downloadLink.innerHTML = "Download File";
        downloadLink.href = textToSaveAsURL;
        downloadLink.onclick = destroyClickedElement;
        downloadLink.style.display = "none";
        document.body.appendChild(downloadLink);

        downloadLink.click();
    }
}

function destroyClickedElement(event)
{
    document.body.removeChild(event.target);
}

// Data validation function.
function validate_data(a_data_obj)
{
    for (var key in a_data_obj.length)
    {
        if (a_data_obj[key] === '')
        {
            alert("Please fill all fields...!!!!!!");
	}
    }

    return true;
}
