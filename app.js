var uploader = new qq.s3.FineUploader({
  debug: false, // defaults to false
  element: document.getElementById("fine-uploader"),
  request: {
    // S3 Bucket URL
    endpoint: "https://s3-upload-using-lambda-kiwony.s3.amazonaws.com",
    // iam ACCESS KEY
    accessKey: "AKIAZVQXJIKFNXRFLHYZ",
  },
  objectProperties: {
    region: "us-east-1",
    key(fileId) {
      var prefixPath = "uploads";
      var filename = this.getName(fileId);
      return prefixPath + "/" + filename;
    },
  },
  signature: {
    // version
    version: 4,
    // AWS API Gate URL
    endpoint: "https://yr5udx91c1.execute-api.us-east-1.amazonaws.com/live",
  },
  retry: {
    enableAuto: true, // defaults to false
  },
});
