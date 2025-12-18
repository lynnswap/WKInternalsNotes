# ``WKInternalsNotes/WKNavigationResponse/_proxyName``

プロキシ名を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *_proxyName WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Default Value
`_navigationResponse->response().proxyName().createNSString()` の結果。

## Discussion
ResourceResponse が保持する proxyName を `NSString` として返す。

## References
- [`WKNavigationResponsePrivate.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponsePrivate.h#L37)
- [`WKNavigationResponse.mm#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationResponse.mm#L110)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
