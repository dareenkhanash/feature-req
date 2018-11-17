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
    errors:ko.observable(""),
    selectedProductArea : ko.observable(1),
        addRequest : function(formElement) {
            var self=this;
            // If the form data is valid, post request
            $(formElement).validate();    
            if ($(formElement).valid()) {
                    $.ajax({
                        type: 'POST',
                        url: '/request',
                        data: $(formElement).serialize(),
                        success: function(response) {
                            if(response.error){
                                console.log(response.error)
                                self.errors("Can not Add request")
                            }else{
                                window.location = "/";
                            }
                        
                        },
                        error: function(error) {
                            console.log(error);
                        }
                    });
            }
        
        },
    getData:function(){
        var self=this;
        $.ajax({
            url: '/getData',
            type: 'GET',
            success: function(response) {
                console.log(response)
                self.featureRequests(response.requests)
                return true;
            },
            error: function(error) {
                console.log(error);
                return false
            }
        });
        return true
    },
    deleteRequest: function(requestId) {
        var self=this;
    	$.ajax({
            url: '/request/delete/'+ requestId,
            type: 'DELETE',
            success: function(response) {
                console.log(response);
                self.getData();
            },
            error: function(error) {
                console.log(error);
            }
        });
    },
    editRequest: function(requestId) {
        window.location = "/request/"+requestId;
    },
    updateRequest: function(formData) {
        var self=this;
        $(formData).validate();
        if ($(formData).valid()) {
                $.ajax({
                    type: 'POST',
                    url: '/request/update',
                    data: $(formData).serialize(),
                    success: function(response) {
                        if(response.error){
                            console.log(response.error)
                            self.errors("Cannot update request")
                        }else{
                            window.location = "/";
                        }
                    },
                    error: function(error) {
                        console.log(error);
                    }
                });
         }
    },
    editData: function(client) {
        //change selected client for the request we want to update
        this.selectedClient(client);

    },
    editProductArea: function(value) {
        //change selected product area for the request we want to update
        this.selectedProductArea(value)
    }
    
}

ko.applyBindings(featureRequestModel);