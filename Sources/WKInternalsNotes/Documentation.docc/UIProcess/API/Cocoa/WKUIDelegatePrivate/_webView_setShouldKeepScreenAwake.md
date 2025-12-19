# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:setShouldKeepScreenAwake:)``

画面スリープ抑止の可否を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView setShouldKeepScreenAwake:(BOOL)shouldKeepScreenAwake;
```

## Discussion
UIDelegate::UIClient が delegate を通じて値を設定し、処理できた場合は `true` を返す。

## References
- [`WKUIDelegatePrivate.h#L215`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L215)
- [`UIDelegate.mm#L170`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L170)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
