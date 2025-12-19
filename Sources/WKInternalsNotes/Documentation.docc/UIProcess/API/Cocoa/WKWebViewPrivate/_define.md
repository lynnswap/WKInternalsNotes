# ``WKInternalsNotes/WKWebView/_define(_:)``

`_define` を実行する。

## Objective-C Declaration
```objective-c
- (void)_define:(id)sender;
```

## Discussion
iOS では `WKContentViewInteraction` 側のハンドラに委譲される。

## References
- [`WKWebViewIOS.h#L133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L133)
- [`WKContentViewInteraction.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
