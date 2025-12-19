# ``WKInternalsNotes/WKWebView/_addShortcut(_:)``

`_addShortcut` を追加する。

## Objective-C Declaration
```objective-c
- (void)_addShortcut:(id)sender;
```

## Discussion
iOS では `WKContentViewInteraction` 側のハンドラに委譲される。

## References
- [`WKWebViewIOS.h#L132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L132)
- [`WKContentViewInteraction.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
