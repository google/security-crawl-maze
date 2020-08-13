const app = angular.module("app", ["ngRoute"]);
app.config(($routeProvider) => {
  $routeProvider.when("/", {
    template : "<p> Default content </p>"
  })
  .when("/ng-href.found", {
    template : "<p> Paragraph linked by ng-href</p>"
  });
});
