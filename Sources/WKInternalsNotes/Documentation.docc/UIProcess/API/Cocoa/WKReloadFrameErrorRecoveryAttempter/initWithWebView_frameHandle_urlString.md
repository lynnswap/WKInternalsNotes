# ``WKInternalsNotes/WKReloadFrameErrorRecoveryAttempter/initWithWebView(_:frameHandle:urlString:)``

フレームリロード用の復旧アテンプタを初期化する。

## Objective-C Declaration
```objective-c
- (id)initWithWebView:(WKWebView *)webView frameHandle:(_WKFrameHandle *)frameHandle urlString:(const String&)urlString;
```

## Discussion
`WKWebView` とフレームハンドル、URL 文字列を保持する。

## References
- [`WKReloadFrameErrorRecoveryAttempter.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKReloadFrameErrorRecoveryAttempter.mm#L48)
- [`WKReloadFrameErrorRecoveryAttempter.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKReloadFrameErrorRecoveryAttempter.h#L35)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
