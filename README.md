# IATI Proxy

A proxy service that adds CORS to IATI registry data, so that it can be reused more easily.

Requests should be in the following format:

```
https://iati-proxy.herokuapp.com/get?id=[dataset ID]
```

So for example: https://iati-proxy.herokuapp.com/get?id=pwyf-org
