# ``WKInternalsNotes/WKInspectorWKWebView/inspectorWKWebViewDelegate``

弱参照の delegate を保持し、通知の監視を切り替える。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <WKInspectorWKWebViewDelegate> inspectorWKWebViewDelegate;
```

## Default Value
初期値は `nil`。

## Discussion
setter は既存 delegate がある場合に通知監視を解除し、新しい delegate を設定後に `NSWindowDidBecomeKeyNotification` を監視する。

## References
- [`WKInspectorWKWebView.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorWKWebView.h#L33)
- [`WKInspectorWKWebView.mm#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorWKWebView.mm#L57)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
