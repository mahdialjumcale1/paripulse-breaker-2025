hereJava.perform(function () {
    var OkHttpClient = Java.use("okhttp3.OkHttpClient");
    OkHttpClient.newCall.implementation = function (request) {
        console.log("[+] URL: " + request.url());
        console.log("[+] Headers: " + request.headers());
        var response = this.newCall(request);
        console.log("[+] Response: " + response);
        return response;
    };
});
