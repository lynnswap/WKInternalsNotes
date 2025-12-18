# ``WKInternalsNotes/WKWebViewConfiguration/_relatedWebView``

関連する `WKWebView`（related page）

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setRelatedWebView:) WKWebView *_relatedWebView WK_API_DEPRECATED("Please migrate away from using _relatedWebView and talk to the WebKit team if there are difficulties doing so", macos(10.10, 15.2), ios(8.0, 18.2));
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: related page は設定されず、`WKWebView` は通常どおり独立して初期化される。
- `WKWebView` を設定すると: 新規 `WKWebView` の `pageConfiguration.relatedPage` が設定され、`processPool` は related 側と同一であることが要求される（違うと例外）。
- `nil` に戻すと: related page の関連付けを解除する。

## Details
- Deprecated（ヘッダコメント参照）

## References
- [`WKWebViewConfigurationPrivate.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L58)
- [`WKWebViewConfiguration.mm#L652`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L652)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
