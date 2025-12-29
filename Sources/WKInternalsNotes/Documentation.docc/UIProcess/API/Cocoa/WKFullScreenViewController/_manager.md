# ``WKInternalsNotes/WKFullScreenViewController/_manager``

関連する `WebFullScreenManagerProxy` を取得する。

## Objective-C Declaration
```objective-c
@property (readonly, nonatomic) WebKit::WebFullScreenManagerProxy* _manager;
```

## Default Value
ページが無い場合は `nullptr`。

## Discussion
`_webView` の `WebPageProxy` から `fullScreenManager()` を返す。

## References
- [`WKFullScreenViewController.mm#L145`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L145)
- [`WKFullScreenViewController.mm#L996`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L996)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
