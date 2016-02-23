var shopControllers = angular.module('shopControllers', []);


shopControllers.controller('shopCtrl', ['$scope', '$http','$location', function($scope, $http, $location) {
    $scope.products = [];
    $scope.cart_total_price = 0.0;
    $scope.cart_items = [];
    $scope.cart_item_count = 0;

    $http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
    $http.get('/api/products/').success(function(data) {
        $scope.products = data;
        $scope.cart_total_price = 0.0;
    });
    $http.get('/cart/get/').success(function(data) {
        $scope.cart_items = data.items;
        $scope.cart_item_count = data.items.length;
        var price = 0;
        for(i in data.items){
            price += data.items[i].price;
        }
        $scope.cart_total_price = price;
        console.log($scope.cart_items, $scope.cart_item_count, $scope.cart_total_price)
    });
    $scope.add_to_cart = function(item_id) {
        $http({
                url: '/cart/add-item/',
                method: "POST",
                data: $.param({
                    'item_id': item_id
                })
            })
            .then(function(response) {
                    $scope.cart_items = response.data.items;
                    $scope.cart_item_count = response.data.items.length;
                    var price = 0;
                    for(i in response.data.items){
                        price += response.data.items[i].price;
                    }
                    $scope.cart_total_price = price;
                    console.log($scope.cart_items, $scope.cart_item_count, $scope.cart_total_price);
                },
                function(response) {
                    console.log('failed');
                });
    };
    $scope.discard_cart = function(item_id) {
        $http({
                url: '/cart/discard/',
                method: "POST",
                data: $.param({
                    'item_id': item_id
                })
            })
            .then(function(response) {
                    $scope.cart_items = 0;
                    $scope.cart_item_count = 0;
                    $scope.cart_total_price = 0.0;
                },
                function(response) {
                    console.log('failed');
                });
    };

    $scope.remove_cart_item = function(item_id) {
        $http({
                url: '/cart/remove-item/',
                method: "POST",
                data: $.param({
                    'item_id': item_id
                })
            })
            .then(function(response) {
                    $scope.cart_items = response.data.items;
                    $scope.cart_item_count = response.data.items.length;
                    var price = 0;
                    for(i in response.data.items){
                        price += response.data.items[i].price;
                    }
                    $scope.cart_total_price = price
                },
                function(response) {
                    console.log('failed');
                });
    };
}]);

shopControllers.controller('checkoutCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
    $('#cartModal').modal('hide');
    $('body').removeClass('modal-open');
    $('.modal-backdrop').remove();
    $scope.submit = function() {
        console.log('submitted');
        console.log($scope.checkout.name, $scope.checkout.email);
        $http({
                url: '/checkout/',
                method: "POST",
                data: $.param({
                    'name': $scope.checkout.name,
                    'email': $scope.checkout.email,
                    'mobile': $scope.checkout.mobile,
                    'address': $scope.checkout.address,
                    'city': $scope.checkout.city,
                    'state': $scope.checkout.state,
                    'pin': $scope.checkout.pin,
                    'payment_option': $scope.checkout.payment_option
                })
            })
            .then(function(response) {
                    console.log(response);
                    console.log('hellos');
                    $scope.cart_items = 0;
                    $scope.cart_item_count = 0;
                    $scope.cart_total_price = 0;
                    alert('Order was sucessfull!')
                    $location.url('/');
                    console.log('failed to route!')
                },
                function(response) {
                    console.log('failed');
                });
    }
}]);


shopControllers.controller('shopHomeCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
    $scope.order = {}
    $scope.trackorder = function() {
        $http({
                url: '/track-order/?orderid=' + $scope.orderid,
                method: "GET",
            })
            .then(function(response) {
                    $('#trackOrderModal').modal('hide');
                    $scope.order = response.data;
                    $location.url('/track-order');
                },
                function(response) {
                    console.log('failed');
                });
    };
}]);


shopControllers.controller('trackOrderCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
    console.log('helllo', $scope.order);
}]);
