# ``WKInternalsNotes/WKWebView/_loadData(_:MIMEType:characterEncodingName:baseURL:userData:)``

`_loadData` を実行する。

## Objective-C Declaration
```objective-c
- (WKNavigation *)_loadData:(NSData *)data MIMEType:(NSString *)MIMEType characterEncodingName:(NSString *)characterEncodingName baseURL:(NSURL *)baseURL userData:(id)userData WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L195)
- [`WKWebView.mm#L4608`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4608)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
