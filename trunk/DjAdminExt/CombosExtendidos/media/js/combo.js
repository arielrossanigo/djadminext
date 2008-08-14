function populateSelect(url, field_master, field_detail ,master_app_name, master_model_name, detail_set, detail_field_name) {
    var sel = document.getElementById(field_master);
    var dest = document.getElementById(field_detail);
    while (dest.options.length > 1) {
        dest.options[1]=null;
    }
    dest.options[0]= new Option("---------","0");
    var id = sel.options[sel.selectedIndex].value;
    $.getJSON(url + id + "/" + master_app_name + "/" + master_model_name + "/" + detail_set + "/" + detail_field_name + "/" , function (data){
        $.each(data, function(k, v){
            dest.options[k]= new Option(data[k]["fields"][detail_field_name],data[k]["pk"]);
        });
    });

    }


