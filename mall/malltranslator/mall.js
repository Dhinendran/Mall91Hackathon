app.controller('main', function($scope, $state, ) {

    $scope.resetForm = function() {
      $scope.form = {
        img : "",
      }
    }


    $scope.submit = function () {
      console.log( $scope.form);
      var method = "POST"
      var fd = new FormData();
      fd.append('image' , $scope.img);
      var url = 'malltranslator/images'
      var dataToSend = {
        image:$scope.img,
      }
      $http({method : 'POST' , url : 'malltranslator/images', data : form  , transformRequest: angular.identity, headers: {'Content-Type': undefined}}).
      then(function(response){
        return
      });
    }
