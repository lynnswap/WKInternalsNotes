# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:requestUserMediaAuthorizationForDevices:url:mainFrameURL:decisionHandler:)``

ユーザーメディアのデバイス許可を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView requestUserMediaAuthorizationForDevices:(_WKCaptureDevices)devices url:(NSURL *)url mainFrameURL:(NSURL *)mainFrameURL decisionHandler:(void (^)(BOOL authorized))decisionHandler WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
UIClient が要求デバイス種別と frame URL / mainFrameURL を渡し、`decisionHandler` 経由で許可/拒否を受け取る。

## References
- [`WKUIDelegatePrivate.h#L166`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L166)
- [`UIDelegate.mm#L1442`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1442)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
