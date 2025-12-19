# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:configurationForLocalInspector:)``

ローカルインスペクタ用の設定を delegate から取得する。

## Objective-C Declaration
```objective-c
- (_WKInspectorConfiguration *)_webView:(WKWebView *)webView configurationForLocalInspector:(_WKInspector *)inspector WK_API_AVAILABLE(macos(12.0));
```

## Discussion
UIClient が delegate 実装時に `_webView:configurationForLocalInspector:` を呼び出し、返った設定を API::InspectorConfiguration として使用する。

## References
- [`WKUIDelegatePrivate.h#L321`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L321)
- [`UIDelegate.mm#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L146)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
