# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didNotHandleWheelEvent:)``

ホイールイベントが処理されなかったことを通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didNotHandleWheelEvent:(NSEvent *)event WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
`NativeWebWheelEvent` の nativeEvent を delegate に渡す。

## References
- [`WKUIDelegatePrivate.h#L297`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L297)
- [`UIDelegate.mm#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L135)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
