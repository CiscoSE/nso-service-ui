/**
 * @license
 * Copyright (c) 2018 Cisco and/or its affiliates.
 *
 * This software is licensed to you under the terms of the Cisco Sample
 * Code License, Version 1.0 (the "License"). You may obtain a copy of the
 * License at
 *
 *                https://developer.cisco.com/docs/licenses
 *
 * All use of the material herein must be in accordance with the terms of
 * the License. All rights not expressly granted by the License are
 * reserved. Unless required by applicable law or agreed to separately in
 * writing, software distributed under the License is distributed on an "AS
 * IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied.
 */
var authModule = angular.module('authModule',['ngRoute'])

authModule.service("AuthService", function(){
    function url_base64_decode(str){
        return window.atob(str)
    }

    this.url_base64_decode = url_base64_decode
})

authModule.controller('AuthCtrl', function($scope, $http, $window, AuthService){
    $scope.user = {username: '', password: ''}
    $scope.isAuthenticated = false

    $scope.submit = function (){
        $http
            .post('api/login', $scope.user)
            .then(function (response, status, headers, config){
                $window.sessionStorage.token = response.data.token;
                $scope.isAthenticated = true;
                $scope.message = "Success! Loading application";
                $window.location.href = '/index'
            })
            .catch(function(response, status, headers, config){
                delete $window.sessionStorage.token;
                $scope.isAuthenticated = false;
                $scope.message = response.data;
            })
    }

    $scope.logout = function() {
        $scope.isAuthenticated = false;
        alert("loggedOut!")
    }
});

authModule.factory("authInterceptor", function($rootScope, $q, $window){
    return {
        request: function(config){
            config.headers = config.headers  || {};
            if ($window.sessionStorage.token){
                config.headers.Authorization = 'Bearer ' + $window.sessionStorage.token;
            }
            return config;
        },
        responseError: function(rejection){
            if (rejection.status === 401){
                //Manage common 401 actions
            }
            return $q.reject(rejection);
        }
    };
});

authModule.config(function ($httpProvider){
    $httpProvider.interceptors.push('authInterceptor');
});

authModule.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{a');
  $interpolateProvider.endSymbol('a}');
}]);
