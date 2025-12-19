# ``WKInternalsNotes/WKWebView/_getContentsAsStringWithCompletionHandlerKeepIPCConnectionAliveForTesting(_:)``

`_getContentsAsStringWithCompletionHandlerKeepIPCConnectionAliveForTesting` を取得する。

## Objective-C Declaration
```objective-c
- (void)_getContentsAsStringWithCompletionHandlerKeepIPCConnectionAliveForTesting:(void (^)(NSString *, NSError *))completionHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L365`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L365)
- [`WKWebView.mm#L5466`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5466)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
