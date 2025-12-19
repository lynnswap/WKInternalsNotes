# ``WKInternalsNotes/WKWebView/_lookup(_:)``

`_lookup` を実行する。

## Objective-C Declaration
```objective-c
- (void)_lookup:(id)sender;
```

## Discussion
iOS では `WKContentViewInteraction` 側のハンドラに委譲される。

## References
- [`WKWebViewIOS.h#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L134)
- [`WKContentViewInteraction.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
