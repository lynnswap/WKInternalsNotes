# ``WKInternalsNotes/WKFullScreenViewController/_webView``

フルスクリーン対象の `WKWebView` への弱参照。

## Objective-C Declaration
```objective-c
@property (weak, nonatomic) WKWebView *_webView;
```

## Default Value
初期値は `nil`。

## Discussion
循環参照を避けるため弱参照として保持し、`initWithWebView:` で設定される。

## References
- [`WKFullScreenViewController.mm#L144`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L144)
- [`WKFullScreenViewController.mm#L197`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L197)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
