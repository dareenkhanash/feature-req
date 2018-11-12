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
    addRequest : function(formData) {
    // If the form data is valid, post the.
    $(formData).validate();
    if ($(formData).valid()) {
        console.log("valid");
        console.log($)
            $.ajax({
                type: 'POST',
                url: '/request',
                data: $(formData).serialize(),
                success: function(response) {
                    console.log(response)
                    window.location = "/";
                },
                error: function(error) {
                    console.log(error);
                }
            });
    }
   
    },
    getData:function(){
        var self=this;
        console.log(self.featureRequests)
        console.log("hi")
        $.ajax({
            url: '/getData',
            type: 'GET',
            success: function(response) {
                console.log("success")
                console.log(response.requests)
                response.requests.map(request=>{
                    self.featureRequests.push(request)
                })
                
                console.log('done')
                console.log(self.featureRequests)
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

}
featureRequestModel.getData();
ko.applyBindings(featureRequestModel, document.getElementById("feature_requests"));