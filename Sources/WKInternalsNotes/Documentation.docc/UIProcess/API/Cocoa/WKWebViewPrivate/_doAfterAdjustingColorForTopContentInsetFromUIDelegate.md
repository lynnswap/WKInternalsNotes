# ``WKInternalsNotes/WKWebView/_doAfterAdjustingColorForTopContentInsetFromUIDelegate(_:)``

`_doAfterAdjustingColorForTopContentInsetFromUIDelegate` を実行する。

## Objective-C Declaration
```objective-c
- (void)_doAfterAdjustingColorForTopContentInsetFromUIDelegate:(Function<void()>&&)callback;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewInternal.h#L582`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L582)
- [`WKWebView.mm#L3366`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3366)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
