# ``WKInternalsNotes/WKWebView/replace(_:)``

`replace` を実行する。

## Objective-C Declaration
```objective-c
- (void)replace:(id)sender;
```

## Discussion
iOS では `WKContentViewInteraction` 側のハンドラに委譲される。

## References
- [`WKWebViewIOS.h#L138`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L138)
- [`WKContentViewInteraction.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
