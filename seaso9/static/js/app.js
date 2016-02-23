"use strict";

var myApp = angular.module('myApp', [
  'ngRoute',
  'shopControllers'
]);

myApp.config(function($interpolateProvider ,$httpProvider){
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfCookieName = 'X-CSRFToken';
        $interpolateProvider.startSymbol('{/');
        $interpolateProvider.endSymbol('/}');
    });

myApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: '/static/partials/shop.html',
        controller: 'shopCtrl'
      }).
      when('/checkout', {
        templateUrl: '/checkout',
        controller: 'checkoutCtrl'
     }).
     when('/track-order', {
       templateUrl: '/static/partials/track_order.html',
       controller: 'trackOrderCtrl'
    }).
      otherwise({
        redirectTo: '/'
      });
  }]);
