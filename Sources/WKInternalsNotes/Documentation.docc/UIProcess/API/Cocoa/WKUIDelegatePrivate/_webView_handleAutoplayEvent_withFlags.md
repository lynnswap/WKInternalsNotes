# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:handleAutoplayEvent:withFlags:)``

自動再生イベントとフラグを delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView handleAutoplayEvent:(_WKAutoplayEvent)event withFlags:(_WKAutoplayEventFlags)flags WK_API_AVAILABLE(macos(10.13.4), ios(14.0));
```

## Discussion
UIClient が `WebCore::AutoplayEvent` と flags を `_WKAutoplayEvent` / `_WKAutoplayEventFlags` に変換して delegate へ渡す。

## References
- [`WKUIDelegatePrivate.h#L198`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L198)
- [`UIDelegate.mm#L834`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L834)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
