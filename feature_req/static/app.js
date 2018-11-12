var featureRequestModel = {
    title : ko.observable(""),
    description : ko.observable(""),
    featureRequests :ko.observableArray([]),
    clients : [
    	{clientName: "Client A", id: 1},
    	{clientName: "Client B", id: 2},
    	{clientName: "Client C", id: 3}
    ],
    selectedClient : ko.observable(1),
    clientPriority : ko.observable(1),
    targetDate : ko.observable(""),
    productAreas:[{productArea:"Policies", id: 1},
    	{productArea: "Billings", id: 2},
    	{productArea: "Claims", id: 3},
    	{productArea: "Reports", id: 4}
    ],
    selectedProductArea : ko.observable(1),
    addRequest : function(formElement) {
    var x=$(formElement).serialize()
    // If the form data is valid, post the serialized form data to the web API.
    $(formElement).validate();
   
    if ($(formElement).valid()) {
        console.log("valid");
        console.log($)
            $.ajax({
                type: 'POST',
                url: '/request',
                data: $(formElement).serialize(),
                success: function(response) {
                    console.log(response)
                    window.location = "/";
                },
                error: function(error) {
                    console.log(error);
                }
            });
    }
   
    }

}
ko.applyBindings(featureRequestModel, document.getElementById("add_feature_request"));